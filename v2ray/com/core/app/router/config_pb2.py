# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/app/router/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.net import port_pb2 as v2ray_dot_com_dot_core_dot_common_dot_net_dot_port__pb2
from v2ray.com.core.common.net import network_pb2 as v2ray_dot_com_dot_core_dot_common_dot_net_dot_network__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/app/router/config.proto',
  package='v2ray.core.app.router',
  syntax='proto3',
  serialized_options=b'\n\031com.v2ray.core.app.routerP\001Z\006router\252\002\025V2Ray.Core.App.Router',
  serialized_pb=b'\n&v2ray.com/core/app/router/config.proto\x12\x15v2ray.core.app.router\x1a$v2ray.com/core/common/net/port.proto\x1a\'v2ray.com/core/common/net/network.proto\"\x8d\x02\n\x06\x44omain\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".v2ray.core.app.router.Domain.Type\x12\r\n\x05value\x18\x02 \x01(\t\x12:\n\tattribute\x18\x03 \x03(\x0b\x32\'.v2ray.core.app.router.Domain.Attribute\x1aR\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x42\r\n\x0btyped_value\"2\n\x04Type\x12\t\n\x05Plain\x10\x00\x12\t\n\x05Regex\x10\x01\x12\n\n\x06\x44omain\x10\x02\x12\x08\n\x04\x46ull\x10\x03\"\"\n\x04\x43IDR\x12\n\n\x02ip\x18\x01 \x01(\x0c\x12\x0e\n\x06prefix\x18\x02 \x01(\r\"H\n\x05GeoIP\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12)\n\x04\x63idr\x18\x02 \x03(\x0b\x32\x1b.v2ray.core.app.router.CIDR\"8\n\tGeoIPList\x12+\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x1c.v2ray.core.app.router.GeoIP\"N\n\x07GeoSite\x12\x14\n\x0c\x63ountry_code\x18\x01 \x01(\t\x12-\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x1d.v2ray.core.app.router.Domain\"<\n\x0bGeoSiteList\x12-\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x1e.v2ray.core.app.router.GeoSite\"\xe5\x04\n\x0bRoutingRule\x12\r\n\x03tag\x18\x01 \x01(\tH\x00\x12\x17\n\rbalancing_tag\x18\x0c \x01(\tH\x00\x12-\n\x06\x64omain\x18\x02 \x03(\x0b\x32\x1d.v2ray.core.app.router.Domain\x12-\n\x04\x63idr\x18\x03 \x03(\x0b\x32\x1b.v2ray.core.app.router.CIDRB\x02\x18\x01\x12+\n\x05geoip\x18\n \x03(\x0b\x32\x1c.v2ray.core.app.router.GeoIP\x12\x38\n\nport_range\x18\x04 \x01(\x0b\x32 .v2ray.core.common.net.PortRangeB\x02\x18\x01\x12\x32\n\tport_list\x18\x0e \x01(\x0b\x32\x1f.v2ray.core.common.net.PortList\x12<\n\x0cnetwork_list\x18\x05 \x01(\x0b\x32\".v2ray.core.common.net.NetworkListB\x02\x18\x01\x12\x30\n\x08networks\x18\r \x03(\x0e\x32\x1e.v2ray.core.common.net.Network\x12\x34\n\x0bsource_cidr\x18\x06 \x03(\x0b\x32\x1b.v2ray.core.app.router.CIDRB\x02\x18\x01\x12\x32\n\x0csource_geoip\x18\x0b \x03(\x0b\x32\x1c.v2ray.core.app.router.GeoIP\x12\x12\n\nuser_email\x18\x07 \x03(\t\x12\x13\n\x0binbound_tag\x18\x08 \x03(\t\x12\x10\n\x08protocol\x18\t \x03(\t\x12\x12\n\nattributes\x18\x0f \x01(\tB\x0c\n\ntarget_tag\"7\n\rBalancingRule\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x19\n\x11outbound_selector\x18\x02 \x03(\t\"\x88\x02\n\x06\x43onfig\x12\x45\n\x0f\x64omain_strategy\x18\x01 \x01(\x0e\x32,.v2ray.core.app.router.Config.DomainStrategy\x12\x30\n\x04rule\x18\x02 \x03(\x0b\x32\".v2ray.core.app.router.RoutingRule\x12<\n\x0e\x62\x61lancing_rule\x18\x03 \x03(\x0b\x32$.v2ray.core.app.router.BalancingRule\"G\n\x0e\x44omainStrategy\x12\x08\n\x04\x41sIs\x10\x00\x12\t\n\x05UseIp\x10\x01\x12\x10\n\x0cIpIfNonMatch\x10\x02\x12\x0e\n\nIpOnDemand\x10\x03\x42=\n\x19\x63om.v2ray.core.app.routerP\x01Z\x06router\xaa\x02\x15V2Ray.Core.App.Routerb\x06proto3'
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_net_dot_port__pb2.DESCRIPTOR,v2ray_dot_com_dot_core_dot_common_dot_net_dot_network__pb2.DESCRIPTOR,])



