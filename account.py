from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from logon import *

host_name = 'wss://demoapi.cqg.com:443' 
user_name = ''
password = ''

# Request for all accounts this user is authorized to trade/monitor
# Accounts are grouped by sales series, which are grouped by brokerages
def resolve_account(client, msg_id=1, subscribe=None):
    client_msg = ClientMsg()
    information_request = client_msg.information_requests.add()
    information_request.id = msg_id
    information_request.accounts_request.SetInParent()

    client.send_client_message(client_msg)
    server_msg = client.receive_server_message()


if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    logon(client, user_name, password)
    resolve_account(client)
    logoff(client)
    client.disconnect()
