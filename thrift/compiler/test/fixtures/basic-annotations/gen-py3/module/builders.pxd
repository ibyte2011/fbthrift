#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
from cpython cimport bool as pbool, int as pint, float as pfloat

cimport folly.iobuf as __iobuf

cimport thrift.py3.builder


cimport module.types as _module_types

cdef class MyStructNestedAnnotation_Builder(thrift.py3.builder.StructBuilder):
    cdef public str name


cdef class MyStructAnnotation_Builder(thrift.py3.builder.StructBuilder):
    cdef public pint count
    cdef public str name
    cdef public str extra
    cdef public object nest


cdef class MyStruct_Builder(thrift.py3.builder.StructBuilder):
    cdef public pint major
    cdef public str package
    cdef public str annotation_with_quote
    cdef public str class_
    cdef public str annotation_with_trailing_comma
    cdef public str empty_annotations


cdef class SecretStruct_Builder(thrift.py3.builder.StructBuilder):
    cdef public pint id
    cdef public str password


