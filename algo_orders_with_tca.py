from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from threading import Thread

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
resolveSymbolName = 'ZUC'

trade_subscription_id = 1
request_id = 2 # request id must have unique value per trader per day

account_id = 00000000 # change the value according to your account_id
contract_id = 1
cl_order_id = '1' # every order must have unique cl_order_id per trader per day
order_type = 1 # 1 means MKT 2 means LMT 3 means STP 4 means STL
duration = 1
side = 1 # 1 means buy and 2 means sell
qty_significant = 1
qty_exponent = 0
is_manual = False

def logon(user_name, password,
          client_app_id='WebApiTest', client_version='python-client-test-2-87',
          protocol_version_major=2,protocol_version_minor = 87):
    client_msg = ClientMsg()
    logon = client_msg.logon
    logon.user_name = user_name
    logon.password = password
    logon.client_app_id = client_app_id
    logon.client_version = client_version
    logon.protocol_version_major = protocol_version_major
    logon.protocol_version_minor = protocol_version_minor
    client.send_client_message(client_msg)
    server_msg = client.receive_server_message()
    if server_msg.logon_result.result_code == 0:
        return server_msg.logon_result.base_time
    else:
        raise Exception("Can't login: " + server_msg.logon_result.text_message)

def resolve_symbol(symbol_name, msg_id=1, subscribe=None):
    client_msg = ClientMsg()
    information_request = client_msg.information_requests.add()
    information_request.id = msg_id
    if subscribe is not None:
        information_request.subscribe = subscribe
    information_request.symbol_resolution_request.symbol = symbol_name
    client.send_client_message(client_msg)

    server_msg = client.receive_server_message()
    return server_msg.information_reports[0].symbol_resolution_report.contract_metadata

def request_trade_subscription(trade_subscription_id):
    client_msg = ClientMsg()
    trade_sub_request = client_msg.trade_subscriptions.add()
    trade_sub_request.id = trade_subscription_id
    trade_sub_request.subscribe = True
    trade_sub_request.subscription_scopes.append(1)
    #trade_sub_request.subscription_scopes.append(2)
    #trade_sub_request.subscription_scopes.append(3)
    client.send_client_message(client_msg)

    while True:
        server_msg = client.receive_server_message()
        if server_msg.trade_snapshot_completions is not None:
            server_msg = client.receive_server_message()
            break

def new_order_request(request_id, account_id, contract_id,
                        cl_order_id, order_type, duration, side,
                        qty_significant, qty_exponent, is_manual):
    client_msg = ClientMsg()
    order_request = client_msg.order_requests.add()
    order_request.request_id = request_id
    order_request.new_order.order.account_id = account_id
    order_request.new_order.order.when_utc_time = 0
    order_request.new_order.order.contract_id = contract_id
    order_request.new_order.order.cl_order_id = cl_order_id
    order_request.new_order.order.order_type = order_type
    order_request.new_order.order.duration = duration
    order_request.new_order.order.side = side
    order_request.new_order.order.qty.significand = qty_significant
    order_request.new_order.order.qty.exponent = qty_exponent
    order_request.new_order.order.is_manual = is_manual

    order_request.new_order.order.algo_strategy = "CQG ARRIVALPRICE"
    extra_attributes = order_request.new_order.order.extra_attributes.add()
    extra_attributes.name = "ALGO_CQG_cost_model"
    extra_attributes.value = "1"

    # add the limit_price when order_type is LIMIT
    # order_request.new_order.order.limit_price = xxxx

    client.send_client_message(client_msg)
    while True:
        server_msg = client.receive_server_message()
      	if server_msg.order_statuses is not None:
            for order_statuses in server_msg.order_statuses:
                # Algo analytics could be found here, is it available or not depends on algo execution,
                # i.e. it could be available not just from start, but after algo is executing for a while
                for exchange_extra_attribute in order_statuses.exchange_extra_attributes:
                    if exchange_extra_attribute.name == "TCAValues":
                        # TCA = Transaction Cost Analysis
                        # A JSON string containing TCA values related to algo order execution.
                        # Example of string: {"TCA param 1 name":"TCA param 1 value", "TCA param 2 name" :"TCA param 2 value"}
                        print("Exchange analytics: ", exchange_extra_attribute.value)

        if server_msg.trade_snapshot_completions is not None:
            server_msg = client.receive_server_message()



if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    baseTime = logon(user_name, password)
    contract_metadata = resolve_symbol(resolveSymbolName)

    t1 = Thread(target = request_trade_subscription(trade_subscription_id))
    t1.setDaemon(True)
    t1.start()

    t2 = Thread(target = new_order_request(request_id, account_id, contract_id, cl_order_id, order_type, duration, side, qty_significant, qty_exponent, is_manual))
    t2.setDaemon(True)
    t2.start()

    client.disconnect()
