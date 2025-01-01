from WebAPI.webapi_2_pb2 import *
from logon import *
from WebAPI import webapi_client

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
# the symbol_name is the CQG symbol used in symbol_resolution_request in information_request
symbol_name = 'ZUC'

# information_request is one type of client message, and allows for many optional parameters.
# symbol_resolution_request returns a session-specific server-defined contract id for the requested symbol.

def resolve_symbol(client, symbol_name, msg_id, subscribe=None):
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
    logon(client, user_name, password)
    msg_id = 1
    resolve_symbol(client, symbol_name, msg_id)

    logoff(client)
    client.disconnect()
