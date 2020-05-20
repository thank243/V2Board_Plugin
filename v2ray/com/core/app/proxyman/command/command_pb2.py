# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/app/proxyman/command/command.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.protocol import user_pb2 as v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_user__pb2
from v2ray.com.core.common.serial import typed_message_pb2 as v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2
from v2ray.com.core import config_pb2 as v2ray_dot_com_dot_core_dot_config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/app/proxyman/command/command.proto',
  package='v2ray.core.app.proxyman.command',
  syntax='proto3',
  serialized_options=b'\n#com.v2ray.core.app.proxyman.commandP\001Z\007command\252\002\037V2Ray.Core.App.Proxyman.Command',
  serialized_pb=b'\n1v2ray.com/core/app/proxyman/command/command.proto\x12\x1fv2ray.core.app.proxyman.command\x1a)v2ray.com/core/common/protocol/user.proto\x1a\x30v2ray.com/core/common/serial/typed_message.proto\x1a\x1bv2ray.com/core/config.proto\"B\n\x10\x41\x64\x64UserOperation\x12.\n\x04user\x18\x01 \x01(\x0b\x32 .v2ray.core.common.protocol.User\"$\n\x13RemoveUserOperation\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"F\n\x11\x41\x64\x64InboundRequest\x12\x31\n\x07inbound\x18\x01 \x01(\x0b\x32 .v2ray.core.InboundHandlerConfig\"\x14\n\x12\x41\x64\x64InboundResponse\"#\n\x14RemoveInboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\x17\n\x15RemoveInboundResponse\"]\n\x13\x41lterInboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x39\n\toperation\x18\x02 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessage\"\x16\n\x14\x41lterInboundResponse\"I\n\x12\x41\x64\x64OutboundRequest\x12\x33\n\x08outbound\x18\x01 \x01(\x0b\x32!.v2ray.core.OutboundHandlerConfig\"\x15\n\x13\x41\x64\x64OutboundResponse\"$\n\x15RemoveOutboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\"\x18\n\x16RemoveOutboundResponse\"^\n\x14\x41lterOutboundRequest\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x39\n\toperation\x18\x02 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessage\"\x17\n\x15\x41lterOutboundResponse\"\x08\n\x06\x43onfig2\x90\x06\n\x0eHandlerService\x12w\n\nAddInbound\x12\x32.v2ray.core.app.proxyman.command.AddInboundRequest\x1a\x33.v2ray.core.app.proxyman.command.AddInboundResponse\"\x00\x12\x80\x01\n\rRemoveInbound\x12\x35.v2ray.core.app.proxyman.command.RemoveInboundRequest\x1a\x36.v2ray.core.app.proxyman.command.RemoveInboundResponse\"\x00\x12}\n\x0c\x41lterInbound\x12\x34.v2ray.core.app.proxyman.command.AlterInboundRequest\x1a\x35.v2ray.core.app.proxyman.command.AlterInboundResponse\"\x00\x12z\n\x0b\x41\x64\x64Outbound\x12\x33.v2ray.core.app.proxyman.command.AddOutboundRequest\x1a\x34.v2ray.core.app.proxyman.command.AddOutboundResponse\"\x00\x12\x83\x01\n\x0eRemoveOutbound\x12\x36.v2ray.core.app.proxyman.command.RemoveOutboundRequest\x1a\x37.v2ray.core.app.proxyman.command.RemoveOutboundResponse\"\x00\x12\x80\x01\n\rAlterOutbound\x12\x35.v2ray.core.app.proxyman.command.AlterOutboundRequest\x1a\x36.v2ray.core.app.proxyman.command.AlterOutboundResponse\"\x00\x42R\n#com.v2ray.core.app.proxyman.commandP\x01Z\x07\x63ommand\xaa\x02\x1fV2Ray.Core.App.Proxyman.Commandb\x06proto3'
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_user__pb2.DESCRIPTOR,v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2.DESCRIPTOR,v2ray_dot_com_dot_core_dot_config__pb2.DESCRIPTOR,])




_ADDUSEROPERATION = _descriptor.Descriptor(
  name='AddUserOperation',
  full_name='v2ray.core.app.proxyman.command.AddUserOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='v2ray.core.app.proxyman.command.AddUserOperation.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=274,
)


_REMOVEUSEROPERATION = _descriptor.Descriptor(
  name='RemoveUserOperation',
  full_name='v2ray.core.app.proxyman.command.RemoveUserOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='v2ray.core.app.proxyman.command.RemoveUserOperation.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=312,
)


_ADDINBOUNDREQUEST = _descriptor.Descriptor(
  name='AddInboundRequest',
  full_name='v2ray.core.app.proxyman.command.AddInboundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inbound', full_name='v2ray.core.app.proxyman.command.AddInboundRequest.inbound', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=384,
)


_ADDINBOUNDRESPONSE = _descriptor.Descriptor(
  name='AddInboundResponse',
  full_name='v2ray.core.app.proxyman.command.AddInboundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=406,
)


