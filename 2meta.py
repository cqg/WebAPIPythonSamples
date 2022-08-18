from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
# the symbol_name is the CQG symbol used in symbol_resolution_request in information_request
symbol_name = 'ZUC'

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

# information_request is one type of client message, and allows for many optional parameters.
# symbol_resolution_request returns a session-specific server-defined contract id for the requested symbol.

def resolve_symbol(symbol_name, msg_id=1, subscribe=None):
    # after the server confirm that we login successfully, we can send information_request
    # contains the symbol_resolution_request, the real time data, historical data, 
    # tick data, and order activities are all depended on symbol_resolution_report
    client_msg = ClientMsg()
    information_request = client_msg.information_requests.add()
    # in this sample, we only ask for one symbol request.
    information_request.id = msg_id
    if subscribe is not None:
        information_request.subscribe = subscribe
    information_request.symbol_resolution_request.symbol = symbol_name
    client.send_client_message(client_msg)

    server_msg = client.receive_server_message()
    return server_msg.information_reports[0].symbol_resolution_report.contract_metadata


if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    logon(user_name, password)

    resolve_symbol(symbol_name)

    client.disconnect()
