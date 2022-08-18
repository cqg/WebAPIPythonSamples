# CQG WebAPI Python Samples

If you are just getting started with the CQG Web API, you may find it helpful to study the basic sample code packages below. Here you will find comments regarding special concepts necessary to working efficiently with the interface. Each sample module demonstrates all the necessary steps to accomplishing its basic function; e.g. all modules include the functions for connecting to the server and logging in with user credentials. Please note these samples stop short of recommending best practices for error handling or memory management.

## Introduction
The following samples are included into the package:
| File name | Description |
|-----------|-------------|
|`1logon.py`|Connect to API server and send client message with login credentials|
|`2meta.py`|1logon, and send client message to associate symbol with contract id, and get metadata|
|`3session_info.py`|1logon, and send session info id received from metadata message|
|`4account.py`|1logon, and send client message to receive account information associated with user id|
|`5real_time.py`|1logon, 2meta, and send client message to subscribe to real time market data updates|
|`6bar_time.py`|1logon, 2meta, and send client message to request bar data starting at specific time|
|`7time_and_sales.py`|1logon, 2meta, and send client message to request time and sales data starting at a specific time|
|`8trade_subscription.py`|1logon, 2meta, and send client message to subscribe to orders, position, or collateral updates|
|`9orders.py`|1logon, 2meta, and send client message to place or modify an order|

New requests for algo customers:
| File name | Description |
|-----------|-------------|
|`entitlements.py`|Receive the order entitlement with enabled algo strategies for certain account and contract|
|`algo_strategy.py`|Create algo strategies definitions|
|`algo_orders.py`|Send algo order requests via WebAPI|

## How to use
Please follow the steps introduced below to test the samples:
1. In order to use the samples, a user needs to have [python 3.x](http://www.python.org/) installed
2. In each sample, a user needs to modify the code according to his purpose
3. Open Command Prompt, go to the sample's path, run the command like:
```
	python 1logon.py
	python 4real_time.py
```

## Package content
### \google
Part of Google Protocol Buffers library

### \Webapi
| File name | Description |
|-----------|-------------|
|`account_authorization_2_pb2.py`|Messages for accounts that require separate authorization process|
|`api_limit_2_pb2.py`|WebAPI limit messages|
|`historical_2_pb2.py`|Historical related messages. T&S, TimeBar, NonTimedBar, RenkoBar and so on|
|`instrument_definition_2_pb2.py`|Instrument definition messages|
|`market_data_2_pb2.py`|Market Data messaging. RealTimeMarketData, DetailedDOM, RFQRequest, OptionCalculationRequest|
|`metadata_2_pb2.py`|Public metadata related messages|
|`metadata_admin_2_pb2.py`|Metadata administration messages|
|`order_2_pb2.py`|Order related messages|
|`otc_1_pb2.py`|OTC messages|
|`rules_1_pb2.py`|Rules server messages|
|`strategy_2_pb2.py`|Strategy related messages|
|`strategy_definition_2_pb2.py`|Strategy definition messages|
|`symbol_browsing_2_pb2.py`|Symbol related messages|
|`trade_routing_2_pb2.py`|Trade Routing messaging|
|`trading_account_2_pb2.py`|Trading account related messages|
|`trading_session_2_pb2.py`|Trading session related messages|
|`user_attribute_2_pb2.py`|User attributes messages|
|`user_session_2_pb2.py`|User session level messages|
|`webapi_2_pb2.py`|CQG Web API server protocol|
|`webapi_client.py`|helper class for connection to WebAPI server|
|`websocket.py`|[WebSocket client library](https://pypi.python.org/pypi/websocket-client/)|

### \common
| File name | Description |
|-----------|-------------|
|`decimal_pb2.py`|protocol wrapper for Python, compiled from .proto|
|`shared_1_pb2.py`|Entities shared between different protocols|

### \proto
| File name | Description |
|-----------|-------------|
|[protoc.exe](https://github.com/protocolbuffers/protobuf/releases)|compiler to convert .proto files to `_pb2.py`, version 21.2 last upgrade date: 06/24/2022|
|`generater.cmd`|double click to generate .py files compiled from protocol files|

### \proto\common
| File name | Description |
|-----------|-------------|
|`decimal.proto`|decimal numbers wrapper|
|`shared.proto`|Entities shared between different protocols|

#### \proto\WebAPI
| File name | Description |
|-----------|-------------|
|[protocol files](https://partners.cqg.com/api-resources/web-api/documentation)|readable description of protocol messages in ProtoBuf format, version 2.87 last upgrade date: 05/18/2022|

## Notice
When protocol files update, a user may obtain more information from the server by using the updated protocol:
1. Go to this page and open the [Production Protocol link](http://partners.cqg.com/api-resources/continuum-connect/documentation)
2. Save the protocol files into your proto folder
3. Follow the instruction in ReadMe.txt in proto folder

## Contact
If you have problems, questions, ideas or suggestions, please [contact us](mailto:apihelp@cqg.com)

