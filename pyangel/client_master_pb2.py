# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_master.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client_master.proto',
  package='ClientMaster',
  syntax='proto3',
  serialized_options=_b('\n com.tencent.client.master.protosB\021ClientMasterProtoP\001\210\001\001'),
  serialized_pb=_b('\n\x13\x63lient_master.proto\x12\x0c\x43lientMaster\x1a\x0c\x63ommon.proto\"/\n\x11RegisterWorkerReq\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"\xca\x01\n\x12RegisterWorkerResp\x12\x0e\n\x06workId\x18\x02 \x01(\x03\x12\x0f\n\x07isChief\x18\x03 \x01(\x08\x12\x1f\n\nasyncModel\x18\x05 \x01(\x0e\x32\x0b.AsyncModel\x12\x38\n\x04\x63onf\x18\x06 \x03(\x0b\x32*.ClientMaster.RegisterWorkerResp.ConfEntry\x12\x0b\n\x03msg\x18\x07 \x01(\t\x1a+\n\tConfEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x0fRegisterTaskReq\x12\x0e\n\x06workId\x18\x02 \x01(\x03\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"\x9b\x01\n\x10RegisterTaskResp\x12\x0e\n\x06taskId\x18\x02 \x01(\x03\x12\x0f\n\x07numTask\x18\x04 \x01(\x05\x12\x38\n\x05\x63lock\x18\x03 \x03(\x0b\x32).ClientMaster.RegisterTaskResp.ClockEntry\x1a,\n\nClockEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"A\n\x13SetAngelLocationReq\x12\x0e\n\x06workId\x18\x01 \x01(\x03\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\"?\n\x14GetAngelLocationResp\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0b\n\x03msg\x18\x04 \x01(\t\"\x1e\n\x0cHeartBeatReq\x12\x0e\n\x06workId\x18\x01 \x01(\x03\"3\n\rHeartBeatResp\x12\"\n\x03\x63md\x18\x03 \x01(\x0e\x32\x15.ClientMaster.Command\"<\n\x08\x43lockReq\x12\x0e\n\x06taskId\x18\x01 \x01(\x03\x12\r\n\x05\x63lock\x18\x02 \x01(\x05\x12\x11\n\tbatchSize\x18\x03 \x01(\x05\"\x85\x01\n\tClockResp\x12\x0e\n\x06taskId\x18\x01 \x01(\x03\x12\x37\n\x08\x63lockMap\x18\x02 \x03(\x0b\x32%.ClientMaster.ClockResp.ClockMapEntry\x1a/\n\rClockMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\" \n\x0eGetClockMapReq\x12\x0e\n\x06taskId\x18\x01 \x01(\x03\"\x91\x01\n\x0fGetClockMapResp\x12\x0e\n\x06taskId\x18\x01 \x01(\x03\x12=\n\x08\x63lockMap\x18\x02 \x03(\x0b\x32+.ClientMaster.GetClockMapResp.ClockMapEntry\x1a/\n\rClockMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\'\n\x12GetGlobalBatchResp\x12\x11\n\tbatchSize\x18\x01 \x01(\x05*F\n\x07\x43ommand\x12\r\n\tSTOPANGEL\x10\x00\x12\x0f\n\x0bSTOPPSAGENT\x10\x01\x12\x0e\n\nSTOPWORKER\x10\x02\x12\x0b\n\x07NOTHING\x10\x03\x32\x88\x05\n\x11\x41ngelCleintMaster\x12U\n\x0eRegisterWorker\x12\x1f.ClientMaster.RegisterWorkerReq\x1a .ClientMaster.RegisterWorkerResp\"\x00\x12O\n\x0cRegisterTask\x12\x1d.ClientMaster.RegisterTaskReq\x1a\x1e.ClientMaster.RegisterTaskResp\"\x00\x12\x42\n\x10SetAngelLocation\x12!.ClientMaster.SetAngelLocationReq\x1a\t.VoidResp\"\x00\x12\x42\n\x10GetAngelLocation\x12\x08.VoidReq\x1a\".ClientMaster.GetAngelLocationResp\"\x00\x12\x46\n\tHeartBeat\x12\x1a.ClientMaster.HeartBeatReq\x1a\x1b.ClientMaster.HeartBeatResp\"\x00\x12:\n\x05\x43lock\x12\x16.ClientMaster.ClockReq\x1a\x17.ClientMaster.ClockResp\"\x00\x12L\n\x0bGetClockMap\x12\x1c.ClientMaster.GetClockMapReq\x1a\x1d.ClientMaster.GetClockMapResp\"\x00\x12\x42\n\x12GetGlobalBatchSize\x12\x08.VoidReq\x1a .ClientMaster.GetGlobalBatchResp\"\x00\x12-\n\x0c\x43ompleteTask\x12\x10.CompleteTaskReq\x1a\t.VoidResp\"\x00\x42:\n com.tencent.client.master.protosB\x11\x43lientMasterProtoP\x01\x88\x01\x01\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='ClientMaster.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOPANGEL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPSAGENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPWORKER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTHING', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1155,
  serialized_end=1225,
)
_sym_db.RegisterEnumDescriptor(_COMMAND)

