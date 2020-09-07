#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import absolute_import
import six
from thrift.util.Recursive import fix_spec
from thrift.Thrift import *
from thrift.protocol.TProtocol import TProtocolException

from json import loads
import sys
if sys.version_info[0] >= 3:
  long = int


import pprint
import warnings
from thrift import Thrift
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.protocol import THeaderProtocol
fastproto = None
if not '__pypy__' in sys.builtin_module_names:
  try:
    from thrift.protocol import fastproto
  except ImportError:
    pass
all_structs = []
UTF8STRINGS = bool(0) or sys.version_info.major >= 3

__all__ = ['UTF8STRINGS', 'MyEnum', 'MyStructNestedAnnotation', 'MyStructAnnotation', 'MyStruct', 'SecretStruct']

class MyEnum:
  MyValue1 = 0
  MyValue2 = 1
  DOMAIN = 2

  _VALUES_TO_NAMES = {
    0: "MyValue1",
    1: "MyValue2",
    2: "DOMAIN",
  }

  _NAMES_TO_VALUES = {
    "MyValue1": 0,
    "MyValue2": 1,
    "DOMAIN": 2,
  }

class MyStructNestedAnnotation:
  """
  Attributes:
   - name
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('MyStructNestedAnnotation')
    if self.name != None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name.encode('utf-8')) if UTF8STRINGS and not isinstance(self.name, bytes) else oprot.writeString(self.name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def readFromJson(self, json, is_text=True, **kwargs):
    relax_enum_validation = bool(kwargs.pop('relax_enum_validation', False))
    set_cls = kwargs.pop('custom_set_cls', set)
    dict_cls = kwargs.pop('custom_dict_cls', dict)
    if kwargs:
        extra_kwargs = ', '.join(kwargs.keys())
        raise ValueError(
            'Unexpected keyword arguments: ' + extra_kwargs
        )
    json_obj = json
    if is_text:
      json_obj = loads(json)
    if 'name' in json_obj and json_obj['name'] is not None:
      self.name = json_obj['name']

  def __repr__(self):
    L = []
    padding = ' ' * 4
    if self.name is not None:
      value = pprint.pformat(self.name, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    name=%s' % (value))
    return "%s(%s)" % (self.__class__.__name__, "\n" + ",\n".join(L) if L else '')

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

class MyStructAnnotation:
  """
  Attributes:
   - count
   - name
   - extra
   - nest
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.count = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.extra = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.nest = MyStructNestedAnnotation()
          self.nest.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('MyStructAnnotation')
    if self.count != None:
      oprot.writeFieldBegin('count', TType.I64, 1)
      oprot.writeI64(self.count)
      oprot.writeFieldEnd()
    if self.name != None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name.encode('utf-8')) if UTF8STRINGS and not isinstance(self.name, bytes) else oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.extra != None:
      oprot.writeFieldBegin('extra', TType.STRING, 3)
      oprot.writeString(self.extra.encode('utf-8')) if UTF8STRINGS and not isinstance(self.extra, bytes) else oprot.writeString(self.extra)
      oprot.writeFieldEnd()
    if self.nest != None:
      oprot.writeFieldBegin('nest', TType.STRUCT, 4)
      self.nest.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def readFromJson(self, json, is_text=True, **kwargs):
    relax_enum_validation = bool(kwargs.pop('relax_enum_validation', False))
    set_cls = kwargs.pop('custom_set_cls', set)
    dict_cls = kwargs.pop('custom_dict_cls', dict)
    if kwargs:
        extra_kwargs = ', '.join(kwargs.keys())
        raise ValueError(
            'Unexpected keyword arguments: ' + extra_kwargs
        )
    json_obj = json
    if is_text:
      json_obj = loads(json)
    if 'count' in json_obj and json_obj['count'] is not None:
      self.count = long(json_obj['count'])
    if 'name' in json_obj and json_obj['name'] is not None:
      self.name = json_obj['name']
    if 'extra' in json_obj and json_obj['extra'] is not None:
      self.extra = json_obj['extra']
    if 'nest' in json_obj and json_obj['nest'] is not None:
      self.nest = MyStructNestedAnnotation()
      self.nest.readFromJson(json_obj['nest'], is_text=False, relax_enum_validation=relax_enum_validation, custom_set_cls=set_cls, custom_dict_cls=dict_cls)

  def __repr__(self):
    L = []
    padding = ' ' * 4
    if self.count is not None:
      value = pprint.pformat(self.count, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    count=%s' % (value))
    if self.name is not None:
      value = pprint.pformat(self.name, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    name=%s' % (value))
    if self.extra is not None:
      value = pprint.pformat(self.extra, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    extra=%s' % (value))
    if self.nest is not None:
      value = pprint.pformat(self.nest, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    nest=%s' % (value))
    return "%s(%s)" % (self.__class__.__name__, "\n" + ",\n".join(L) if L else '')

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

class MyStruct:
  """
  Attributes:
   - major
   - package
   - annotation_with_quote
   - class_
   - annotation_with_trailing_comma
   - empty_annotations
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.major = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.package = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.annotation_with_quote = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.class_ = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.annotation_with_trailing_comma = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.empty_annotations = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('MyStruct')
    if self.major != None:
      oprot.writeFieldBegin('major', TType.I64, 1)
      oprot.writeI64(self.major)
      oprot.writeFieldEnd()
    if self.package != None:
      oprot.writeFieldBegin('package', TType.STRING, 2)
      oprot.writeString(self.package.encode('utf-8')) if UTF8STRINGS and not isinstance(self.package, bytes) else oprot.writeString(self.package)
      oprot.writeFieldEnd()
    if self.annotation_with_quote != None:
      oprot.writeFieldBegin('annotation_with_quote', TType.STRING, 3)
      oprot.writeString(self.annotation_with_quote.encode('utf-8')) if UTF8STRINGS and not isinstance(self.annotation_with_quote, bytes) else oprot.writeString(self.annotation_with_quote)
      oprot.writeFieldEnd()
    if self.class_ != None:
      oprot.writeFieldBegin('class_', TType.STRING, 4)
      oprot.writeString(self.class_.encode('utf-8')) if UTF8STRINGS and not isinstance(self.class_, bytes) else oprot.writeString(self.class_)
      oprot.writeFieldEnd()
    if self.annotation_with_trailing_comma != None:
      oprot.writeFieldBegin('annotation_with_trailing_comma', TType.STRING, 5)
      oprot.writeString(self.annotation_with_trailing_comma.encode('utf-8')) if UTF8STRINGS and not isinstance(self.annotation_with_trailing_comma, bytes) else oprot.writeString(self.annotation_with_trailing_comma)
      oprot.writeFieldEnd()
    if self.empty_annotations != None:
      oprot.writeFieldBegin('empty_annotations', TType.STRING, 6)
      oprot.writeString(self.empty_annotations.encode('utf-8')) if UTF8STRINGS and not isinstance(self.empty_annotations, bytes) else oprot.writeString(self.empty_annotations)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def readFromJson(self, json, is_text=True, **kwargs):
    relax_enum_validation = bool(kwargs.pop('relax_enum_validation', False))
    set_cls = kwargs.pop('custom_set_cls', set)
    dict_cls = kwargs.pop('custom_dict_cls', dict)
    if kwargs:
        extra_kwargs = ', '.join(kwargs.keys())
        raise ValueError(
            'Unexpected keyword arguments: ' + extra_kwargs
        )
    json_obj = json
    if is_text:
      json_obj = loads(json)
    if 'major' in json_obj and json_obj['major'] is not None:
      self.major = long(json_obj['major'])
    if 'package' in json_obj and json_obj['package'] is not None:
      self.package = json_obj['package']
    if 'annotation_with_quote' in json_obj and json_obj['annotation_with_quote'] is not None:
      self.annotation_with_quote = json_obj['annotation_with_quote']
    if 'class_' in json_obj and json_obj['class_'] is not None:
      self.class_ = json_obj['class_']
    if 'annotation_with_trailing_comma' in json_obj and json_obj['annotation_with_trailing_comma'] is not None:
      self.annotation_with_trailing_comma = json_obj['annotation_with_trailing_comma']
    if 'empty_annotations' in json_obj and json_obj['empty_annotations'] is not None:
      self.empty_annotations = json_obj['empty_annotations']

  def __repr__(self):
    L = []
    padding = ' ' * 4
    if self.major is not None:
      value = pprint.pformat(self.major, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    major=%s' % (value))
    if self.package is not None:
      value = pprint.pformat(self.package, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    package=%s' % (value))
    if self.annotation_with_quote is not None:
      value = pprint.pformat(self.annotation_with_quote, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    annotation_with_quote=%s' % (value))
    if self.class_ is not None:
      value = pprint.pformat(self.class_, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    class_=%s' % (value))
    if self.annotation_with_trailing_comma is not None:
      value = pprint.pformat(self.annotation_with_trailing_comma, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    annotation_with_trailing_comma=%s' % (value))
    if self.empty_annotations is not None:
      value = pprint.pformat(self.empty_annotations, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    empty_annotations=%s' % (value))
    return "%s(%s)" % (self.__class__.__name__, "\n" + ",\n".join(L) if L else '')

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

class SecretStruct:
  """
  Attributes:
   - id
   - password
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocolAccelerate) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.id = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.password = iprot.readString().decode('utf-8') if UTF8STRINGS else iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocolAccelerate) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('SecretStruct')
    if self.id != None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.password != None:
      oprot.writeFieldBegin('password', TType.STRING, 2)
      oprot.writeString(self.password.encode('utf-8')) if UTF8STRINGS and not isinstance(self.password, bytes) else oprot.writeString(self.password)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def readFromJson(self, json, is_text=True, **kwargs):
    relax_enum_validation = bool(kwargs.pop('relax_enum_validation', False))
    set_cls = kwargs.pop('custom_set_cls', set)
    dict_cls = kwargs.pop('custom_dict_cls', dict)
    if kwargs:
        extra_kwargs = ', '.join(kwargs.keys())
        raise ValueError(
            'Unexpected keyword arguments: ' + extra_kwargs
        )
    json_obj = json
    if is_text:
      json_obj = loads(json)
    if 'id' in json_obj and json_obj['id'] is not None:
      self.id = long(json_obj['id'])
    if 'password' in json_obj and json_obj['password'] is not None:
      self.password = json_obj['password']

  def __repr__(self):
    L = []
    padding = ' ' * 4
    if self.id is not None:
      value = pprint.pformat(self.id, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    id=%s' % (value))
    if self.password is not None:
      value = pprint.pformat(self.password, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    password=%s' % (value))
    return "%s(%s)" % (self.__class__.__name__, "\n" + ",\n".join(L) if L else '')

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

all_structs.append(MyStructNestedAnnotation)
MyStructNestedAnnotation.thrift_spec = (
  None, # 0
  (1, TType.STRING, 'name', True, None, 2, ), # 1
)

MyStructNestedAnnotation.thrift_struct_annotations = {
}
MyStructNestedAnnotation.thrift_field_annotations = {
}

def MyStructNestedAnnotation__init__(self, name=None,):
  self.name = name

MyStructNestedAnnotation.__init__ = MyStructNestedAnnotation__init__

def MyStructNestedAnnotation__setstate__(self, state):
  state.setdefault('name', None)
  self.__dict__ = state

MyStructNestedAnnotation.__getstate__ = lambda self: self.__dict__.copy()
MyStructNestedAnnotation.__setstate__ = MyStructNestedAnnotation__setstate__

all_structs.append(MyStructAnnotation)
MyStructAnnotation.thrift_spec = (
  None, # 0
  (1, TType.I64, 'count', None, None, 2, ), # 1
  (2, TType.STRING, 'name', True, None, 2, ), # 2
  (3, TType.STRING, 'extra', True, None, 1, ), # 3
  (4, TType.STRUCT, 'nest', [MyStructNestedAnnotation, MyStructNestedAnnotation.thrift_spec, False], None, 2, ), # 4
)

MyStructAnnotation.thrift_struct_annotations = {
}
MyStructAnnotation.thrift_field_annotations = {
}

def MyStructAnnotation__init__(self, count=None, name=None, extra=None, nest=None,):
  self.count = count
  self.name = name
  self.extra = extra
  self.nest = nest

MyStructAnnotation.__init__ = MyStructAnnotation__init__

def MyStructAnnotation__setstate__(self, state):
  state.setdefault('count', None)
  state.setdefault('name', None)
  state.setdefault('extra', None)
  state.setdefault('nest', None)
  self.__dict__ = state

MyStructAnnotation.__getstate__ = lambda self: self.__dict__.copy()
MyStructAnnotation.__setstate__ = MyStructAnnotation__setstate__

all_structs.append(MyStruct)
MyStruct.thrift_spec = (
  None, # 0
  (1, TType.I64, 'major', None, None, 2, ), # 1
  (2, TType.STRING, 'package', True, None, 2, ), # 2
  (3, TType.STRING, 'annotation_with_quote', True, None, 2, ), # 3
  (4, TType.STRING, 'class_', True, None, 2, ), # 4
  (5, TType.STRING, 'annotation_with_trailing_comma', True, None, 2, ), # 5
  (6, TType.STRING, 'empty_annotations', True, None, 2, ), # 6
)

MyStruct.thrift_struct_annotations = {
  "android.generate_builder": """1""",
}
MyStruct.thrift_field_annotations = {
  1: {
    "cpp.name": """majorVer""",
  },
  2: {
    "java.swift.name": """_package""",
  },
  3: {
    "go.tag": """tag:\"somevalue\"""",
  },
  4: {
    "java.swift.name": """class_""",
  },
  5: {
    "custom": """test""",
  },
}

def MyStruct__init__(self, major=None, package=None, annotation_with_quote=None, class_=None, annotation_with_trailing_comma=None, empty_annotations=None,):
  self.major = major
  self.package = package
  self.annotation_with_quote = annotation_with_quote
  self.class_ = class_
  self.annotation_with_trailing_comma = annotation_with_trailing_comma
  self.empty_annotations = empty_annotations

MyStruct.__init__ = MyStruct__init__

def MyStruct__setstate__(self, state):
  state.setdefault('major', None)
  state.setdefault('package', None)
  state.setdefault('annotation_with_quote', None)
  state.setdefault('class_', None)
  state.setdefault('annotation_with_trailing_comma', None)
  state.setdefault('empty_annotations', None)
  self.__dict__ = state

MyStruct.__getstate__ = lambda self: self.__dict__.copy()
MyStruct.__setstate__ = MyStruct__setstate__

all_structs.append(SecretStruct)
SecretStruct.thrift_spec = (
  None, # 0
  (1, TType.I64, 'id', None, None, 2, ), # 1
  (2, TType.STRING, 'password', True, None, 2, ), # 2
)

SecretStruct.thrift_struct_annotations = {
}
SecretStruct.thrift_field_annotations = {
  2: {
    "java.sensitive": """1""",
  },
}

def SecretStruct__init__(self, id=None, password=None,):
  self.id = id
  self.password = password

SecretStruct.__init__ = SecretStruct__init__

def SecretStruct__setstate__(self, state):
  state.setdefault('id', None)
  state.setdefault('password', None)
  self.__dict__ = state

SecretStruct.__getstate__ = lambda self: self.__dict__.copy()
SecretStruct.__setstate__ = SecretStruct__setstate__

fix_spec(all_structs)
del all_structs