_REMOVEINBOUNDREQUEST = _descriptor.Descriptor(
  name='RemoveInboundRequest',
  full_name='v2ray.core.app.proxyman.command.RemoveInboundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.proxyman.command.RemoveInboundRequest.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=443,
)


_REMOVEINBOUNDRESPONSE = _descriptor.Descriptor(
  name='RemoveInboundResponse',
  full_name='v2ray.core.app.proxyman.command.RemoveInboundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=445,
  serialized_end=468,
)


_ALTERINBOUNDREQUEST = _descriptor.Descriptor(
  name='AlterInboundRequest',
  full_name='v2ray.core.app.proxyman.command.AlterInboundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.proxyman.command.AlterInboundRequest.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='v2ray.core.app.proxyman.command.AlterInboundRequest.operation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=563,
)


_ALTERINBOUNDRESPONSE = _descriptor.Descriptor(
  name='AlterInboundResponse',
  full_name='v2ray.core.app.proxyman.command.AlterInboundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=587,
)


_ADDOUTBOUNDREQUEST = _descriptor.Descriptor(
  name='AddOutboundRequest',
  full_name='v2ray.core.app.proxyman.command.AddOutboundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outbound', full_name='v2ray.core.app.proxyman.command.AddOutboundRequest.outbound', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=662,
)


_ADDOUTBOUNDRESPONSE = _descriptor.Descriptor(
  name='AddOutboundResponse',
  full_name='v2ray.core.app.proxyman.command.AddOutboundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=664,
  serialized_end=685,
)


_REMOVEOUTBOUNDREQUEST = _descriptor.Descriptor(
  name='RemoveOutboundRequest',
  full_name='v2ray.core.app.proxyman.command.RemoveOutboundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.proxyman.command.RemoveOutboundRequest.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=723,
)


_REMOVEOUTBOUNDRESPONSE = _descriptor.Descriptor(
  name='RemoveOutboundResponse',
  full_name='v2ray.core.app.proxyman.command.RemoveOutboundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=749,
)


_ALTEROUTBOUNDREQUEST = _descriptor.Descriptor(
  name='AlterOutboundRequest',
  full_name='v2ray.core.app.proxyman.command.AlterOutboundRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.proxyman.command.AlterOutboundRequest.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='v2ray.core.app.proxyman.command.AlterOutboundRequest.operation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=751,
  serialized_end=845,
)


_ALTEROUTBOUNDRESPONSE = _descriptor.Descriptor(
  name='AlterOutboundResponse',
  full_name='v2ray.core.app.proxyman.command.AlterOutboundResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=847,
  serialized_end=870,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.app.proxyman.command.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=880,
)

_ADDUSEROPERATION.fields_by_name['user'].message_type = v2ray_dot_com_dot_core_dot_common_dot_protocol_dot_user__pb2._USER
_ADDINBOUNDREQUEST.fields_by_name['inbound'].message_type = v2ray_dot_com_dot_core_dot_config__pb2._INBOUNDHANDLERCONFIG
_ALTERINBOUNDREQUEST.fields_by_name['operation'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
_ADDOUTBOUNDREQUEST.fields_by_name['outbound'].message_type = v2ray_dot_com_dot_core_dot_config__pb2._OUTBOUNDHANDLERCONFIG
_ALTEROUTBOUNDREQUEST.fields_by_name['operation'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
DESCRIPTOR.message_types_by_name['AddUserOperation'] = _ADDUSEROPERATION
DESCRIPTOR.message_types_by_name['RemoveUserOperation'] = _REMOVEUSEROPERATION
DESCRIPTOR.message_types_by_name['AddInboundRequest'] = _ADDINBOUNDREQUEST
DESCRIPTOR.message_types_by_name['AddInboundResponse'] = _ADDINBOUNDRESPONSE
DESCRIPTOR.message_types_by_name['RemoveInboundRequest'] = _REMOVEINBOUNDREQUEST
DESCRIPTOR.message_types_by_name['RemoveInboundResponse'] = _REMOVEINBOUNDRESPONSE
DESCRIPTOR.message_types_by_name['AlterInboundRequest'] = _ALTERINBOUNDREQUEST
DESCRIPTOR.message_types_by_name['AlterInboundResponse'] = _ALTERINBOUNDRESPONSE
DESCRIPTOR.message_types_by_name['AddOutboundRequest'] = _ADDOUTBOUNDREQUEST
DESCRIPTOR.message_types_by_name['AddOutboundResponse'] = _ADDOUTBOUNDRESPONSE
DESCRIPTOR.message_types_by_name['RemoveOutboundRequest'] = _REMOVEOUTBOUNDREQUEST
DESCRIPTOR.message_types_by_name['RemoveOutboundResponse'] = _REMOVEOUTBOUNDRESPONSE
DESCRIPTOR.message_types_by_name['AlterOutboundRequest'] = _ALTEROUTBOUNDREQUEST
DESCRIPTOR.message_types_by_name['AlterOutboundResponse'] = _ALTEROUTBOUNDRESPONSE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddUserOperation = _reflection.GeneratedProtocolMessageType('AddUserOperation', (_message.Message,), {
  'DESCRIPTOR' : _ADDUSEROPERATION,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AddUserOperation)
  })
_sym_db.RegisterMessage(AddUserOperation)

RemoveUserOperation = _reflection.GeneratedProtocolMessageType('RemoveUserOperation', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEUSEROPERATION,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.RemoveUserOperation)
  })
