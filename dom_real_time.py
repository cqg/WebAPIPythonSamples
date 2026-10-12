"""
DOM (Depth Of Market) is requested with market data subscription level LEVEL_TRADES_BBA_DOM. The first
RealTimeMarketData message after subscription is a snapshot (is_snapshot = True) and contains all current
DOM levels as quotes of TYPE_BID and TYPE_ASK. Next RealTimeMarketData messages are updates (is_snapshot = False):
  - quote with volume > 0 -> new price level or new volume for the existing price level;
  - quote with volume = 0 -> price level is removed from DOM.

NOTE: This script requests a lot of data. Consider to dump logs into file if you want to see whole result.
"""

import time

import WebAPI.webapi_2_pb2 as pb
from logon import logoff, logon
from meta import resolve_symbol
from WebAPI import webapi_client
from WebAPI.market_data_2_pb2 import (
    MarketDataSubscription,
    MarketDataSubscriptionStatus,
    Quote,
)

host_name = "wss://demoapi.cqg.com:443"
user_name = ""
password = ""
symbol_name = "EP"
real_time_data_update_duration_sec = 1

local_dom = {Quote.TYPE_BID: {}, Quote.TYPE_ASK: {}}


def request_real_time(client, contract_id, msg_id, level):
    client_msg = pb.ClientMsg()
    subscription = client_msg.market_data_subscriptions.add()
    subscription.contract_id = contract_id
    subscription.request_id = msg_id
    subscription.level = level
    client.send_client_message(client_msg)


def process_incoming_messages(client, correct_price_scale):
    t_end = time.time() + real_time_data_update_duration_sec
    while time.time() < t_end:
        server_msg = client.receive_server_message()

        # Process confirmation of performed market data subscription
        for status in server_msg.market_data_subscription_statuses:
            if status.status_code != MarketDataSubscriptionStatus.STATUS_CODE_SUCCESS:
                raise Exception("Subscription failed: " + status.text_message)
            if status.level != MarketDataSubscription.LEVEL_TRADES_BBA_DOM:
                raise Exception(f"Subscribed with {status.level} instead of DOM")

        # Process real time market data
        for real_time_market_data in server_msg.real_time_market_data:
            update_dom(real_time_market_data)
            print_dom(correct_price_scale)


def update_dom(real_time_market_data):
    if real_time_market_data.is_snapshot:
        # Snapshot: forget everything we had before
        local_dom[Quote.TYPE_ASK].clear()
        local_dom[Quote.TYPE_BID].clear()

    for quote in real_time_market_data.quotes:
        if quote.type == Quote.TYPE_BID:
            side = local_dom[Quote.TYPE_BID]
        elif quote.type == Quote.TYPE_ASK:
            side = local_dom[Quote.TYPE_ASK]
        else:
            # Trades, best bid/ask, settlements are not part of DOM
            continue

        quote_volume = get_volume(quote)
        if quote_volume == 0:
            # Deletion of the price level
            side.pop(quote.scaled_price, None)
        else:
            # Insertion or update of the price level
            side[quote.scaled_price] = quote_volume


def get_volume(quote):
    # Volume is cqg.Decimal: significand * 10^exponent
    return quote.volume.significand * (10**quote.volume.exponent)


def print_dom(correct_price_scale, depth=5):
    print("Asks:")
    for scaled_price, volume in sorted(local_dom[Quote.TYPE_ASK].items(), reverse=True)[-depth:]:
        print(f"  {scaled_price * correct_price_scale} x {volume}")
    print("Bids:")
    for scaled_price, volume in sorted(local_dom[Quote.TYPE_BID].items(), reverse=True)[:depth]:
        print(f"  {scaled_price * correct_price_scale} x {volume}")
    print("\n")


if __name__ == "__main__":
    client = webapi_client.WebApiClient()
    client.connect(host_name)
    logon(client, user_name, password)

    msg_id = 1
    contract_metadata = resolve_symbol(client, symbol_name, msg_id)
    contract_id = contract_metadata.contract_id
    correct_price_scale = contract_metadata.correct_price_scale

    # Peform market data subscription
    msg_id += 1
    request_real_time(client, contract_id, msg_id, level=MarketDataSubscription.LEVEL_TRADES_BBA_DOM)

    # Keep DOM subscription for real_time_data_update_duration_sec and unsubscribe
    process_incoming_messages(client, correct_price_scale)

    # Drop market data subscription
    msg_id += 1
    request_real_time(client, contract_id, msg_id, level=MarketDataSubscription.LEVEL_NONE)

    # Wait market data unsubscription result while skip market data which is still on the way
    while True:
        server_msg = client.receive_server_message()
        if any(
            status.level == MarketDataSubscription.LEVEL_NONE for status in server_msg.market_data_subscription_statuses
        ):
            break

    logoff(client)
    client.disconnect()