Command = enum_type_wrapper.EnumTypeWrapper(_COMMAND)
STOPANGEL = 0
STOPPSAGENT = 1
STOPWORKER = 2
NOTHING = 3



_REGISTERWORKERREQ = _descriptor.Descriptor(
  name='RegisterWorkerReq',
  full_name='ClientMaster.RegisterWorkerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='ClientMaster.RegisterWorkerReq.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ClientMaster.RegisterWorkerReq.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=51,
  serialized_end=98,
)


_REGISTERWORKERRESP_CONFENTRY = _descriptor.Descriptor(
  name='ConfEntry',
  full_name='ClientMaster.RegisterWorkerResp.ConfEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientMaster.RegisterWorkerResp.ConfEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientMaster.RegisterWorkerResp.ConfEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=303,
)

_REGISTERWORKERRESP = _descriptor.Descriptor(
  name='RegisterWorkerResp',
  full_name='ClientMaster.RegisterWorkerResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workId', full_name='ClientMaster.RegisterWorkerResp.workId', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isChief', full_name='ClientMaster.RegisterWorkerResp.isChief', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asyncModel', full_name='ClientMaster.RegisterWorkerResp.asyncModel', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='ClientMaster.RegisterWorkerResp.conf', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ClientMaster.RegisterWorkerResp.msg', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REGISTERWORKERRESP_CONFENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=303,
)


_REGISTERTASKREQ = _descriptor.Descriptor(
  name='RegisterTaskReq',
  full_name='ClientMaster.RegisterTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workId', full_name='ClientMaster.RegisterTaskReq.workId', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ClientMaster.RegisterTaskReq.timestamp', index=1,
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
  ],
  serialized_start=305,
  serialized_end=357,
)


_REGISTERTASKRESP_CLOCKENTRY = _descriptor.Descriptor(
  name='ClockEntry',
  full_name='ClientMaster.RegisterTaskResp.ClockEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientMaster.RegisterTaskResp.ClockEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientMaster.RegisterTaskResp.ClockEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=515,
)

_REGISTERTASKRESP = _descriptor.Descriptor(
  name='RegisterTaskResp',
  full_name='ClientMaster.RegisterTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='ClientMaster.RegisterTaskResp.taskId', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numTask', full_name='ClientMaster.RegisterTaskResp.numTask', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clock', full_name='ClientMaster.RegisterTaskResp.clock', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REGISTERTASKRESP_CLOCKENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=515,
)


_SETANGELLOCATIONREQ = _descriptor.Descriptor(
  name='SetAngelLocationReq',
  full_name='ClientMaster.SetAngelLocationReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workId', full_name='ClientMaster.SetAngelLocationReq.workId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='ClientMaster.SetAngelLocationReq.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ClientMaster.SetAngelLocationReq.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=517,
  serialized_end=582,
)


_GETANGELLOCATIONRESP = _descriptor.Descriptor(
  name='GetAngelLocationResp',
  full_name='ClientMaster.GetAngelLocationResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='ClientMaster.GetAngelLocationResp.host', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='ClientMaster.GetAngelLocationResp.port', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ClientMaster.GetAngelLocationResp.msg', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=647,
)


_HEARTBEATREQ = _descriptor.Descriptor(
  name='HeartBeatReq',
  full_name='ClientMaster.HeartBeatReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workId', full_name='ClientMaster.HeartBeatReq.workId', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=649,
  serialized_end=679,
)


