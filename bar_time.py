from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from logon import *
from meta import *
# Use the datetime lib and other 2 functions below to calculate the
# from_utc_time, which determines the time_bar_request range
from datetime import datetime
host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''

resolveSymbolName = 'ZUC'
bars_number = 10
minutely_index = 8 # hourly_index = 7, daily_index = 6, please find other indexes in protocol
milliseconds_in_minute = 60000

# function returns the current_time in milliseconds, in order to calculate the from_utc_time
current_milli_time = lambda: int(round( datetime.utcnow().timestamp() * 1000))
# function returns the baseTime in milliseconds, in order to calculate the from_utc_time
base_time_milli_time = lambda: int(round(datetime.strptime\
                        (baseTime,"%Y-%m-%dT%H:%M:%S").timestamp() * 1000))

# in this example, we are going to request historical S&P 500 minutely 10 bars' data
# User can also request hourly data, daily data and so on
# The parameter from_utc_time will always be in milliseconds format
def request_bar_time(client, msg_id, contract_id):
    client_msg = ClientMsg()
    tb_request = client_msg.time_bar_requests.add()
    tb_request.request_id = msg_id
    tb_request.time_bar_parameters.contract_id = contract_id
    tb_request.time_bar_parameters.bar_unit = minutely_index
    # Important: Because millisecond time integers are very large, this API uses 
    # a process to shorten time values used for requesting and receiving data
    # The getTime() function formats the date to the number of milliseconds since January 1, 1970, 00:00:00.
    # To get historical data starting from a specific time, first we take the getTime() value and subtract
    # the base_time we received from the logon_report, then we subtract the amount of time
    # (converted to milliseconds) for which we want data. This value is "params.from_utc_time"
    # the server will send historical data from "params.from_utc_time" to now
    tb_request.time_bar_parameters.from_utc_time = current_milli_time()\
                - base_time_milli_time() - bars_number * milliseconds_in_minute
    client.send_client_message(client_msg)
    while True:
        server_msg = client.receive_server_message()
        for i in range(len(server_msg.time_bar_reports)):
            if server_msg.time_bar_reports[i].is_report_complete is True:
                break
        break


if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    baseTime = logon(client, user_name, password)
    print("base_time in milliseconds is: " + str(base_time_milli_time()))
    msg_id = 1
    contract_id = resolve_symbol(client, resolveSymbolName, msg_id).contract_id
    msg_id += 1
    request_bar_time(client, msg_id, contract_id)
    logoff(client)
    client.disconnect()
