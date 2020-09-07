#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from cpython.ref cimport PyObject
from libc.stdint cimport (
    int8_t as cint8_t,
    int16_t as cint16_t,
    int32_t as cint32_t,
    int64_t as cint64_t,
)
from libcpp cimport bool as cbool
from libcpp.map cimport map as cmap, pair as cpair
from libcpp.memory cimport shared_ptr, unique_ptr
from libcpp.set cimport set as cset
from libcpp.string cimport string
from libcpp.vector cimport vector

from folly cimport cFollyFuture, cFollyTry, cFollyUnit
cimport folly.iobuf as __iobuf
from thrift.py3.common cimport cRpcOptions

cimport module.types as _module_types
from thrift.py3.stream cimport cResponseAndClientBufferedStream, cClientBufferedStream


cdef extern from "src/gen-cpp2/PubSubStreamingService.h" namespace "::cpp2":
  cdef cppclass cPubSubStreamingServiceAsyncClient "::cpp2::PubSubStreamingServiceAsyncClient":
      pass

cdef extern from "<utility>" namespace "std":
  cdef unique_ptr[cPubSubStreamingServiceClientWrapper] move(unique_ptr[cPubSubStreamingServiceClientWrapper])

cdef extern from "thrift/lib/cpp/TProcessorEventHandler.h" namespace "::apache::thrift":
  cdef cppclass cTProcessorEventHandler "apache::thrift::TProcessorEventHandler":
    pass

cdef extern from "src/gen-py3/module/clients_wrapper.h" namespace "::cpp2":
  cdef cppclass cPubSubStreamingServiceClientWrapper "::cpp2::PubSubStreamingServiceClientWrapper":
    void setPersistentHeader(const string& key, const string& value)
    void addEventHandler(const shared_ptr[cTProcessorEventHandler]& handler)

    cFollyFuture[cClientBufferedStream[cint32_t]] returnstream(cRpcOptions, 
      cint32_t arg_i32_from,
      cint32_t arg_i32_to,)
    cFollyFuture[cClientBufferedStream[cint32_t]] streamthrows(cRpcOptions, 
      cint32_t arg_foo,)
    cFollyFuture[cClientBufferedStream[cint32_t]] boththrows(cRpcOptions, 
      cint32_t arg_foo,)
    cFollyFuture[cResponseAndClientBufferedStream[cint32_t,cint32_t]] responseandstreamthrows(cRpcOptions, 
      cint32_t arg_foo,)

