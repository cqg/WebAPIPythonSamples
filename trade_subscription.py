from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from logon import *
from WebAPI.trade_routing_2_pb2 import *

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''

def request_trade_subscription(client, msg_id):
    client_msg = ClientMsg()
    trade_sub_request = client_msg.trade_subscriptions.add()
    # user-defined ID of a request that should be unique to match with possible OrderRequestReject.
    trade_sub_request.id = msg_id
    trade_sub_request.subscribe = True
    # the client can specify the accounts in the request:
    #trade_sub_request.publication_type=1
    #trade_sub_request.account_ids.append(16883045)
    # subscription_scope is an array, we use "extend" to add subscription_scope
    # 1 means order_status, 2 means positions_status, 3 means colleteral_status, deprecated, use 4 instead
    # 4 means account_summary_status, 5 means exchange_positions, 6 means exchange_balances
    trade_sub_request.subscription_scopes.extend([1])#,2,4,5,6]) 
    ## user needs account_summary_parameters when scopes contain 4
    ##account_summary_parameters = trade_sub_request.account_summary_parameters
    # 8 means purchasing_power, 15 means urrent_balance, 16 means profit_loss
    ##account_summary_parameters.requested_fields.extend([8,15,16])
    client.send_client_message(client_msg)

    while True: 
        server_msg = client.receive_server_message()
        if server_msg.trade_snapshot_completions is not None:
            server_msg = client.receive_server_message()
            break

if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    baseTime = logon(client, user_name, password)
    msg_id = 1
    request_trade_subscription(client, msg_id)
    logoff(client)
    client.disconnect()