_DOMAIN_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='v2ray.core.app.router.Domain.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Plain', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Regex', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Domain', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Full', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=364,
  serialized_end=414,
)
_sym_db.RegisterEnumDescriptor(_DOMAIN_TYPE)

_CONFIG_DOMAINSTRATEGY = _descriptor.EnumDescriptor(
  name='DomainStrategy',
  full_name='v2ray.core.app.router.Config.DomainStrategy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AsIs', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UseIp', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IpIfNonMatch', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IpOnDemand', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1593,
  serialized_end=1664,
)
_sym_db.RegisterEnumDescriptor(_CONFIG_DOMAINSTRATEGY)


_DOMAIN_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='v2ray.core.app.router.Domain.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v2ray.core.app.router.Domain.Attribute.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='v2ray.core.app.router.Domain.Attribute.bool_value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='v2ray.core.app.router.Domain.Attribute.int_value', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='typed_value', full_name='v2ray.core.app.router.Domain.Attribute.typed_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=280,
  serialized_end=362,
)

_DOMAIN = _descriptor.Descriptor(
  name='Domain',
  full_name='v2ray.core.app.router.Domain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='v2ray.core.app.router.Domain.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.app.router.Domain.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='v2ray.core.app.router.Domain.attribute', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DOMAIN_ATTRIBUTE, ],
  enum_types=[
    _DOMAIN_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=414,
)


_CIDR = _descriptor.Descriptor(
  name='CIDR',
  full_name='v2ray.core.app.router.CIDR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='v2ray.core.app.router.CIDR.ip', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='v2ray.core.app.router.CIDR.prefix', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=416,
  serialized_end=450,
)


_GEOIP = _descriptor.Descriptor(
  name='GeoIP',
  full_name='v2ray.core.app.router.GeoIP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_code', full_name='v2ray.core.app.router.GeoIP.country_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cidr', full_name='v2ray.core.app.router.GeoIP.cidr', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=452,
  serialized_end=524,
)


_GEOIPLIST = _descriptor.Descriptor(
  name='GeoIPList',
  full_name='v2ray.core.app.router.GeoIPList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='v2ray.core.app.router.GeoIPList.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=526,
  serialized_end=582,
)


_GEOSITE = _descriptor.Descriptor(
  name='GeoSite',
  full_name='v2ray.core.app.router.GeoSite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_code', full_name='v2ray.core.app.router.GeoSite.country_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='v2ray.core.app.router.GeoSite.domain', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=584,
  serialized_end=662,
)


_GEOSITELIST = _descriptor.Descriptor(
  name='GeoSiteList',
  full_name='v2ray.core.app.router.GeoSiteList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='v2ray.core.app.router.GeoSiteList.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=664,
  serialized_end=724,
)


