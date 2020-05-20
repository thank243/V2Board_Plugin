# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/transport/internet/tcp/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.serial import typed_message_pb2 as v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/transport/internet/tcp/config.proto',
  package='v2ray.core.transport.internet.tcp',
  syntax='proto3',
  serialized_options=b'\n%com.v2ray.core.transport.internet.tcpP\001Z\003tcp\252\002!V2Ray.Core.Transport.Internet.Tcp',
  serialized_pb=b'\n2v2ray.com/core/transport/internet/tcp/config.proto\x12!v2ray.core.transport.internet.tcp\x1a\x30v2ray.com/core/common/serial/typed_message.proto\"O\n\x06\x43onfig\x12?\n\x0fheader_settings\x18\x02 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessageJ\x04\x08\x01\x10\x02\x42R\n%com.v2ray.core.transport.internet.tcpP\x01Z\x03tcp\xaa\x02!V2Ray.Core.Transport.Internet.Tcpb\x06proto3'
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.tcp.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_settings', full_name='v2ray.core.transport.internet.tcp.Config.header_settings', index=0,
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
  serialized_start=139,
  serialized_end=218,
)

_CONFIG.fields_by_name['header_settings'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.transport.internet.tcp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.tcp.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