_HEARTBEATRESP = _descriptor.Descriptor(
  name='HeartBeatResp',
  full_name='ClientMaster.HeartBeatResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='ClientMaster.HeartBeatResp.cmd', index=0,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=681,
  serialized_end=732,
)


_CLOCKREQ = _descriptor.Descriptor(
  name='ClockReq',
  full_name='ClientMaster.ClockReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='ClientMaster.ClockReq.taskId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clock', full_name='ClientMaster.ClockReq.clock', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchSize', full_name='ClientMaster.ClockReq.batchSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=734,
  serialized_end=794,
)


_CLOCKRESP_CLOCKMAPENTRY = _descriptor.Descriptor(
  name='ClockMapEntry',
  full_name='ClientMaster.ClockResp.ClockMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientMaster.ClockResp.ClockMapEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientMaster.ClockResp.ClockMapEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=883,
  serialized_end=930,
)

_CLOCKRESP = _descriptor.Descriptor(
  name='ClockResp',
  full_name='ClientMaster.ClockResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='ClientMaster.ClockResp.taskId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clockMap', full_name='ClientMaster.ClockResp.clockMap', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLOCKRESP_CLOCKMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=797,
  serialized_end=930,
)


_GETCLOCKMAPREQ = _descriptor.Descriptor(
  name='GetClockMapReq',
  full_name='ClientMaster.GetClockMapReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='ClientMaster.GetClockMapReq.taskId', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=932,
  serialized_end=964,
)


_GETCLOCKMAPRESP_CLOCKMAPENTRY = _descriptor.Descriptor(
  name='ClockMapEntry',
  full_name='ClientMaster.GetClockMapResp.ClockMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientMaster.GetClockMapResp.ClockMapEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientMaster.GetClockMapResp.ClockMapEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=883,
  serialized_end=930,
)

_GETCLOCKMAPRESP = _descriptor.Descriptor(
  name='GetClockMapResp',
  full_name='ClientMaster.GetClockMapResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='ClientMaster.GetClockMapResp.taskId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clockMap', full_name='ClientMaster.GetClockMapResp.clockMap', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETCLOCKMAPRESP_CLOCKMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=967,
  serialized_end=1112,
)


_GETGLOBALBATCHRESP = _descriptor.Descriptor(
  name='GetGlobalBatchResp',
  full_name='ClientMaster.GetGlobalBatchResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batchSize', full_name='ClientMaster.GetGlobalBatchResp.batchSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1114,
  serialized_end=1153,
)

_REGISTERWORKERRESP_CONFENTRY.containing_type = _REGISTERWORKERRESP
_REGISTERWORKERRESP.fields_by_name['asyncModel'].enum_type = common__pb2._ASYNCMODEL
_REGISTERWORKERRESP.fields_by_name['conf'].message_type = _REGISTERWORKERRESP_CONFENTRY
_REGISTERTASKRESP_CLOCKENTRY.containing_type = _REGISTERTASKRESP
_REGISTERTASKRESP.fields_by_name['clock'].message_type = _REGISTERTASKRESP_CLOCKENTRY
_HEARTBEATRESP.fields_by_name['cmd'].enum_type = _COMMAND
_CLOCKRESP_CLOCKMAPENTRY.containing_type = _CLOCKRESP
_CLOCKRESP.fields_by_name['clockMap'].message_type = _CLOCKRESP_CLOCKMAPENTRY
_GETCLOCKMAPRESP_CLOCKMAPENTRY.containing_type = _GETCLOCKMAPRESP
_GETCLOCKMAPRESP.fields_by_name['clockMap'].message_type = _GETCLOCKMAPRESP_CLOCKMAPENTRY
DESCRIPTOR.message_types_by_name['RegisterWorkerReq'] = _REGISTERWORKERREQ
DESCRIPTOR.message_types_by_name['RegisterWorkerResp'] = _REGISTERWORKERRESP
DESCRIPTOR.message_types_by_name['RegisterTaskReq'] = _REGISTERTASKREQ
DESCRIPTOR.message_types_by_name['RegisterTaskResp'] = _REGISTERTASKRESP
DESCRIPTOR.message_types_by_name['SetAngelLocationReq'] = _SETANGELLOCATIONREQ
DESCRIPTOR.message_types_by_name['GetAngelLocationResp'] = _GETANGELLOCATIONRESP
DESCRIPTOR.message_types_by_name['HeartBeatReq'] = _HEARTBEATREQ
DESCRIPTOR.message_types_by_name['HeartBeatResp'] = _HEARTBEATRESP
DESCRIPTOR.message_types_by_name['ClockReq'] = _CLOCKREQ
DESCRIPTOR.message_types_by_name['ClockResp'] = _CLOCKRESP
DESCRIPTOR.message_types_by_name['GetClockMapReq'] = _GETCLOCKMAPREQ
DESCRIPTOR.message_types_by_name['GetClockMapResp'] = _GETCLOCKMAPRESP
DESCRIPTOR.message_types_by_name['GetGlobalBatchResp'] = _GETGLOBALBATCHRESP
DESCRIPTOR.enum_types_by_name['Command'] = _COMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterWorkerReq = _reflection.GeneratedProtocolMessageType('RegisterWorkerReq', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERWORKERREQ,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.RegisterWorkerReq)
  })
