from WebAPI.webapi_2_pb2 import *
from WebAPI.historical_2_pb2 import *
from WebAPI import webapi_client
from logon import *
from meta import *
from datetime import datetime

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''

resolveSymbolName = 'ZUC'

milliseconds_in_second = 1000
number_of_seconds = 1

current_milli_time = lambda: int(round(datetime.utcnow().timestamp() * 1000))
base_time_milli_time = lambda: int(round(datetime.strptime\
                        (baseTime,"%Y-%m-%dT%H:%M:%S").timestamp() * 1000))

# in this example we are going to request 1 second tick data, there could be
# any number of data inside 1 second, in average, there are 200-400 quotes inside
# one minute for a high liquidity contract as EP
def request_time_and_sales(client, msg_id, contract_id):
    client_msg = ClientMsg()
    ts_request = client_msg.time_and_sales_requests.add()
    ts_request.request_id = msg_id
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
    baseTime = logon(client, user_name, password)
    print("base_time in milliseconds is: " + str(base_time_milli_time()))
    msg_id = 1
    contract_id = resolve_symbol(client, resolveSymbolName, msg_id).contract_id
    msg_id += 1
    request_time_and_sales(client, msg_id, contract_id)
    logoff(client)
    client.disconnect()
