from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from threading import Thread
from logon import *
from meta import *

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
resolveSymbolName = 'ZUC'

account_id = 16883045 # change the value according to your account_id

def new_entitlement_request(client, request_id, account_id, contract_id):
    client_msg = ClientMsg()
    information_request = client_msg.information_requests.add()
    information_request.id = request_id
    information_request.order_entitlement_request.contract_id = contract_id
    information_request.order_entitlement_request.account_id = account_id

    client.send_client_message(client_msg)
    server_msg = client.receive_server_message()



if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    baseTime = logon(client, user_name, password)
    msg_id = 1
    contract_id = resolve_symbol(client, resolveSymbolName, msg_id).contract_id
    msg_id += 1
    new_entitlement_request(client, msg_id, account_id, contract_id)
    logoff(client)
    client.disconnect()
