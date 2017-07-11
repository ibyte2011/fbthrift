#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libcpp.string cimport string
from libcpp cimport bool as cbool
from cpython cimport bool as pbool
from libc.stdint cimport int8_t, int16_t, int32_t, int64_t
from libcpp.memory cimport shared_ptr, unique_ptr
from libcpp.vector cimport vector
from libcpp.set cimport set as cset
from libcpp.map cimport map as cmap, pair as cpair
from libcpp.unordered_set cimport unordered_set as cuset
from libcpp.unordered_map cimport unordered_map as cumap
from thrift.py3.exceptions cimport cTException, Error as __Error
cimport thrift.py3.types


cdef extern from "src/gen-cpp2/module_types.h" namespace "py3::simple":
    cdef cppclass cAnEnum "py3::simple::AnEnum":
        bint operator==(cAnEnum&)
    cAnEnum AnEnum__ONE "py3::simple::AnEnum::ONE"
    cAnEnum AnEnum__TWO "py3::simple::AnEnum::TWO"
    cAnEnum AnEnum__THREE "py3::simple::AnEnum::THREE"
    cAnEnum AnEnum__FOUR "py3::simple::AnEnum::FOUR"

cdef cAnEnum AnEnum_to_cpp(value)

cdef extern from "src/gen-cpp2/module_types_custom_protocol.h" namespace "py3::simple":
    cdef cppclass cSimpleException__isset "py3::simple::SimpleException::__isset":
        bint err_code

    # Forward Declaration
    cdef cppclass cSimpleException "py3::simple::SimpleException"(cTException)

    cdef cppclass cSimpleException "py3::simple::SimpleException"(cTException):
        cSimpleException() except +
        cSimpleException(const cSimpleException&) except +
        bint operator==(cSimpleException&)
        int16_t err_code
        cSimpleException__isset __isset

    cdef cppclass cSimpleStruct__isset "py3::simple::SimpleStruct::__isset":
        bint is_on
        bint tiny_int
        bint small_int
        bint nice_sized_int
        bint big_int
        bint real
        bint smaller_real

    # Forward Declaration
    cdef cppclass cSimpleStruct "py3::simple::SimpleStruct"

    cdef cppclass cSimpleStruct "py3::simple::SimpleStruct":
        cSimpleStruct() except +
        cSimpleStruct(const cSimpleStruct&) except +
        bint operator==(cSimpleStruct&)
        cbool is_on
        int8_t tiny_int
        int16_t small_int
        int32_t nice_sized_int
        int64_t big_int
        double real
        float smaller_real
        cSimpleStruct__isset __isset

    cdef cppclass cComplexStruct__isset "py3::simple::ComplexStruct::__isset":
        bint structOne
        bint structTwo
        bint an_integer
        bint name
        bint an_enum
        bint some_bytes

    # Forward Declaration
    cdef cppclass cComplexStruct "py3::simple::ComplexStruct"

    cdef cppclass cComplexStruct "py3::simple::ComplexStruct":
        cComplexStruct() except +
        cComplexStruct(const cComplexStruct&) except +
        bint operator==(cComplexStruct&)
        cSimpleStruct structOne
        cSimpleStruct structTwo
        int32_t an_integer
        string name
        cAnEnum an_enum
        string some_bytes
        cComplexStruct__isset __isset


cdef extern from "<utility>" namespace "std" nogil:
    cdef shared_ptr[cSimpleException] move(unique_ptr[cSimpleException])
    cdef shared_ptr[cSimpleException] move_shared "std::move"(shared_ptr[cSimpleException])
    cdef shared_ptr[cSimpleStruct] move(unique_ptr[cSimpleStruct])
    cdef shared_ptr[cSimpleStruct] move_shared "std::move"(shared_ptr[cSimpleStruct])
    cdef shared_ptr[cComplexStruct] move(unique_ptr[cComplexStruct])
    cdef shared_ptr[cComplexStruct] move_shared "std::move"(shared_ptr[cComplexStruct])

# Forward Definition of the cython struct
cdef class SimpleException(__Error)

cdef class SimpleException(__Error):
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cSimpleException] _cpp_obj

    @staticmethod
    cdef create(shared_ptr[cSimpleException])

# Forward Definition of the cython struct
cdef class SimpleStruct(thrift.py3.types.Struct)

cdef class SimpleStruct(thrift.py3.types.Struct):
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cSimpleStruct] _cpp_obj

    @staticmethod
    cdef create(shared_ptr[cSimpleStruct])

# Forward Definition of the cython struct
cdef class ComplexStruct(thrift.py3.types.Struct)

cdef class ComplexStruct(thrift.py3.types.Struct):
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cComplexStruct] _cpp_obj
    cdef SimpleStruct __structOne
    cdef SimpleStruct __structTwo

    @staticmethod
    cdef create(shared_ptr[cComplexStruct])


cdef class List__i16:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[int16_t]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[int16_t]])

cdef class List__i32:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[int32_t]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[int32_t]])

cdef class List__i64:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[int64_t]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[int64_t]])

cdef class List__string:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[string]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[string]])

cdef class List__SimpleStruct:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[cSimpleStruct]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[cSimpleStruct]])

cdef class Set__i32:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cset[int32_t]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cset[int32_t]])

cdef class Set__string:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cset[string]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cset[string]])

cdef class Map__string_string:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cmap[string,string]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cmap[string,string]])

