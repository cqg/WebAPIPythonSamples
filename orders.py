from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from threading import Thread
from logon import *
from meta import *
from trade_subscription import *

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
resolveSymbolName = 'ZUC'

request_id = 1 # request id must have unique value per trader per day
account_id = 16883045 # change the value according to your account_id
contract_id = 1
cl_order_id = '1' # every order must have unique cl_order_id per trader per day
order_type = 1 # 1 means MKT 2 means LMT 3 means STP 4 means STL
duration = 1
side = 1 # 1 means buy and 2 means sell
qty_significant = 1
qty_exponent = 0
is_manual = False

def new_order_request(client, request_id, account_id, contract_id, 
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
    # add the limit_price when order_type is LIMIT
    # order_request.new_order.order.limit_price = xxxx
    client.send_client_message(client_msg)
    while True:
        server_msg = client.receive_server_message()
        if server_msg.trade_snapshot_completions is not None:
            server_msg = client.receive_server_message()


if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    baseTime = logon(client, user_name, password)
    msg_id = 1
    contract_metadata = resolve_symbol(client, resolveSymbolName, msg_id)
    msg_id += 1
    t1 = Thread(target = request_trade_subscription(client, msg_id), daemon=True)
    t2 = Thread(target = new_order_request(client, request_id, account_id, contract_id, cl_order_id, order_type, duration, side, qty_significant, qty_exponent, is_manual), daemon=True)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    #logoff(client)
    #client.disconnect()