_sym_db.RegisterMessage(RemoveUserOperation)

AddInboundRequest = _reflection.GeneratedProtocolMessageType('AddInboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDINBOUNDREQUEST,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AddInboundRequest)
  })
_sym_db.RegisterMessage(AddInboundRequest)

AddInboundResponse = _reflection.GeneratedProtocolMessageType('AddInboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDINBOUNDRESPONSE,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AddInboundResponse)
  })
_sym_db.RegisterMessage(AddInboundResponse)

RemoveInboundRequest = _reflection.GeneratedProtocolMessageType('RemoveInboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEINBOUNDREQUEST,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.RemoveInboundRequest)
  })
_sym_db.RegisterMessage(RemoveInboundRequest)

RemoveInboundResponse = _reflection.GeneratedProtocolMessageType('RemoveInboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEINBOUNDRESPONSE,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.RemoveInboundResponse)
  })
_sym_db.RegisterMessage(RemoveInboundResponse)

AlterInboundRequest = _reflection.GeneratedProtocolMessageType('AlterInboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALTERINBOUNDREQUEST,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AlterInboundRequest)
  })
_sym_db.RegisterMessage(AlterInboundRequest)

AlterInboundResponse = _reflection.GeneratedProtocolMessageType('AlterInboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALTERINBOUNDRESPONSE,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AlterInboundResponse)
  })
_sym_db.RegisterMessage(AlterInboundResponse)

AddOutboundRequest = _reflection.GeneratedProtocolMessageType('AddOutboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDOUTBOUNDREQUEST,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AddOutboundRequest)
  })
_sym_db.RegisterMessage(AddOutboundRequest)

AddOutboundResponse = _reflection.GeneratedProtocolMessageType('AddOutboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDOUTBOUNDRESPONSE,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AddOutboundResponse)
  })
_sym_db.RegisterMessage(AddOutboundResponse)

RemoveOutboundRequest = _reflection.GeneratedProtocolMessageType('RemoveOutboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEOUTBOUNDREQUEST,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.RemoveOutboundRequest)
  })
_sym_db.RegisterMessage(RemoveOutboundRequest)

RemoveOutboundResponse = _reflection.GeneratedProtocolMessageType('RemoveOutboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEOUTBOUNDRESPONSE,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.RemoveOutboundResponse)
  })
_sym_db.RegisterMessage(RemoveOutboundResponse)

AlterOutboundRequest = _reflection.GeneratedProtocolMessageType('AlterOutboundRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALTEROUTBOUNDREQUEST,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AlterOutboundRequest)
  })
_sym_db.RegisterMessage(AlterOutboundRequest)

AlterOutboundResponse = _reflection.GeneratedProtocolMessageType('AlterOutboundResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALTEROUTBOUNDRESPONSE,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.AlterOutboundResponse)
  })
_sym_db.RegisterMessage(AlterOutboundResponse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.command.command_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.command.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None

_HANDLERSERVICE = _descriptor.ServiceDescriptor(
  name='HandlerService',
  full_name='v2ray.core.app.proxyman.command.HandlerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=883,
  serialized_end=1667,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddInbound',
    full_name='v2ray.core.app.proxyman.command.HandlerService.AddInbound',
    index=0,
    containing_service=None,
    input_type=_ADDINBOUNDREQUEST,
    output_type=_ADDINBOUNDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveInbound',
    full_name='v2ray.core.app.proxyman.command.HandlerService.RemoveInbound',
    index=1,
    containing_service=None,
    input_type=_REMOVEINBOUNDREQUEST,
    output_type=_REMOVEINBOUNDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AlterInbound',
    full_name='v2ray.core.app.proxyman.command.HandlerService.AlterInbound',
    index=2,
    containing_service=None,
    input_type=_ALTERINBOUNDREQUEST,
    output_type=_ALTERINBOUNDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddOutbound',
    full_name='v2ray.core.app.proxyman.command.HandlerService.AddOutbound',
    index=3,
    containing_service=None,
    input_type=_ADDOUTBOUNDREQUEST,
    output_type=_ADDOUTBOUNDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveOutbound',
    full_name='v2ray.core.app.proxyman.command.HandlerService.RemoveOutbound',
    index=4,
    containing_service=None,
    input_type=_REMOVEOUTBOUNDREQUEST,
    output_type=_REMOVEOUTBOUNDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AlterOutbound',
    full_name='v2ray.core.app.proxyman.command.HandlerService.AlterOutbound',
    index=5,
    containing_service=None,
    input_type=_ALTEROUTBOUNDREQUEST,
    output_type=_ALTEROUTBOUNDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HANDLERSERVICE)

DESCRIPTOR.services_by_name['HandlerService'] = _HANDLERSERVICE

# @@protoc_insertion_point(module_scope)
