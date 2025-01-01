# logging on is a prerequisite to accomplishing anything using the Web API.
# All other samples require a successful logon to work.
# The first step to logon is to build connection with the WebAPi Server.
# Second, logon message is built with valid credentials and sent as a client message.
# Success code in WebAPI when logon_result.result_code = 0.

from WebAPI.webapi_2_pb2 import *
from WebAPI.user_session_2_pb2 import LogonResult
from WebAPI import webapi_client

# the host_name is the stage server url we will connect to in demo environment.
host_name = 'wss://demoapi.cqg.com:443' 
user_name = ''
password = ''

def logon(client, user_name, password, 
          client_app_id='WebApiTest', client_version='python-client-test-2-230',
          protocol_version_major=2,protocol_version_minor = 230):
    # create a client_msg based on the protocol.
    client_msg = ClientMsg()
    # initialize the logon message, there are four required parameters.
    logon = client_msg.logon
    logon.user_name = user_name
    logon.password = password
    logon.client_app_id = client_app_id
    logon.client_version = client_version
    logon.protocol_version_major = protocol_version_major
    logon.protocol_version_minor = protocol_version_minor
    # see send_client_message() function in webapi_client.py in line 23.
    client.send_client_message(client_msg)
    # see receive_server_message() function in webapi_client.py in line 33.
    server_msg = client.receive_server_message()
    if server_msg.logon_result.result_code == LogonResult.ResultCode.RESULT_CODE_SUCCESS:
        # in later samples, we will need to use base_time to complete the from_utc_time.
        # in the time_and_sales_request sample and the time_bar_request sample.
        return server_msg.logon_result.base_time
    else:
        # the text_message contains the reason why user cannot login.
        raise Exception("Can't login: " + server_msg.logon_result.text_message)

def logoff(client):
    client_msg = ClientMsg()
    logoff = client_msg.logoff
    logoff.text_message = "logoff test"
    client.send_client_message(client_msg)
    server_msg = client.receive_server_message()
    if server_msg.logged_off:
        print("Logoff :)")
    if server_msg.logged_off.text_message:
        print("Logoff reason is: " + server_msg.logged_off.logoff_reason)

if __name__ == "__main__":
    # see WebApiClient() class in webapi_client.py in line 5.
    client = webapi_client.WebApiClient()
    # see connect() function in webapi_client.py in line 16.
    client.connect(host_name)
    logon(client, user_name, password)
    # see disconnect() function in webapi_client.py in line 19.
    logoff(client)
    client.disconnect()
