# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WebAPI/user_attribute_2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dWebAPI/user_attribute_2.proto\x12\x10user_attribute_2\"=\n\rUserAttribute\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x03 \x01(\x08\"\x90\x01\n\x14ModifyUserAttributes\x12\x16\n\x0e\x63hain_order_id\x18\x01 \x02(\t\x12\x12\n\naccount_id\x18\x02 \x02(\x11\x12\x38\n\x0fuser_attributes\x18\x03 \x03(\x0b\x32\x1f.user_attribute_2.UserAttribute\x12\x12\n\nis_checked\x18\x04 \x01(\x08')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WebAPI.user_attribute_2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERATTRIBUTE._serialized_start=51
  _USERATTRIBUTE._serialized_end=112
  _MODIFYUSERATTRIBUTES._serialized_start=115
  _MODIFYUSERATTRIBUTES._serialized_end=259
# @@protoc_insertion_point(module_scope)