_ROUTINGRULE = _descriptor.Descriptor(
  name='RoutingRule',
  full_name='v2ray.core.app.router.RoutingRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.router.RoutingRule.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balancing_tag', full_name='v2ray.core.app.router.RoutingRule.balancing_tag', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='v2ray.core.app.router.RoutingRule.domain', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cidr', full_name='v2ray.core.app.router.RoutingRule.cidr', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geoip', full_name='v2ray.core.app.router.RoutingRule.geoip', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port_range', full_name='v2ray.core.app.router.RoutingRule.port_range', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port_list', full_name='v2ray.core.app.router.RoutingRule.port_list', index=6,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_list', full_name='v2ray.core.app.router.RoutingRule.network_list', index=7,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networks', full_name='v2ray.core.app.router.RoutingRule.networks', index=8,
      number=13, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_cidr', full_name='v2ray.core.app.router.RoutingRule.source_cidr', index=9,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_geoip', full_name='v2ray.core.app.router.RoutingRule.source_geoip', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='v2ray.core.app.router.RoutingRule.user_email', index=11,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbound_tag', full_name='v2ray.core.app.router.RoutingRule.inbound_tag', index=12,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='v2ray.core.app.router.RoutingRule.protocol', index=13,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='v2ray.core.app.router.RoutingRule.attributes', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='target_tag', full_name='v2ray.core.app.router.RoutingRule.target_tag',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=727,
  serialized_end=1340,
)


_BALANCINGRULE = _descriptor.Descriptor(
  name='BalancingRule',
  full_name='v2ray.core.app.router.BalancingRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.router.BalancingRule.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outbound_selector', full_name='v2ray.core.app.router.BalancingRule.outbound_selector', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1342,
  serialized_end=1397,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.app.router.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_strategy', full_name='v2ray.core.app.router.Config.domain_strategy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='v2ray.core.app.router.Config.rule', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balancing_rule', full_name='v2ray.core.app.router.Config.balancing_rule', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIG_DOMAINSTRATEGY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1400,
  serialized_end=1664,
)

_DOMAIN_ATTRIBUTE.containing_type = _DOMAIN
_DOMAIN_ATTRIBUTE.oneofs_by_name['typed_value'].fields.append(
  _DOMAIN_ATTRIBUTE.fields_by_name['bool_value'])
_DOMAIN_ATTRIBUTE.fields_by_name['bool_value'].containing_oneof = _DOMAIN_ATTRIBUTE.oneofs_by_name['typed_value']
_DOMAIN_ATTRIBUTE.oneofs_by_name['typed_value'].fields.append(
  _DOMAIN_ATTRIBUTE.fields_by_name['int_value'])
