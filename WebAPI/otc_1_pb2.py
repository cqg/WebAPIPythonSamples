# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WebAPI/otc_1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import shared_1_pb2 as common_dot_shared__1__pb2
from common import decimal_pb2 as common_dot_decimal__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12WebAPI/otc_1.proto\x12\x05otc_1\x1a\x15\x63ommon/shared_1.proto\x1a\x14\x63ommon/decimal.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd9\x04\n\nOtcRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x43\n\x1aotc_instances_subscription\x18\x02 \x01(\x0b\x32\x1f.otc_1.OtcInstancesSubscription\x12?\n\x18hedge_books_subscription\x18\x03 \x01(\x0b\x32\x1d.otc_1.HedgeBooksSubscription\x12L\n\x1fhedge_book_details_subscription\x18\x04 \x01(\x0b\x32#.otc_1.HedgeBookDetailsSubscription\x12\x46\n\x1coffset_hedge_balance_request\x18\x05 \x01(\x0b\x32 .otc_1.OffsetHedgeBalanceRequest\x12>\n\x18\x63hange_otc_state_request\x18\x06 \x01(\x0b\x32\x1c.otc_1.ChangeOtcStateRequest\x12<\n\x17\x66ill_cash_order_request\x18\x07 \x01(\x0b\x32\x1b.otc_1.FillCashOrderRequest\x12W\n%archive_hedge_balance_details_request\x18\x08 \x01(\x0b\x32(.otc_1.ArchiveHedgeBalanceDetailsRequest\x12\x44\n\x1b\x62\x61lance_items_links_request\x18\t \x01(\x0b\x32\x1f.otc_1.BalanceItemsLinksRequest\"\xe0\x07\n\tOtcReport\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\r\x12\x1f\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.shared_1.Text\x12\x37\n\x14otc_instances_report\x18\x04 \x01(\x0b\x32\x19.otc_1.OtcInstancesReport\x12\x33\n\x12hedge_books_report\x18\x05 \x01(\x0b\x32\x17.otc_1.HedgeBooksReport\x12@\n\x19hedge_book_details_report\x18\x06 \x01(\x0b\x32\x1d.otc_1.HedgeBookDetailsReport\x12\x44\n\x1boffset_hedge_balance_result\x18\x07 \x01(\x0b\x32\x1f.otc_1.OffsetHedgeBalanceResult\x12<\n\x17\x63hange_otc_state_result\x18\x08 \x01(\x0b\x32\x1b.otc_1.ChangeOtcStateResult\x12:\n\x16\x66ill_cash_order_result\x18\t \x01(\x0b\x32\x1a.otc_1.FillCashOrderResult\x12U\n$archive_hedge_balance_details_result\x18\n \x01(\x0b\x32\'.otc_1.ArchiveHedgeBalanceDetailsResult\x12\x42\n\x1a\x62\x61lance_items_links_result\x18\x0b \x01(\x0b\x32\x1e.otc_1.BalanceItemsLinksResult\"\xfd\x02\n\nStatusCode\x12\x17\n\x13STATUS_CODE_SUCCESS\x10\x00\x12\x1a\n\x16STATUS_CODE_SUBSCRIBED\x10\x01\x12\x17\n\x13STATUS_CODE_DROPPED\x10\x02\x12\x16\n\x12STATUS_CODE_UPDATE\x10\x03\x12\x1c\n\x18STATUS_CODE_DISCONNECTED\x10\x04\x12\x17\n\x13STATUS_CODE_FAILURE\x10\x65\x12\x1e\n\x1aSTATUS_CODE_INVALID_PARAMS\x10\x66\x12\x1d\n\x19STATUS_CODE_ACCESS_DENIED\x10g\x12,\n(STATUS_CODE_SUBSCRIPTION_LIMIT_VIOLATION\x10h\x12\x31\n-STATUS_CODE_SUBSCRIPTION_RATE_LIMIT_VIOLATION\x10i\x12\x19\n\x15STATUS_CODE_NOT_FOUND\x10j\x12\x17\n\x13STATUS_CODE_TIMEOUT\x10k\"A\n\x0fHedgeBalanceKey\x12\x12\n\naccount_id\x18\x01 \x01(\x11\x12\x13\n\x0b\x63ontract_id\x18\x02 \x01(\r*\x05\x08\x64\x10\xc8\x01\"3\n\x18OtcInstancesSubscription\x12\x17\n\tsubscribe\x18\x01 \x01(\x08:\x04true\"J\n\x12OtcInstancesReport\x12\x34\n\x13otc_instance_states\x18\x01 \x03(\x0b\x32\x17.otc_1.OtcInstanceState\"D\n\x10OtcInstanceState\x12\x13\n\x0binstance_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\r\"J\n\x16HedgeBooksSubscription\x12\x17\n\tsubscribe\x18\x01 \x01(\x08:\x04true\x12\x17\n\x0fotc_instance_id\x18\x02 \x01(\r\"\xc4\x01\n\x10HedgeBooksReport\x12\x13\n\x0bis_snapshot\x18\x01 \x01(\x08\x12\x14\n\x0cis_last_part\x18\x02 \x01(\x08\x12\x39\n\x15hedge_balance_details\x18\x03 \x03(\x0b\x32\x1a.otc_1.HedgeBalanceDetails\x12J\n\x1e\x61rchived_hedge_balance_details\x18\x04 \x03(\x0b\x32\".otc_1.ArchivedHedgeBalanceDetails\"\xe2\x01\n\x13HedgeBalanceDetails\x12\x31\n\x11hedge_balance_key\x18\x01 \x01(\x0b\x32\x16.otc_1.HedgeBalanceKey\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\x12#\n\rhedge_balance\x18\x03 \x01(\x0b\x32\x0c.cqg.Decimal\x12%\n\x0fpending_balance\x18\x04 \x01(\x0b\x32\x0c.cqg.Decimal\x12\x17\n\x0f\x63ontract_symbol\x18\x05 \x01(\t\x12\"\n\nunits_name\x18\x06 \x01(\x0b\x32\x0e.shared_1.Text\"\xcf\x01\n\x1cHedgeBookDetailsSubscription\x12\x17\n\tsubscribe\x18\x01 \x01(\x08:\x04true\x12\x17\n\x0fotc_instance_id\x18\x02 \x01(\r\x12\x31\n\x11hedge_balance_key\x18\x03 \x01(\x0b\x32\x16.otc_1.HedgeBalanceKey\x12\x36\n\x12\x66rom_utc_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\narchive_id\x18\x05 \x01(\t\"\xd6\x02\n\x16HedgeBookDetailsReport\x12\x13\n\x0bis_snapshot\x18\x01 \x01(\x08\x12\x14\n\x0cis_last_part\x18\x02 \x01(\x08\x12\x37\n\x12\x63\x61sh_order_details\x18\x03 \x03(\x0b\x32\x17.otc_1.CashOrderDetailsB\x02\x18\x01\x12\x39\n\x13hedge_order_details\x18\x04 \x03(\x0b\x32\x18.otc_1.HedgeOrderDetailsB\x02\x18\x01\x12\x44\n\x1a\x63\x61sh_to_hedge_orders_links\x18\x05 \x03(\x0b\x32\x1c.otc_1.CashToHedgeOrdersLinkB\x02\x18\x01\x12)\n\rbalance_items\x18\x06 \x03(\x0b\x32\x12.otc_1.BalanceItem\x12,\n\x0bitems_links\x18\x07 \x03(\x0b\x32\x17.otc_1.BalanceItemsLink\"\xe5\x01\n\x10\x43\x61shOrderDetails\x12\x16\n\x0e\x63hain_order_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\x12\x12\n\naccount_id\x18\x03 \x01(\x11\x12\x13\n\x0b\x63ontract_id\x18\x04 \x01(\r\x12\x37\n\x13hedge_utc_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x05units\x18\x06 \x01(\x0b\x32\x0c.cqg.Decimal\x12\"\n\nunits_name\x18\x07 \x01(\x0b\x32\x0e.shared_1.Text*\x05\x08\x64\x10\xc8\x01\"\xd8\x01\n\x11HedgeOrderDetails\x12\x16\n\x0e\x63hain_order_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\x12\x37\n\x13hedge_utc_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x05units\x18\x04 \x01(\x0b\x32\x0c.cqg.Decimal\x12 \n\nopen_units\x18\x05 \x01(\x0b\x32\x0c.cqg.Decimal\x12\"\n\nunits_name\x18\x06 \x01(\x0b\x32\x0e.shared_1.Text\"\xd5\x01\n\x15\x43\x61shToHedgeOrdersLink\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\x12\x36\n\x12link_utc_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rcash_order_id\x18\x03 \x01(\t\x12\x16\n\x0ehedge_order_id\x18\x04 \x01(\t\x12 \n\nlink_units\x18\x05 \x01(\x0b\x32\x0c.cqg.Decimal\x12\"\n\nunits_name\x18\x06 \x01(\x0b\x32\x0e.shared_1.Text\"u\n\x0e\x42\x61lanceItemKey\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x11\n\titem_type\x18\x02 \x01(\r\"?\n\x08ItemType\x12\x0e\n\nCASH_ORDER\x10\x01\x12\x0f\n\x0bHEDGE_ORDER\x10\x02\x12\x12\n\x0e\x42\x41LANCE_OFFSET\x10\x03\"\x9c\x02\n\x0b\x42\x61lanceItem\x12\'\n\x08item_key\x18\x01 \x01(\x0b\x32\x15.otc_1.BalanceItemKey\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\x12\x31\n\rutc_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x05units\x18\x04 \x01(\x0b\x32\x0c.cqg.Decimal\x12 \n\nopen_units\x18\x05 \x01(\x0b\x32\x0c.cqg.Decimal\x12\"\n\nunits_name\x18\x06 \x01(\x0b\x32\x0e.shared_1.Text\x12\x10\n\x08username\x18\x07 \x01(\t\x12\x0f\n\x07\x63omment\x18\x08 \x01(\t\x12\x13\n\x0b\x63ontract_id\x18\t \x01(\r*\x05\x08\x64\x10\xc8\x01\"\xf0\x02\n\x10\x42\x61lanceItemsLink\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\x12\x36\n\x12link_utc_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x0e\x66irst_item_key\x18\x03 \x01(\x0b\x32\x15.otc_1.BalanceItemKey\x12.\n\x0fsecond_item_key\x18\x04 \x01(\x0b\x32\x15.otc_1.BalanceItemKey\x12.\n\x18size_in_first_item_units\x18\x05 \x01(\x0b\x32\x0c.cqg.Decimal\x12(\n\x10\x66irst_item_units\x18\x06 \x01(\x0b\x32\x0e.shared_1.Text\x12/\n\x19size_in_second_item_units\x18\x07 \x01(\x0b\x32\x0c.cqg.Decimal\x12)\n\x11second_item_units\x18\x08 \x01(\x0b\x32\x0e.shared_1.Text\"\xcc\x01\n\x19OffsetHedgeBalanceRequest\x12\x17\n\x0fotc_instance_id\x18\x01 \x01(\r\x12\x31\n\x11hedge_balance_key\x18\x02 \x01(\x0b\x32\x16.otc_1.HedgeBalanceKey\x12*\n\x14hedge_balance_offset\x18\x03 \x01(\x0b\x32\x0c.cqg.Decimal\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x0f\n\x07\x63omment\x18\x05 \x01(\t\x12\x14\n\x0czero_balance\x18\x06 \x01(\x08\"\x1a\n\x18OffsetHedgeBalanceResult\"s\n\x15\x43hangeOtcStateRequest\x12\x17\n\x0fotc_instance_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\r\"1\n\x06\x41\x63tion\x12\x13\n\x0f\x41\x43TION_ACTIVATE\x10\x00\x12\x12\n\x0e\x41\x43TION_SUSPEND\x10\x01\"\x16\n\x14\x43hangeOtcStateResult\"\xc5\x01\n\x14\x46illCashOrderRequest\x12\x17\n\x0fotc_instance_id\x18\x01 \x01(\r\x12\x16\n\x0e\x63hain_order_id\x18\x02 \x01(\t\x12\x12\n\naccount_id\x18\x03 \x01(\x11\x12\x13\n\x0b\x63ontract_id\x18\x04 \x01(\r\x12\x19\n\x03qty\x18\x05 \x01(\x0b\x32\x0c.cqg.Decimal\x12\x19\n\x11scaled_fill_price\x18\x06 \x01(\x12\x12\x16\n\x0e\x63ontributor_id\x18\x07 \x01(\t*\x05\x08\x64\x10\xc8\x01\"\x15\n\x13\x46illCashOrderResult\"o\n!ArchiveHedgeBalanceDetailsRequest\x12\x31\n\x11hedge_balance_key\x18\x01 \x01(\x0b\x32\x16.otc_1.HedgeBalanceKey\x12\x17\n\x0fotc_instance_id\x18\x02 \x01(\r\"\"\n ArchiveHedgeBalanceDetailsResult\"\xb8\x01\n\x1b\x41rchivedHedgeBalanceDetails\x12\x0f\n\x07\x64\x65leted\x18\x01 \x01(\x08\x12\x12\n\narchive_id\x18\x02 \x01(\t\x12\x39\n\x15hedge_balance_details\x18\x03 \x01(\x0b\x32\x1a.otc_1.HedgeBalanceDetails\x12\x39\n\x15\x61rchive_utc_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"t\n\x18\x42\x61lanceItemsLinksRequest\x12\x17\n\x0fotc_instance_id\x18\x01 \x01(\r\x12\x0f\n\x07item_id\x18\x02 \x01(\t\x12\x12\n\naccount_id\x18\x03 \x01(\x11\x12\x13\n\x0b\x63ontract_id\x18\x04 \x01(\r*\x05\x08\x64\x10\xc8\x01\"r\n\x17\x42\x61lanceItemsLinksResult\x12)\n\rbalance_items\x18\x01 \x03(\x0b\x32\x12.otc_1.BalanceItem\x12,\n\x0bitems_links\x18\x02 \x03(\x0b\x32\x17.otc_1.BalanceItemsLink*d\n\rInstanceState\x12\x19\n\x15INSTANCE_STATE_ONLINE\x10\x00\x12\x1a\n\x16INSTANCE_STATE_OFFLINE\x10\x01\x12\x1c\n\x18INSTANCE_STATE_SUSPENDED\x10\x02')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WebAPI.otc_1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEDGEBOOKDETAILSREPORT.fields_by_name['cash_order_details']._options = None
  _HEDGEBOOKDETAILSREPORT.fields_by_name['cash_order_details']._serialized_options = b'\030\001'
  _HEDGEBOOKDETAILSREPORT.fields_by_name['hedge_order_details']._options = None
  _HEDGEBOOKDETAILSREPORT.fields_by_name['hedge_order_details']._serialized_options = b'\030\001'
  _HEDGEBOOKDETAILSREPORT.fields_by_name['cash_to_hedge_orders_links']._options = None
  _HEDGEBOOKDETAILSREPORT.fields_by_name['cash_to_hedge_orders_links']._serialized_options = b'\030\001'
  _INSTANCESTATE._serialized_start=5644
  _INSTANCESTATE._serialized_end=5744
  _OTCREQUEST._serialized_start=108
  _OTCREQUEST._serialized_end=709
  _OTCREPORT._serialized_start=712
  _OTCREPORT._serialized_end=1704
  _OTCREPORT_STATUSCODE._serialized_start=1323
  _OTCREPORT_STATUSCODE._serialized_end=1704
  _HEDGEBALANCEKEY._serialized_start=1706
  _HEDGEBALANCEKEY._serialized_end=1771
  _OTCINSTANCESSUBSCRIPTION._serialized_start=1773
  _OTCINSTANCESSUBSCRIPTION._serialized_end=1824
  _OTCINSTANCESREPORT._serialized_start=1826
  _OTCINSTANCESREPORT._serialized_end=1900
  _OTCINSTANCESTATE._serialized_start=1902
  _OTCINSTANCESTATE._serialized_end=1970
  _HEDGEBOOKSSUBSCRIPTION._serialized_start=1972
  _HEDGEBOOKSSUBSCRIPTION._serialized_end=2046
  _HEDGEBOOKSREPORT._serialized_start=2049
  _HEDGEBOOKSREPORT._serialized_end=2245
  _HEDGEBALANCEDETAILS._serialized_start=2248
  _HEDGEBALANCEDETAILS._serialized_end=2474
  _HEDGEBOOKDETAILSSUBSCRIPTION._serialized_start=2477
  _HEDGEBOOKDETAILSSUBSCRIPTION._serialized_end=2684
  _HEDGEBOOKDETAILSREPORT._serialized_start=2687
  _HEDGEBOOKDETAILSREPORT._serialized_end=3029
  _CASHORDERDETAILS._serialized_start=3032
  _CASHORDERDETAILS._serialized_end=3261
  _HEDGEORDERDETAILS._serialized_start=3264
  _HEDGEORDERDETAILS._serialized_end=3480
  _CASHTOHEDGEORDERSLINK._serialized_start=3483
  _CASHTOHEDGEORDERSLINK._serialized_end=3696
  _BALANCEITEMKEY._serialized_start=3698
  _BALANCEITEMKEY._serialized_end=3815
  _BALANCEITEMKEY_ITEMTYPE._serialized_start=3752
  _BALANCEITEMKEY_ITEMTYPE._serialized_end=3815
  _BALANCEITEM._serialized_start=3818
  _BALANCEITEM._serialized_end=4102
  _BALANCEITEMSLINK._serialized_start=4105
  _BALANCEITEMSLINK._serialized_end=4473
  _OFFSETHEDGEBALANCEREQUEST._serialized_start=4476
  _OFFSETHEDGEBALANCEREQUEST._serialized_end=4680
  _OFFSETHEDGEBALANCERESULT._serialized_start=4682
  _OFFSETHEDGEBALANCERESULT._serialized_end=4708
  _CHANGEOTCSTATEREQUEST._serialized_start=4710
  _CHANGEOTCSTATEREQUEST._serialized_end=4825
  _CHANGEOTCSTATEREQUEST_ACTION._serialized_start=4776
  _CHANGEOTCSTATEREQUEST_ACTION._serialized_end=4825
  _CHANGEOTCSTATERESULT._serialized_start=4827
  _CHANGEOTCSTATERESULT._serialized_end=4849
  _FILLCASHORDERREQUEST._serialized_start=4852
  _FILLCASHORDERREQUEST._serialized_end=5049
  _FILLCASHORDERRESULT._serialized_start=5051
  _FILLCASHORDERRESULT._serialized_end=5072
  _ARCHIVEHEDGEBALANCEDETAILSREQUEST._serialized_start=5074
  _ARCHIVEHEDGEBALANCEDETAILSREQUEST._serialized_end=5185
  _ARCHIVEHEDGEBALANCEDETAILSRESULT._serialized_start=5187
  _ARCHIVEHEDGEBALANCEDETAILSRESULT._serialized_end=5221
  _ARCHIVEDHEDGEBALANCEDETAILS._serialized_start=5224
  _ARCHIVEDHEDGEBALANCEDETAILS._serialized_end=5408
  _BALANCEITEMSLINKSREQUEST._serialized_start=5410
  _BALANCEITEMSLINKSREQUEST._serialized_end=5526
  _BALANCEITEMSLINKSRESULT._serialized_start=5528
  _BALANCEITEMSLINKSRESULT._serialized_end=5642
# @@protoc_insertion_point(module_scope)
