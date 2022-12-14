# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WebAPI/trading_account_2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eWebAPI/trading_account_2.proto\x12\x11trading_account_2\x1a\x1fgoogle/protobuf/timestamp.proto\"\x11\n\x0f\x41\x63\x63ountsRequest\"B\n\x0e\x41\x63\x63ountsReport\x12\x30\n\nbrokerages\x18\x01 \x03(\x0b\x32\x1c.trading_account_2.Brokerage\"\xc7\x01\n\tBrokerage\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\x34\n\x0csales_series\x18\x03 \x03(\x0b\x32\x1e.trading_account_2.SalesSeries\"\\\n\rBrokerageType\x12\x1a\n\x16\x42ROKERAGE_TYPE_REGULAR\x10\x01\x12\x16\n\x12\x42ROKERAGE_TYPE_SIM\x10\x02\x12\x17\n\x13\x42ROKERAGE_TYPE_DEMO\x10\x03\"Y\n\x0bSalesSeries\x12\x0e\n\x06number\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12,\n\x08\x61\x63\x63ounts\x18\x03 \x03(\x0b\x32\x1a.trading_account_2.Account\"\xc0\x04\n\x07\x41\x63\x63ount\x12\x12\n\naccount_id\x18\x01 \x02(\x11\x12\x1c\n\x14\x62rokerage_account_id\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x1b\n\x13last_statement_date\x18\x04 \x02(\x12\x12\x14\n\x0cis_view_only\x18\x05 \x01(\x08\x12\x17\n\x0fis_unauthorized\x18\x06 \x01(\x08\x12\x11\n\treserved1\x18\x07 \x01(\x12\x12!\n\x19\x61\x63\x63ount_connection_status\x18\x08 \x01(\r\x12K\n\'account_connection_status_utc_timestamp\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0f\x63ontributor_ids\x18\n \x03(\t\x12*\n\"pre_trade_mid_market_mark_required\x18\x0b \x01(\x08\x12\x1f\n\x17\x61llow_external_accounts\x18\x0c \x01(\x08\"\xbf\x01\n\x17\x41\x63\x63ountConnectionStatus\x12%\n!ACCOUNT_CONNECTION_STATUS_OFFLINE\x10\x01\x12*\n&ACCOUNT_CONNECTION_STATUS_DISCONNECTED\x10\x02\x12(\n$ACCOUNT_CONNECTION_STATUS_CONNECTING\x10\x03\x12\'\n#ACCOUNT_CONNECTION_STATUS_CONNECTED\x10\x04\"\x1e\n\x1cLastStatementBalancesRequest\"K\n\x1bLastStatementBalancesReport\x12,\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x1a.trading_account_2.Balance\"\xf2\x01\n\x07\x42\x61lance\x12\n\n\x02id\x18\x01 \x02(\x11\x12\x12\n\naccount_id\x18\x02 \x02(\x11\x12\x16\n\x0estatement_date\x18\x03 \x02(\x12\x12\x10\n\x08\x63urrency\x18\x04 \x02(\t\x12\x0f\n\x07\x62\x61lance\x18\x05 \x02(\x01\x12\x13\n\x0btotal_value\x18\x06 \x02(\x01\x12\x0b\n\x03ote\x18\x07 \x02(\x01\x12\x0b\n\x03upl\x18\x08 \x02(\x01\x12\x0b\n\x03mvo\x18\t \x02(\x01\x12\x13\n\x0b\x63\x61sh_excess\x18\n \x02(\x01\x12\x12\n\ncollateral\x18\x0b \x02(\x01\x12\x16\n\x0einitial_margin\x18\x0c \x02(\x01\x12\x0f\n\x07\x64\x65leted\x18\r \x01(\x08\"\x16\n\x14\x43urrencyRatesRequest\"b\n\x13\x43urrencyRatesReport\x12K\n\x18\x62rokerage_currency_rates\x18\x01 \x03(\x0b\x32).trading_account_2.BrokerageCurrencyRates\"\x98\x01\n\x16\x42rokerageCurrencyRates\x12\x14\n\x0c\x62rokerage_id\x18\x01 \x02(\r\x12\x17\n\x0fmaster_currency\x18\x02 \x02(\t\x12\x16\n\x0estatement_date\x18\x03 \x02(\x12\x12\x37\n\x0e\x63urrency_rates\x18\x04 \x03(\x0b\x32\x1f.trading_account_2.CurrencyRate\"F\n\x0c\x43urrencyRate\x12\x10\n\x08\x63urrency\x18\x02 \x02(\t\x12\x0c\n\x04rate\x18\x03 \x02(\x01\x12\x16\n\x0e\x64\x65\x63imal_places\x18\x04 \x01(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WebAPI.trading_account_2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACCOUNTSREQUEST._serialized_start=86
  _ACCOUNTSREQUEST._serialized_end=103
  _ACCOUNTSREPORT._serialized_start=105
  _ACCOUNTSREPORT._serialized_end=171
  _BROKERAGE._serialized_start=174
  _BROKERAGE._serialized_end=373
  _BROKERAGE_BROKERAGETYPE._serialized_start=281
  _BROKERAGE_BROKERAGETYPE._serialized_end=373
  _SALESSERIES._serialized_start=375
  _SALESSERIES._serialized_end=464
  _ACCOUNT._serialized_start=467
  _ACCOUNT._serialized_end=1043
  _ACCOUNT_ACCOUNTCONNECTIONSTATUS._serialized_start=852
  _ACCOUNT_ACCOUNTCONNECTIONSTATUS._serialized_end=1043
  _LASTSTATEMENTBALANCESREQUEST._serialized_start=1045
  _LASTSTATEMENTBALANCESREQUEST._serialized_end=1075
  _LASTSTATEMENTBALANCESREPORT._serialized_start=1077
  _LASTSTATEMENTBALANCESREPORT._serialized_end=1152
  _BALANCE._serialized_start=1155
  _BALANCE._serialized_end=1397
  _CURRENCYRATESREQUEST._serialized_start=1399
  _CURRENCYRATESREQUEST._serialized_end=1421
  _CURRENCYRATESREPORT._serialized_start=1423
  _CURRENCYRATESREPORT._serialized_end=1521
  _BROKERAGECURRENCYRATES._serialized_start=1524
  _BROKERAGECURRENCYRATES._serialized_end=1676
  _CURRENCYRATE._serialized_start=1678
  _CURRENCYRATE._serialized_end=1748
# @@protoc_insertion_point(module_scope)