cdef class Map__string_SimpleStruct:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cmap[string,cSimpleStruct]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cmap[string,cSimpleStruct]])

cdef class Map__string_i16:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cmap[string,int16_t]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cmap[string,int16_t]])

cdef class List__List__i32:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[vector[int32_t]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[vector[int32_t]]])

cdef class Map__string_i32:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cmap[string,int32_t]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cmap[string,int32_t]])

cdef class Map__string_Map__string_i32:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cmap[string,cmap[string,int32_t]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cmap[string,cmap[string,int32_t]]])

cdef class List__Set__string:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[cset[string]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[cset[string]]])

cdef class Map__string_List__SimpleStruct:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cmap[string,vector[cSimpleStruct]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cmap[string,vector[cSimpleStruct]]])

cdef class List__List__string:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[vector[string]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[vector[string]]])

cdef class List__Set__i32:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[cset[int32_t]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[cset[int32_t]]])

cdef class List__Map__string_string:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[cmap[string,string]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[cmap[string,string]]])

cdef class List__binary:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[string]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[string]])

cdef class Set__binary:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cset[string]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cset[string]])

cdef class List__AnEnum:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[cAnEnum]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[cAnEnum]])

cdef class Map__i32_double:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[cmap[int32_t,double]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[cmap[int32_t,double]])

cdef class List__Map__i32_double:
    cdef object __hash
    cdef object __weakref__
    cdef shared_ptr[vector[cmap[int32_t,double]]] _cpp_obj
    @staticmethod
    cdef create(shared_ptr[vector[cmap[int32_t,double]]])

cdef extern from "<utility>" namespace "std" nogil:
    cdef shared_ptr[vector[int16_t]] move(unique_ptr[vector[int16_t]])
    cdef shared_ptr[vector[int32_t]] move(unique_ptr[vector[int32_t]])
    cdef shared_ptr[vector[int64_t]] move(unique_ptr[vector[int64_t]])
    cdef shared_ptr[vector[string]] move(unique_ptr[vector[string]])
    cdef shared_ptr[vector[cSimpleStruct]] move(unique_ptr[vector[cSimpleStruct]])
    cdef shared_ptr[cset[int32_t]] move(unique_ptr[cset[int32_t]])
    cdef shared_ptr[cset[string]] move(unique_ptr[cset[string]])
    cdef shared_ptr[cmap[string,string]] move(unique_ptr[cmap[string,string]])
    cdef shared_ptr[cmap[string,cSimpleStruct]] move(unique_ptr[cmap[string,cSimpleStruct]])
    cdef shared_ptr[cmap[string,int16_t]] move(unique_ptr[cmap[string,int16_t]])
    cdef shared_ptr[vector[vector[int32_t]]] move(unique_ptr[vector[vector[int32_t]]])
    cdef shared_ptr[cmap[string,int32_t]] move(unique_ptr[cmap[string,int32_t]])
    cdef shared_ptr[cmap[string,cmap[string,int32_t]]] move(unique_ptr[cmap[string,cmap[string,int32_t]]])
    cdef shared_ptr[vector[cset[string]]] move(unique_ptr[vector[cset[string]]])
    cdef shared_ptr[cmap[string,vector[cSimpleStruct]]] move(unique_ptr[cmap[string,vector[cSimpleStruct]]])
    cdef shared_ptr[vector[vector[string]]] move(unique_ptr[vector[vector[string]]])
    cdef shared_ptr[vector[cset[int32_t]]] move(unique_ptr[vector[cset[int32_t]]])
    cdef shared_ptr[vector[cmap[string,string]]] move(unique_ptr[vector[cmap[string,string]]])
    cdef shared_ptr[vector[cAnEnum]] move(unique_ptr[vector[cAnEnum]])
    cdef shared_ptr[cmap[int32_t,double]] move(unique_ptr[cmap[int32_t,double]])
    cdef shared_ptr[vector[cmap[int32_t,double]]] move(unique_ptr[vector[cmap[int32_t,double]]])

cdef extern from "src/gen-cpp2/module_constants.h" namespace "py3::simple":
    cdef cbool cA_BOOL "py3::simple::module_constants::A_BOOL"
    cdef int8_t cA_BYTE "py3::simple::module_constants::A_BYTE"
    cdef int16_t cTHE_ANSWER "py3::simple::module_constants::THE_ANSWER"
    cdef int32_t cA_NUMBER "py3::simple::module_constants::A_NUMBER"
    cdef int64_t cA_BIG_NUMBER "py3::simple::module_constants::A_BIG_NUMBER"
    cdef double cA_REAL_NUMBER "py3::simple::module_constants::A_REAL_NUMBER"
    cdef double cA_FAKE_NUMBER "py3::simple::module_constants::A_FAKE_NUMBER"
    cdef const char* cA_WORD "py3::simple::module_constants::A_WORD"()
    cdef string cSOME_BYTES "py3::simple::module_constants::SOME_BYTES"()
    cdef cSimpleStruct cA_STRUCT "py3::simple::module_constants::A_STRUCT"()
    cdef vector[string] cWORD_LIST "py3::simple::module_constants::WORD_LIST"()
    cdef vector[cmap[int32_t,double]] cSOME_MAP "py3::simple::module_constants::SOME_MAP"()
    cdef cset[int32_t] cDIGITS "py3::simple::module_constants::DIGITS"()
    cdef cmap[string,cSimpleStruct] cA_CONST_MAP "py3::simple::module_constants::A_CONST_MAP"()