_sym_db.RegisterMessage(RegisterWorkerReq)

RegisterWorkerResp = _reflection.GeneratedProtocolMessageType('RegisterWorkerResp', (_message.Message,), {

  'ConfEntry' : _reflection.GeneratedProtocolMessageType('ConfEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERWORKERRESP_CONFENTRY,
    '__module__' : 'client_master_pb2'
    # @@protoc_insertion_point(class_scope:ClientMaster.RegisterWorkerResp.ConfEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTERWORKERRESP,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.RegisterWorkerResp)
  })
_sym_db.RegisterMessage(RegisterWorkerResp)
_sym_db.RegisterMessage(RegisterWorkerResp.ConfEntry)

RegisterTaskReq = _reflection.GeneratedProtocolMessageType('RegisterTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTASKREQ,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.RegisterTaskReq)
  })
_sym_db.RegisterMessage(RegisterTaskReq)

RegisterTaskResp = _reflection.GeneratedProtocolMessageType('RegisterTaskResp', (_message.Message,), {

  'ClockEntry' : _reflection.GeneratedProtocolMessageType('ClockEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTERTASKRESP_CLOCKENTRY,
    '__module__' : 'client_master_pb2'
    # @@protoc_insertion_point(class_scope:ClientMaster.RegisterTaskResp.ClockEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTERTASKRESP,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.RegisterTaskResp)
  })
_sym_db.RegisterMessage(RegisterTaskResp)
_sym_db.RegisterMessage(RegisterTaskResp.ClockEntry)

SetAngelLocationReq = _reflection.GeneratedProtocolMessageType('SetAngelLocationReq', (_message.Message,), {
  'DESCRIPTOR' : _SETANGELLOCATIONREQ,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.SetAngelLocationReq)
  })
_sym_db.RegisterMessage(SetAngelLocationReq)

GetAngelLocationResp = _reflection.GeneratedProtocolMessageType('GetAngelLocationResp', (_message.Message,), {
  'DESCRIPTOR' : _GETANGELLOCATIONRESP,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.GetAngelLocationResp)
  })
_sym_db.RegisterMessage(GetAngelLocationResp)

HeartBeatReq = _reflection.GeneratedProtocolMessageType('HeartBeatReq', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQ,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.HeartBeatReq)
  })
_sym_db.RegisterMessage(HeartBeatReq)

HeartBeatResp = _reflection.GeneratedProtocolMessageType('HeartBeatResp', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESP,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.HeartBeatResp)
  })
_sym_db.RegisterMessage(HeartBeatResp)

ClockReq = _reflection.GeneratedProtocolMessageType('ClockReq', (_message.Message,), {
  'DESCRIPTOR' : _CLOCKREQ,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.ClockReq)
  })
_sym_db.RegisterMessage(ClockReq)

ClockResp = _reflection.GeneratedProtocolMessageType('ClockResp', (_message.Message,), {

  'ClockMapEntry' : _reflection.GeneratedProtocolMessageType('ClockMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLOCKRESP_CLOCKMAPENTRY,
    '__module__' : 'client_master_pb2'
    # @@protoc_insertion_point(class_scope:ClientMaster.ClockResp.ClockMapEntry)
    })
  ,
  'DESCRIPTOR' : _CLOCKRESP,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.ClockResp)
  })
