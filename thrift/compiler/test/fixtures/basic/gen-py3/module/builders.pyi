#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import typing as _typing

import folly.iobuf as __iobuf
import thrift.py3.builder


import module.types as _module_types


class MyStruct_Builder(thrift.py3.builder.StructBuilder):
    MyIntField: _typing.Optional[int]
    MyStringField: _typing.Optional[str]
    MyDataField: _typing.Any
    myEnum: _typing.Optional[_module_types.MyEnum]

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...


class MyDataItem_Builder(thrift.py3.builder.StructBuilder):

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...


class MyUnion_Builder(thrift.py3.builder.StructBuilder):
    myEnum: _typing.Optional[_module_types.MyEnum]
    myStruct: _typing.Any
    myDataItem: _typing.Any

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...


