# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: WebAPI/api_limit_2.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'WebAPI/api_limit_2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import shared_1_pb2 as common_dot_shared__1__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18WebAPI/api_limit_2.proto\x12\x0b\x61pi_limit_2\x1a\x15\x63ommon/shared_1.proto\"!\n\x0f\x41piLimitRequest\x12\x0e\n\x06limits\x18\x01 \x03(\r\"{\n\rApiLimitEntry\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x13\n\x0bstatus_code\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\r\x12\x12\n\nperiod_sec\x18\x04 \x01(\r\x12#\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x0e.shared_1.Text\"C\n\x0e\x41piLimitReport\x12\x31\n\rlimit_entries\x18\x01 \x03(\x0b\x32\x1a.api_limit_2.ApiLimitEntry*\x89-\n\x08\x41piLimit\x12\x19\n\x15\x41PI_LIMIT_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x41PI_LIMIT_CONNECTION_RATE\x10\x01\x12$\n API_LIMIT_CONCURRENT_SUBSESSIONS\x10\x02\x12 \n\x1c\x41PI_LIMIT_CONNECTIONS_PER_IP\x10\x03\x12\x37\n3API_LIMIT_SOCKET_UNREADY_PERIOD_TO_CLOSE_CONNECTION\x10\x64\x12\"\n\x1e\x41PI_LIMIT_CLIENT_MESSAGES_RATE\x10n\x12(\n#API_LIMIT_INFORMATION_REQUESTS_RATE\x10\xc8\x01\x12%\n API_LIMIT_ACCOUNTS_REQUESTS_RATE\x10\xd2\x01\x12.\n)API_LIMIT_SYMBOL_RESOLUTION_REQUESTS_RATE\x10\xdc\x01\x12+\n&API_LIMIT_LAST_STATEMENT_BALANCES_RATE\x10\xe6\x01\x12+\n&API_LIMIT_CURRENCY_RATES_REQUESTS_RATE\x10\xf0\x01\x12\x32\n-API_LIMIT_CURRENCY_RATE_SOURCES_REQUESTS_RATE\x10\xf1\x01\x12\x39\n4API_LIMIT_SESSION_INFORMATION_REQUESTS_IN_PROCESSING\x10\xfa\x01\x12\x30\n+API_LIMIT_SESSION_INFORMATION_SUBSCRIPTIONS\x10\xfb\x01\x12\x37\n2API_LIMIT_HISTORICAL_ORDERS_REQUESTS_IN_PROCESSING\x10\x84\x02\x12%\n API_LIMIT_HISTORICAL_ORDERS_DAYS\x10\x85\x02\x12:\n5API_LIMIT_OPTION_MATURITY_LIST_REQUESTS_IN_PROCESSING\x10\x8e\x02\x12\x31\n,API_LIMIT_OPTION_MATURITY_LIST_SUBSCRIPTIONS\x10\x8f\x02\x12\x36\n1API_LIMIT_INSTRUMENT_GROUP_REQUESTS_IN_PROCESSING\x10\x98\x02\x12-\n(API_LIMIT_INSTRUMENT_GROUP_SUBSCRIPTIONS\x10\x99\x02\x12\x39\n4API_LIMIT_AT_THE_MONEY_STRIKE_REQUESTS_IN_PROCESSING\x10\xa2\x02\x12\x30\n+API_LIMIT_AT_THE_MONEY_STRIKE_SUBSCRIPTIONS\x10\xa3\x02\x12\x30\n+API_LIMIT_STRATEGY_DEFINITION_REQUESTS_RATE\x10\xac\x02\x12\x38\n3API_LIMIT_SESSION_TIME_RANGE_REQUESTS_IN_PROCESSING\x10\xb6\x02\x12<\n7API_LIMIT_TRADING_DAY_TIME_RANGE_REQUESTS_IN_PROCESSING\x10\xc0\x02\x12\x37\n2API_LIMIT_ORDER_ENTITLEMENT_REQUESTS_IN_PROCESSING\x10\xca\x02\x12:\n5API_LIMIT_SYMBOL_CATEGORY_LIST_REQUESTS_IN_PROCESSING\x10\xd4\x02\x12\x31\n,API_LIMIT_SYMBOL_CATEGORY_LIST_SUBSCRIPTIONS\x10\xd5\x02\x12\x35\n0API_LIMIT_SYMBOL_CATEGORY_REQUESTS_IN_PROCESSING\x10\xde\x02\x12,\n\'API_LIMIT_SYMBOL_CATEGORY_SUBSCRIPTIONS\x10\xdf\x02\x12\x31\n,API_LIMIT_SYMBOL_LIST_REQUESTS_IN_PROCESSING\x10\xe8\x02\x12(\n#API_LIMIT_SYMBOL_LIST_SUBSCRIPTIONS\x10\xe9\x02\x12#\n\x1e\x41PI_LIMIT_SYMBOL_REQUESTS_RATE\x10\xf2\x02\x12,\n\'API_LIMIT_SYMBOL_REQUESTS_IN_PROCESSING\x10\xf3\x02\x12>\n9API_LIMIT_ALGO_STRATEGY_DEFINITION_REQUESTS_IN_PROCESSING\x10\xfc\x02\x12\x42\n=API_LIMIT_API_LIMITS_SUBSCRIPTIONS_AND_REQUESTS_IN_PROCESSING\x10\x86\x03\x12\x31\n,API_LIMIT_CONTRIBUTOR_METADATA_REQUESTS_RATE\x10\x90\x03\x12:\n5API_LIMIT_CONTRIBUTOR_METADATA_REQUESTS_IN_PROCESSING\x10\x91\x03\x12\x31\n,API_LIMIT_CONTRIBUTOR_METADATA_SUBSCRIPTIONS\x10\x92\x03\x12K\nFAPI_LIMIT_BROKERAGE_TRADING_FEATURE_ENTITLEMENT_REQUESTS_IN_PROCESSING\x10\x9a\x03\x12)\n$API_LIMIT_ORDER_STATUS_REQUESTS_RATE\x10\xa4\x03\x12+\n&API_LIMIT_PRODUCT_SEARCH_REQUESTS_RATE\x10\xae\x03\x12\x34\n/API_LIMIT_PRODUCT_SEARCH_REQUESTS_IN_PROCESSING\x10\xaf\x03\x12\x44\n?API_LIMIT_SYMBOL_CATEGORY_LIST_BY_INSTRUMENT_TYPE_REQUESTS_RATE\x10\xb8\x03\x12M\nHAPI_LIMIT_SYMBOL_CATEGORY_LIST_BY_INSTRUMENT_TYPE_REQUESTS_IN_PROCESSING\x10\xb9\x03\x12\x32\n-API_LIMIT_MARKET_STATE_METADATA_REQUESTS_RATE\x10\xc2\x03\x12;\n6API_LIMIT_MARKET_STATE_METADATA_REQUESTS_IN_PROCESSING\x10\xc3\x03\x12\x32\n-API_LIMIT_MARKET_STATE_METADATA_SUBSCRIPTIONS\x10\xc4\x03\x12\x32\n-API_LIMIT_INSTRUMENT_DEFINITION_REQUESTS_RATE\x10\xcc\x03\x12\x37\n2API_LIMIT_EXCHANGE_METADATA_REQUESTS_IN_PROCESSING\x10\xd6\x03\x12.\n)API_LIMIT_EXCHANGE_METADATA_SUBSCRIPTIONS\x10\xd7\x03\x12\x31\n,API_LIMIT_ENTITLEMENT_REQUESTS_SUBSCRIPTIONS\x10\xe0\x03\x12;\n6API_LIMIT_INSTRUMENT_GROUP_BY_SECURITIES_REQUESTS_RATE\x10\xea\x03\x12\x44\n?API_LIMIT_INSTRUMENT_GROUP_BY_SECURITIES_REQUESTS_IN_PROCESSING\x10\xeb\x03\x12;\n6API_LIMIT_INSTRUMENT_GROUP_BY_SECURITIES_SUBSCRIPTIONS\x10\xec\x03\x12\x39\n4API_LIMIT_INSTRUMENT_GROUP_BY_EXCHANGE_REQUESTS_RATE\x10\xf4\x03\x12\x42\n=API_LIMIT_INSTRUMENT_GROUP_BY_EXCHANGE_REQUESTS_IN_PROCESSING\x10\xf5\x03\x12\x39\n4API_LIMIT_INSTRUMENT_GROUP_BY_EXCHANGE_SUBSCRIPTIONS\x10\xf6\x03\x12\x30\n+API_LIMIT_EXCHANGE_SECURITIES_REQUESTS_RATE\x10\xfe\x03\x12\x39\n4API_LIMIT_EXCHANGE_SECURITIES_REQUESTS_IN_PROCESSING\x10\xff\x03\x12\x30\n+API_LIMIT_EXCHANGE_SECURITIES_SUBSCRIPTIONS\x10\x80\x04\x12)\n$API_LIMIT_COUNTRY_LIST_REQUESTS_RATE\x10\x88\x04\x12\x32\n-API_LIMIT_COUNTRY_LIST_REQUESTS_IN_PROCESSING\x10\x89\x04\x12)\n$API_LIMIT_COUNTRY_LIST_SUBSCRIPTIONS\x10\x8a\x04\x12\x30\n+API_LIMIT_CALENDAR_EVENT_LIST_REQUESTS_RATE\x10\x92\x04\x12\x39\n4API_LIMIT_CALENDAR_EVENT_LIST_REQUESTS_IN_PROCESSING\x10\x93\x04\x12\x30\n+API_LIMIT_CALENDAR_EVENT_LIST_SUBSCRIPTIONS\x10\x94\x04\x12\x39\n4API_LIMIT_CALENDAR_EVENT_PROVIDER_LIST_REQUESTS_RATE\x10\x9c\x04\x12\x42\n=API_LIMIT_CALENDAR_EVENT_PROVIDER_LIST_REQUESTS_IN_PROCESSING\x10\x9d\x04\x12\x39\n4API_LIMIT_CALENDAR_EVENT_PROVIDER_LIST_SUBSCRIPTIONS\x10\x9e\x04\x12\x35\n0API_LIMIT_CALENDAR_EVENT_TYPE_LIST_REQUESTS_RATE\x10\xa6\x04\x12>\n9API_LIMIT_CALENDAR_EVENT_TYPE_LIST_REQUESTS_IN_PROCESSING\x10\xa7\x04\x12\x35\n0API_LIMIT_CALENDAR_EVENT_TYPE_LIST_SUBSCRIPTIONS\x10\xa8\x04\x12%\n API_LIMIT_TRADE_ROUTING_ACCOUNTS\x10\xd8\x04\x12\"\n\x1d\x41PI_LIMIT_TRADE_SUBSCRIPTIONS\x10\xe2\x04\x12+\n&API_LIMIT_TRADE_SUBSCRIPTIONS_ACCOUNTS\x10\xe3\x04\x12\"\n\x1d\x41PI_LIMIT_ORDER_REQUESTS_RATE\x10\xbc\x05\x12*\n%API_LIMIT_ORDER_REQUESTS_ACCOUNT_RATE\x10\xbd\x05\x12,\n\'API_LIMIT_MARKET_DATA_SUBSCRIPTION_RATE\x10\xa0\x06\x12(\n#API_LIMIT_MARKET_DATA_SUBSCRIPTIONS\x10\xa1\x06\x12\x34\n/API_LIMIT_MARKET_DATA_DELAY_TO_CLOSE_CONNECTION\x10\xaa\x06\x12\x30\n+API_LIMIT_HISTORICAL_REQUESTS_IN_PROCESSING\x10\xe8\x07\x12\'\n\"API_LIMIT_HISTORICAL_SUBSCRIPTIONS\x10\xe9\x07\x12+\n&API_LIMIT_TIME_AND_SALES_REQUESTS_RATE\x10\xf2\x07\x12%\n API_LIMIT_TIME_BAR_REQUESTS_RATE\x10\xfc\x07\x12>\n9API_LIMIT_VOLUME_PROFILE_REQUESTS_CONTRACT_AND_RANGE_RATE\x10\x86\x08\x12*\n%API_LIMIT_NON_TIMED_BAR_REQUESTS_RATE\x10\x90\x08\x12!\n\x1c\x41PI_LIMIT_RULE_REQUESTS_RATE\x10\xb1\t\x12\x18\n\x13\x41PI_LIMIT_RESERVED1\x10\x94\n\x12?\n:API_LIMIT_PUBLISH_UNPUBLISH_PREVIEW_CONTRACT_REQUESTS_RATE\x10\x95\n\x12\x41\n<API_LIMIT_PUBLISH_UNPUBLISH_PUBLISHED_CONTRACT_REQUESTS_RATE\x10\x96\n\x12\x34\n/API_LIMIT_GET_SECURITY_PARAMETERS_REQUESTS_RATE\x10\x97\n\x12\x34\n/API_LIMIT_SET_SECURITY_PARAMETERS_REQUESTS_RATE\x10\x98\n\x12\x34\n/API_LIMIT_GET_CONTRACT_PARAMETERS_REQUESTS_RATE\x10\x99\n\x12*\n%API_LIMIT_OTC_INSTANCES_SUBSCRIPTIONS\x10\xf8\n\x12(\n#API_LIMIT_HEDGE_BOOKS_SUBSCRIPTIONS\x10\x82\x0b\x12/\n*API_LIMIT_HEDGE_BOOK_DETAILS_REQUESTS_RATE\x10\x8c\x0b\x12\x38\n3API_LIMIT_HEDGE_BOOK_DETAILS_REQUESTS_IN_PROCESSING\x10\x8d\x0b\x12/\n*API_LIMIT_HEDGE_BOOK_DETAILS_SUBSCRIPTIONS\x10\x8e\x0b\x12\x31\n,API_LIMIT_OFFSET_HEDGE_BALANCE_REQUESTS_RATE\x10\x96\x0b\x12-\n(API_LIMIT_CHANGE_OTC_STATE_REQUESTS_RATE\x10\xa0\x0b\x12,\n\'API_LIMIT_FILL_CASH_ORDER_REQUESTS_RATE\x10\xaa\x0b\x12\x30\n+API_LIMIT_BALANCE_ITEMS_LINKS_REQUESTS_RATE\x10\xb4\x0b\x12:\n5API_LIMIT_ARCHIVE_HEDGE_BALANCE_DETAILS_REQUESTS_RATE\x10\xbe\x0b\x12:\n5API_LIMIT_TAIL_MANAGEMENT_CONFIGURATION_SUBSCRIPTIONS\x10\xc8\x0b\x12\x41\n<API_LIMIT_UPDATE_TAIL_MANAGEMENT_CONFIGURATION_REQUESTS_RATE\x10\xd2\x0b\x12\x43\n>API_LIMIT_TAIL_MANAGEMENT_CONFIGURATION_METADATA_REQUESTS_RATE\x10\x90N\x12\x18\n\x13\x41PI_LIMIT_RESERVED2\x10\x9aN\x12(\n#API_LIMIT_RFQ_REQUESTS_ACCOUNT_RATE\x10\xdc\x0b\x12/\n*API_LIMIT_OPTION_CALCULATION_REQUESTS_RATE\x10\xc0\x0c\x12/\n*API_LIMIT_OPTION_CALCULATION_SUBSCRIPTIONS\x10\xc1\x0c\x12-\n(API_LIMIT_RFQ_SUBSCRIPTION_REQUESTS_RATE\x10\xa4\r\"\x06\x08\xb0\t\x10\xb0\t*\xc3\x01\n\x17\x41piLimitEntryStatusCode\x12+\n\'API_LIMIT_ENTRY_STATUS_CODE_UNSPECIFIED\x10\x00\x12\'\n#API_LIMIT_ENTRY_STATUS_CODE_SUCCESS\x10\x01\x12\'\n#API_LIMIT_ENTRY_STATUS_CODE_FAILURE\x10\x65\x12)\n%API_LIMIT_ENTRY_STATUS_CODE_NOT_FOUND\x10h')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WebAPI.api_limit_2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_APILIMIT']._serialized_start=294
  _globals['_APILIMIT']._serialized_end=6063
  _globals['_APILIMITENTRYSTATUSCODE']._serialized_start=6066
  _globals['_APILIMITENTRYSTATUSCODE']._serialized_end=6261
  _globals['_APILIMITREQUEST']._serialized_start=64
  _globals['_APILIMITREQUEST']._serialized_end=97
  _globals['_APILIMITENTRY']._serialized_start=99
  _globals['_APILIMITENTRY']._serialized_end=222
  _globals['_APILIMITREPORT']._serialized_start=224
  _globals['_APILIMITREPORT']._serialized_end=291
# @@protoc_insertion_point(module_scope)
