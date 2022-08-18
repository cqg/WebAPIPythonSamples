from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''

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

def request_trade_subscription():
    client_msg = ClientMsg()
    trade_sub_request = client_msg.trade_subscriptions.add()
    # user-defined ID of a request that should be unique to match with possible OrderRequestReject.
    trade_sub_request.id = 1
    trade_sub_request.subscribe = True
    # subscription_scope is an array, we use "append" to add subscription_scope
    #trade_sub_request.subscription_scopes.append(1) # 1 means order_status
    trade_sub_request.subscription_scopes.append(2) # 2 means positions_status
    #trade_sub_request.subscription_scopes.append(3) # 3 means collateral_status
    client.send_client_message(client_msg)

    while True: 
        server_msg = client.receive_server_message()

if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    baseTime = logon(user_name, password)
    request_trade_subscription()
    client.disconnect()
