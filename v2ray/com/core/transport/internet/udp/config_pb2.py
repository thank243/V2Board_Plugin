# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/transport/internet/udp/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/transport/internet/udp/config.proto',
  package='v2ray.core.transport.internet.udp',
  syntax='proto3',
  serialized_options=b'\n%com.v2ray.core.transport.internet.udpP\001Z\003udp\252\002!V2Ray.Core.Transport.Internet.Udp',
  serialized_pb=b'\n2v2ray.com/core/transport/internet/udp/config.proto\x12!v2ray.core.transport.internet.udp\"\x08\n\x06\x43onfigBR\n%com.v2ray.core.transport.internet.udpP\x01Z\x03udp\xaa\x02!V2Ray.Core.Transport.Internet.Udpb\x06proto3'
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.udp.Config',
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
  serialized_start=89,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.transport.internet.udp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.udp.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
