from WebAPI.webapi_2_pb2 import *
from logon import *
from meta import *
from WebAPI import webapi_client

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
symbol_name = 'ZSE'


def session_information_request(client, session_info_id, msg_id, subscribe=None):
    client_msg = ClientMsg()
    information_request = client_msg.information_requests.add()
    information_request.id = msg_id
    if subscribe is not None:
        information_request.subscribe = subscribe
    information_request.session_information_request.session_info_id = session_info_id
    client.send_client_message(client_msg)

    server_msg = client.receive_server_message()
    return server_msg.information_reports[0].session_information_report


if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    logon(client, user_name, password)
    msg_id = 1
    session_info_id = resolve_symbol(client, symbol_name, msg_id).session_info_id
    msg_id += 1
    session_information_request(client, session_info_id, msg_id)

    logoff(client)
    client.disconnect()