_sym_db.RegisterMessage(ClockResp)
_sym_db.RegisterMessage(ClockResp.ClockMapEntry)

GetClockMapReq = _reflection.GeneratedProtocolMessageType('GetClockMapReq', (_message.Message,), {
  'DESCRIPTOR' : _GETCLOCKMAPREQ,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.GetClockMapReq)
  })
_sym_db.RegisterMessage(GetClockMapReq)

GetClockMapResp = _reflection.GeneratedProtocolMessageType('GetClockMapResp', (_message.Message,), {

  'ClockMapEntry' : _reflection.GeneratedProtocolMessageType('ClockMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETCLOCKMAPRESP_CLOCKMAPENTRY,
    '__module__' : 'client_master_pb2'
    # @@protoc_insertion_point(class_scope:ClientMaster.GetClockMapResp.ClockMapEntry)
    })
  ,
  'DESCRIPTOR' : _GETCLOCKMAPRESP,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.GetClockMapResp)
  })
_sym_db.RegisterMessage(GetClockMapResp)
_sym_db.RegisterMessage(GetClockMapResp.ClockMapEntry)

GetGlobalBatchResp = _reflection.GeneratedProtocolMessageType('GetGlobalBatchResp', (_message.Message,), {
  'DESCRIPTOR' : _GETGLOBALBATCHRESP,
  '__module__' : 'client_master_pb2'
  # @@protoc_insertion_point(class_scope:ClientMaster.GetGlobalBatchResp)
  })
_sym_db.RegisterMessage(GetGlobalBatchResp)


DESCRIPTOR._options = None
_REGISTERWORKERRESP_CONFENTRY._options = None
_REGISTERTASKRESP_CLOCKENTRY._options = None
_CLOCKRESP_CLOCKMAPENTRY._options = None
_GETCLOCKMAPRESP_CLOCKMAPENTRY._options = None

_ANGELCLEINTMASTER = _descriptor.ServiceDescriptor(
  name='AngelCleintMaster',
  full_name='ClientMaster.AngelCleintMaster',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1228,
  serialized_end=1876,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterWorker',
    full_name='ClientMaster.AngelCleintMaster.RegisterWorker',
    index=0,
    containing_service=None,
    input_type=_REGISTERWORKERREQ,
    output_type=_REGISTERWORKERRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterTask',
    full_name='ClientMaster.AngelCleintMaster.RegisterTask',
    index=1,
    containing_service=None,
    input_type=_REGISTERTASKREQ,
    output_type=_REGISTERTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetAngelLocation',
    full_name='ClientMaster.AngelCleintMaster.SetAngelLocation',
    index=2,
    containing_service=None,
    input_type=_SETANGELLOCATIONREQ,
    output_type=common__pb2._VOIDRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAngelLocation',
    full_name='ClientMaster.AngelCleintMaster.GetAngelLocation',
    index=3,
    containing_service=None,
    input_type=common__pb2._VOIDREQ,
    output_type=_GETANGELLOCATIONRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HeartBeat',
    full_name='ClientMaster.AngelCleintMaster.HeartBeat',
    index=4,
    containing_service=None,
    input_type=_HEARTBEATREQ,
    output_type=_HEARTBEATRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Clock',
    full_name='ClientMaster.AngelCleintMaster.Clock',
    index=5,
    containing_service=None,
    input_type=_CLOCKREQ,
    output_type=_CLOCKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetClockMap',
    full_name='ClientMaster.AngelCleintMaster.GetClockMap',
    index=6,
    containing_service=None,
    input_type=_GETCLOCKMAPREQ,
    output_type=_GETCLOCKMAPRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetGlobalBatchSize',
    full_name='ClientMaster.AngelCleintMaster.GetGlobalBatchSize',
    index=7,
    containing_service=None,
    input_type=common__pb2._VOIDREQ,
    output_type=_GETGLOBALBATCHRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CompleteTask',
    full_name='ClientMaster.AngelCleintMaster.CompleteTask',
    index=8,
    containing_service=None,
    input_type=common__pb2._COMPLETETASKREQ,
    output_type=common__pb2._VOIDRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANGELCLEINTMASTER)

DESCRIPTOR.services_by_name['AngelCleintMaster'] = _ANGELCLEINTMASTER

# @@protoc_insertion_point(module_scope)
