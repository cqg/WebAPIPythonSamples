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

# We use contract_id instead of symbol to request_real_time
# LEVEL_NONE = 0                Unsubscribe.
# LEVEL_TRADES = 1              Get trade with volumes and settlement quotes
# LEVEL_TRADES_BBA = 2          Get trades with volumes, settlement and best ask & bid without volumes
# LEVEL_TRADES_BBA_TRADES = 3   Get trades with volumes, settlement and best ask & bid with volumes
# LEVEL_TRADES_BBA_DOM = 4      All price data including DOM.
# LEVEL_SETTLEMENTS = 5         Get only settlement quotes. NOTE: MarketValues will contain only settlements
# LEVEL_MARKET_VALUES = 6       Get only market values. NOTE: Array of quotes in RealTimeMarketData message will be always empty
# LEVEL_TRADES_BBA_DETAILED_DOM = 7  LEVEL_TRADES_BBA_DOM + Order Details

def request_real_time(contract_id=1, level=1):
    client_msg = ClientMsg()
    subscription = client_msg.market_data_subscriptions.add()
    subscription.contract_id = contract_id
    subscription.level = level
    client.send_client_message(client_msg)
    while True: 
        # In the sample we use a larger number "timeout" in webapi_client.py in line 16
        # to receive real time market data continuously, you may stop receiving updates 
        # for illiquid symbols when the timeout is small
        server_msg = client.receive_server_message()

if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    logon(user_name, password)
    contract_metadata = resolve_symbol(symbol_name)

    request_real_time()

    client.disconnect()
