from WebAPI.webapi_2_pb2 import *
from WebAPI.historical_2_pb2 import *
from WebAPI import webapi_client
from datetime import datetime

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
resolveSymbolName = 'ZUC'

milliseconds_in_second = 1000
number_of_seconds = 1

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


current_milli_time = lambda: int(round(datetime.utcnow().timestamp() * 1000))
base_time_milli_time = lambda: int(round(datetime.strptime\
                        (baseTime,"%Y-%m-%dT%H:%M:%S").timestamp() * 1000))

# in this example we are going to request 1 second tick data, there could be
# any number of data inside 1 second, in average, there are 200-400 quotes inside
# one minute for a high liquidity contract as EP
def request_time_and_sales(contract_id):
    client_msg = ClientMsg()
    ts_request = client_msg.time_and_sales_requests.add()
    ts_request.request_id = 3
    ts_request.time_and_sales_parameters.contract_id = contract_id
    ts_request.time_and_sales_parameters.level = TimeAndSalesParameters.LEVEL_TRADES_BBA_VOLUMES
    ts_request.time_and_sales_parameters.from_utc_time = \
                current_milli_time() - base_time_milli_time() -  milliseconds_in_second * number_of_seconds
    client.send_client_message(client_msg)
    while True:
        server_msg = client.receive_server_message()
        for i in range(len(server_msg.time_and_sales_reports)):
            if server_msg.time_and_sales_reports[i].is_report_complete is True:
                break
        break


if __name__ == '__main__':
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    baseTime = logon(user_name, password)
    contract_metadata = resolve_symbol(resolveSymbolName)
    request_time_and_sales(contract_metadata.contract_id)
    client.disconnect()
