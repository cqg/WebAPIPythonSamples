from WebAPI.webapi_2_pb2 import *
from WebAPI import webapi_client
from logon import *
from meta import *
import time

host_name = 'wss://demoapi.cqg.com:443'
user_name = ''
password = ''
symbol_name = 'ZUC'

# We use contract_id instead of symbol to request_real_time
# LEVEL_NONE = 0                Unsubscribe.
# LEVEL_TRADES = 1              Get trade with volumes and settlement quotes
# LEVEL_TRADES_BBA = 2          Get trades with volumes, settlement and best ask & bid without volumes
# LEVEL_TRADES_BBA_TRADES = 3   Get trades with volumes, settlement and best ask & bid with volumes
# LEVEL_TRADES_BBA_DOM = 4      All price data including DOM.
# LEVEL_SETTLEMENTS = 5         Get only settlement quotes. NOTE: MarketValues will contain only settlements
# LEVEL_MARKET_VALUES = 6       Get only market values. NOTE: Array of quotes in RealTimeMarketData message will be always empty
# LEVEL_TRADES_BBA_DETAILED_DOM = 7  LEVEL_TRADES_BBA_DOM + Order Details

def request_real_time(client, contract_id, msg_id, level):
    client_msg = ClientMsg()
    subscription = client_msg.market_data_subscriptions.add()
    subscription.contract_id = contract_id
    subscription.request_id = msg_id
    subscription.level = level
    client.send_client_message(client_msg)
    while True: 
        server_msg = client.receive_server_message()

if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    logon(client, user_name, password)
    msg_id = 1
    contract_id = resolve_symbol(client, symbol_name, msg_id).contract_id
    msg_id+=1
    request_real_time(client, contract_id, msg_id, 1)
    # This sample doesn't have multiple threads, it subscribe for 5 seconds and unsubscribe
    t_end = time.time() + 5
    while True:
        # ...
        if time.time() > t_end:
                msg_id+=1
                request_real_time(client, contract_id, msg_id, 0)
                break
    
    logoff(client)
    client.disconnect()
