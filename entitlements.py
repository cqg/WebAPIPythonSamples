from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from threading import Thread

host_name = ''
user_name = ''
password = ''
resolveSymbolName = 'ZUC'

request_id = 1 # request id must have unique value per trader per day
account_id = 0000000 # change the value according to your account_id
contract_id = 1


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


def new_entitlement_request(request_id, account_id, contract_id):
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
    baseTime = logon(user_name, password)
    contract_metadata = resolve_symbol(resolveSymbolName)
    new_entitlement_request(request_id, account_id, contract_id)
    client.disconnect()