_DOMAIN_ATTRIBUTE.fields_by_name['int_value'].containing_oneof = _DOMAIN_ATTRIBUTE.oneofs_by_name['typed_value']
_DOMAIN.fields_by_name['type'].enum_type = _DOMAIN_TYPE
_DOMAIN.fields_by_name['attribute'].message_type = _DOMAIN_ATTRIBUTE
_DOMAIN_TYPE.containing_type = _DOMAIN
_GEOIP.fields_by_name['cidr'].message_type = _CIDR
_GEOIPLIST.fields_by_name['entry'].message_type = _GEOIP
_GEOSITE.fields_by_name['domain'].message_type = _DOMAIN
_GEOSITELIST.fields_by_name['entry'].message_type = _GEOSITE
_ROUTINGRULE.fields_by_name['domain'].message_type = _DOMAIN
_ROUTINGRULE.fields_by_name['cidr'].message_type = _CIDR
_ROUTINGRULE.fields_by_name['geoip'].message_type = _GEOIP
_ROUTINGRULE.fields_by_name['port_range'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_port__pb2._PORTRANGE
_ROUTINGRULE.fields_by_name['port_list'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_port__pb2._PORTLIST
_ROUTINGRULE.fields_by_name['network_list'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_network__pb2._NETWORKLIST
_ROUTINGRULE.fields_by_name['networks'].enum_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_network__pb2._NETWORK
_ROUTINGRULE.fields_by_name['source_cidr'].message_type = _CIDR
_ROUTINGRULE.fields_by_name['source_geoip'].message_type = _GEOIP
_ROUTINGRULE.oneofs_by_name['target_tag'].fields.append(
  _ROUTINGRULE.fields_by_name['tag'])
_ROUTINGRULE.fields_by_name['tag'].containing_oneof = _ROUTINGRULE.oneofs_by_name['target_tag']
_ROUTINGRULE.oneofs_by_name['target_tag'].fields.append(
  _ROUTINGRULE.fields_by_name['balancing_tag'])
_ROUTINGRULE.fields_by_name['balancing_tag'].containing_oneof = _ROUTINGRULE.oneofs_by_name['target_tag']
_CONFIG.fields_by_name['domain_strategy'].enum_type = _CONFIG_DOMAINSTRATEGY
_CONFIG.fields_by_name['rule'].message_type = _ROUTINGRULE
_CONFIG.fields_by_name['balancing_rule'].message_type = _BALANCINGRULE
_CONFIG_DOMAINSTRATEGY.containing_type = _CONFIG
DESCRIPTOR.message_types_by_name['Domain'] = _DOMAIN
DESCRIPTOR.message_types_by_name['CIDR'] = _CIDR
DESCRIPTOR.message_types_by_name['GeoIP'] = _GEOIP
DESCRIPTOR.message_types_by_name['GeoIPList'] = _GEOIPLIST
DESCRIPTOR.message_types_by_name['GeoSite'] = _GEOSITE
DESCRIPTOR.message_types_by_name['GeoSiteList'] = _GEOSITELIST
DESCRIPTOR.message_types_by_name['RoutingRule'] = _ROUTINGRULE
DESCRIPTOR.message_types_by_name['BalancingRule'] = _BALANCINGRULE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Domain = _reflection.GeneratedProtocolMessageType('Domain', (_message.Message,), {

  'Attribute' : _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
    'DESCRIPTOR' : _DOMAIN_ATTRIBUTE,
    '__module__' : 'v2ray.com.core.app.router.config_pb2'
    # @@protoc_insertion_point(class_scope:v2ray.core.app.router.Domain.Attribute)
    })
  ,
  'DESCRIPTOR' : _DOMAIN,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.Domain)
  })
_sym_db.RegisterMessage(Domain)
_sym_db.RegisterMessage(Domain.Attribute)

CIDR = _reflection.GeneratedProtocolMessageType('CIDR', (_message.Message,), {
  'DESCRIPTOR' : _CIDR,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.CIDR)
  })
_sym_db.RegisterMessage(CIDR)

GeoIP = _reflection.GeneratedProtocolMessageType('GeoIP', (_message.Message,), {
  'DESCRIPTOR' : _GEOIP,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.GeoIP)
  })
_sym_db.RegisterMessage(GeoIP)

GeoIPList = _reflection.GeneratedProtocolMessageType('GeoIPList', (_message.Message,), {
  'DESCRIPTOR' : _GEOIPLIST,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.GeoIPList)
  })
_sym_db.RegisterMessage(GeoIPList)

GeoSite = _reflection.GeneratedProtocolMessageType('GeoSite', (_message.Message,), {
  'DESCRIPTOR' : _GEOSITE,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.GeoSite)
  })
_sym_db.RegisterMessage(GeoSite)

GeoSiteList = _reflection.GeneratedProtocolMessageType('GeoSiteList', (_message.Message,), {
  'DESCRIPTOR' : _GEOSITELIST,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.GeoSiteList)
  })
_sym_db.RegisterMessage(GeoSiteList)

RoutingRule = _reflection.GeneratedProtocolMessageType('RoutingRule', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGRULE,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.RoutingRule)
  })
_sym_db.RegisterMessage(RoutingRule)

BalancingRule = _reflection.GeneratedProtocolMessageType('BalancingRule', (_message.Message,), {
  'DESCRIPTOR' : _BALANCINGRULE,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.BalancingRule)
  })
_sym_db.RegisterMessage(BalancingRule)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.app.router.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.router.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
_ROUTINGRULE.fields_by_name['cidr']._options = None
_ROUTINGRULE.fields_by_name['port_range']._options = None
_ROUTINGRULE.fields_by_name['network_list']._options = None
_ROUTINGRULE.fields_by_name['source_cidr']._options = None
# @@protoc_insertion_point(module_scope)
