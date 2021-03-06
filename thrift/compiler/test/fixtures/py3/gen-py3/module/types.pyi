#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from folly.iobuf import IOBuf as __IOBuf
import thrift.py3.types
import thrift.py3.exceptions
from thrift.py3.types import NOTSET, NOTSETTYPE
from thrift.py3.serializer import Protocol
import typing as _typing

import sys
import itertools


__property__ = property


class AnEnum(thrift.py3.types.Enum):
    NOTSET: AnEnum = ...
    ONE: AnEnum = ...
    TWO: AnEnum = ...
    THREE: AnEnum = ...
    FOUR: AnEnum = ...


class Flags(thrift.py3.types.Flag):
    flag_A: Flags = ...
    flag_B: Flags = ...
    flag_C: Flags = ...
    flag_D: Flags = ...


class SimpleException(thrift.py3.exceptions.Error, _typing.Hashable, _typing.Iterable[_typing.Tuple[str, _typing.Any]]):
    def __init__(
        self, *,
        err_code: _typing.Optional[int]=None
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'SimpleException') -> bool: ...
    def __gt__(self, other: 'SimpleException') -> bool: ...
    def __le__(self, other: 'SimpleException') -> bool: ...
    def __ge__(self, other: 'SimpleException') -> bool: ...

    @__property__
    def err_code(self) -> int: ...


class SimpleStruct(thrift.py3.types.Struct, _typing.Hashable, _typing.Iterable[_typing.Tuple[str, _typing.Any]]):
    def __init__(
        self, *,
        is_on: _typing.Optional[bool]=None,
        tiny_int: _typing.Optional[int]=None,
        small_int: _typing.Optional[int]=None,
        nice_sized_int: _typing.Optional[int]=None,
        big_int: _typing.Optional[int]=None,
        real: _typing.Optional[float]=None,
        smaller_real: _typing.Optional[float]=None
    ) -> None: ...

    def __call__(
        self, *,
        is_on: _typing.Union[bool, NOTSETTYPE, None]=NOTSET,
        tiny_int: _typing.Union[int, NOTSETTYPE, None]=NOTSET,
        small_int: _typing.Union[int, NOTSETTYPE, None]=NOTSET,
        nice_sized_int: _typing.Union[int, NOTSETTYPE, None]=NOTSET,
        big_int: _typing.Union[int, NOTSETTYPE, None]=NOTSET,
        real: _typing.Union[float, NOTSETTYPE, None]=NOTSET,
        smaller_real: _typing.Union[float, NOTSETTYPE, None]=NOTSET
    ) -> SimpleStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['SimpleStruct'], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'SimpleStruct') -> bool: ...
    def __gt__(self, other: 'SimpleStruct') -> bool: ...
    def __le__(self, other: 'SimpleStruct') -> bool: ...
    def __ge__(self, other: 'SimpleStruct') -> bool: ...

    @__property__
    def is_on(self) -> bool: ...
    @__property__
    def tiny_int(self) -> int: ...
    @__property__
    def small_int(self) -> int: ...
    @__property__
    def nice_sized_int(self) -> int: ...
    @__property__
    def big_int(self) -> int: ...
    @__property__
    def real(self) -> float: ...
    @__property__
    def smaller_real(self) -> float: ...


class ComplexStruct(thrift.py3.types.Struct, _typing.Hashable, _typing.Iterable[_typing.Tuple[str, _typing.Any]]):
    def __init__(
        self, *,
        structOne: _typing.Optional['SimpleStruct']=None,
        structTwo: _typing.Optional['SimpleStruct']=None,
        an_integer: _typing.Optional[int]=None,
        name: _typing.Optional[str]=None,
        an_enum: _typing.Optional[AnEnum]=None,
        some_bytes: _typing.Optional[bytes]=None,
        sender: _typing.Optional[str]=None,
        cdef_: _typing.Optional[str]=None,
        bytes_with_cpp_type: _typing.Optional[bytes]=None
    ) -> None: ...

    def __call__(
        self, *,
        structOne: _typing.Union['SimpleStruct', NOTSETTYPE, None]=NOTSET,
        structTwo: _typing.Union['SimpleStruct', NOTSETTYPE, None]=NOTSET,
        an_integer: _typing.Union[int, NOTSETTYPE, None]=NOTSET,
        name: _typing.Union[str, NOTSETTYPE, None]=NOTSET,
        an_enum: _typing.Union[AnEnum, NOTSETTYPE, None]=NOTSET,
        some_bytes: _typing.Union[bytes, NOTSETTYPE, None]=NOTSET,
        sender: _typing.Union[str, NOTSETTYPE, None]=NOTSET,
        cdef_: _typing.Union[str, NOTSETTYPE, None]=NOTSET,
        bytes_with_cpp_type: _typing.Union[bytes, NOTSETTYPE, None]=NOTSET
    ) -> ComplexStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['ComplexStruct'], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'ComplexStruct') -> bool: ...
    def __gt__(self, other: 'ComplexStruct') -> bool: ...
    def __le__(self, other: 'ComplexStruct') -> bool: ...
    def __ge__(self, other: 'ComplexStruct') -> bool: ...

    @__property__
    def structOne(self) -> 'SimpleStruct': ...
    @__property__
    def structTwo(self) -> 'SimpleStruct': ...
    @__property__
    def an_integer(self) -> int: ...
    @__property__
    def name(self) -> str: ...
    @__property__
    def an_enum(self) -> AnEnum: ...
    @__property__
    def some_bytes(self) -> bytes: ...
    @__property__
    def sender(self) -> str: ...
    @__property__
    def cdef_(self) -> str: ...
    @__property__
    def bytes_with_cpp_type(self) -> bytes: ...


_List__i16T = _typing.TypeVar('_List__i16T', bound=_typing.Sequence[int])


class List__i16(_typing.Sequence[int], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[int]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> int: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[int]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> 'List__i16': ...
    def __radd__(self, other: _List__i16T) -> _List__i16T: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


_List__i32T = _typing.TypeVar('_List__i32T', bound=_typing.Sequence[int])


class List__i32(_typing.Sequence[int], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[int]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> int: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[int]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> 'List__i32': ...
    def __radd__(self, other: _List__i32T) -> _List__i32T: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


_List__i64T = _typing.TypeVar('_List__i64T', bound=_typing.Sequence[int])


class List__i64(_typing.Sequence[int], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[int]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> int: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[int]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[int]) -> 'List__i64': ...
    def __radd__(self, other: _List__i64T) -> _List__i64T: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


_List__stringT = _typing.TypeVar('_List__stringT', bound=_typing.Sequence[str])


class List__string(_typing.Sequence[str], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[str]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> str: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[str]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[str]) -> 'List__string': ...
    def __radd__(self, other: _List__stringT) -> _List__stringT: ...
    def __reversed__(self) -> _typing.Iterator[str]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__SimpleStructT = _typing.TypeVar('_List__SimpleStructT', bound=_typing.Sequence['SimpleStruct'])


class List__SimpleStruct(_typing.Sequence['SimpleStruct'], _typing.Hashable):
    def __init__(self, items: _typing.Sequence['SimpleStruct']=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence['SimpleStruct']: ...
    @_typing.overload
    def __getitem__(self, i: int) -> 'SimpleStruct': ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence['SimpleStruct']: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence['SimpleStruct']) -> 'List__SimpleStruct': ...
    def __radd__(self, other: _List__SimpleStructT) -> _List__SimpleStructT: ...
    def __reversed__(self) -> _typing.Iterator['SimpleStruct']: ...
    def __iter__(self) -> _typing.Iterator['SimpleStruct']: ...


class Set__i32(_typing.AbstractSet[int], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.AbstractSet[int]: ...
    def isdisjoint(self, other: _typing.AbstractSet[int]) -> bool: ...
    def union(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def intersection(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def difference(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def symmetric_difference(self, other: _typing.AbstractSet[int]) -> 'Set__i32': ...
    def issubset(self, other: _typing.AbstractSet[int]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[int]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


class Set__string(_typing.AbstractSet[str], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.AbstractSet[str]: ...
    def isdisjoint(self, other: _typing.AbstractSet[str]) -> bool: ...
    def union(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def intersection(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def difference(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def symmetric_difference(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def issubset(self, other: _typing.AbstractSet[str]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[str]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_string(_typing.Mapping[str, str], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Mapping[str, str]: ...
    def __getitem__(self, key: str) -> str: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_SimpleStruct(_typing.Mapping[str, 'SimpleStruct'], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, 'SimpleStruct']=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Mapping[str, 'SimpleStruct']: ...
    def __getitem__(self, key: str) -> 'SimpleStruct': ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_i16(_typing.Mapping[str, int], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Mapping[str, int]: ...
    def __getitem__(self, key: str) -> int: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__List__i32T = _typing.TypeVar('_List__List__i32T', bound=_typing.Sequence[_typing.Sequence[int]])


class List__List__i32(_typing.Sequence[_typing.Sequence[int]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.Sequence[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[_typing.Sequence[int]]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Sequence[int]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Sequence[int]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Sequence[int]]) -> 'List__List__i32': ...
    def __radd__(self, other: _List__List__i32T) -> _List__List__i32T: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Sequence[int]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[int]]: ...


class Map__string_i32(_typing.Mapping[str, int], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, int]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Mapping[str, int]: ...
    def __getitem__(self, key: str) -> int: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_Map__string_i32(_typing.Mapping[str, _typing.Mapping[str, int]], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, _typing.Mapping[str, int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Mapping[str, _typing.Mapping[str, int]]: ...
    def __getitem__(self, key: str) -> _typing.Mapping[str, int]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__Set__stringT = _typing.TypeVar('_List__Set__stringT', bound=_typing.Sequence[_typing.AbstractSet[str]])


class List__Set__string(_typing.Sequence[_typing.AbstractSet[str]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.AbstractSet[str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[_typing.AbstractSet[str]]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.AbstractSet[str]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.AbstractSet[str]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.AbstractSet[str]]) -> 'List__Set__string': ...
    def __radd__(self, other: _List__Set__stringT) -> _List__Set__stringT: ...
    def __reversed__(self) -> _typing.Iterator[_typing.AbstractSet[str]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[str]]: ...


class Map__string_List__SimpleStruct(_typing.Mapping[str, _typing.Sequence['SimpleStruct']], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[str, _typing.Sequence['SimpleStruct']]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Mapping[str, _typing.Sequence['SimpleStruct']]: ...
    def __getitem__(self, key: str) -> _typing.Sequence['SimpleStruct']: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__List__stringT = _typing.TypeVar('_List__List__stringT', bound=_typing.Sequence[_typing.Sequence[str]])


class List__List__string(_typing.Sequence[_typing.Sequence[str]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.Sequence[str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[_typing.Sequence[str]]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Sequence[str]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Sequence[str]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Sequence[str]]) -> 'List__List__string': ...
    def __radd__(self, other: _List__List__stringT) -> _List__List__stringT: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Sequence[str]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Sequence[str]]: ...


_List__Set__i32T = _typing.TypeVar('_List__Set__i32T', bound=_typing.Sequence[_typing.AbstractSet[int]])


class List__Set__i32(_typing.Sequence[_typing.AbstractSet[int]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.AbstractSet[int]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[_typing.AbstractSet[int]]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.AbstractSet[int]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.AbstractSet[int]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.AbstractSet[int]]) -> 'List__Set__i32': ...
    def __radd__(self, other: _List__Set__i32T) -> _List__Set__i32T: ...
    def __reversed__(self) -> _typing.Iterator[_typing.AbstractSet[int]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.AbstractSet[int]]: ...


_List__Map__string_stringT = _typing.TypeVar('_List__Map__string_stringT', bound=_typing.Sequence[_typing.Mapping[str, str]])


class List__Map__string_string(_typing.Sequence[_typing.Mapping[str, str]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.Mapping[str, str]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[_typing.Mapping[str, str]]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Mapping[str, str]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Mapping[str, str]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Mapping[str, str]]) -> 'List__Map__string_string': ...
    def __radd__(self, other: _List__Map__string_stringT) -> _List__Map__string_stringT: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Mapping[str, str]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Mapping[str, str]]: ...


_List__binaryT = _typing.TypeVar('_List__binaryT', bound=_typing.Sequence[bytes])


class List__binary(_typing.Sequence[bytes], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[bytes]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[bytes]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> bytes: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[bytes]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[bytes]) -> 'List__binary': ...
    def __radd__(self, other: _List__binaryT) -> _List__binaryT: ...
    def __reversed__(self) -> _typing.Iterator[bytes]: ...
    def __iter__(self) -> _typing.Iterator[bytes]: ...


class Set__binary(_typing.AbstractSet[bytes], _typing.Hashable):
    def __init__(self, items: _typing.AbstractSet[bytes]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.AbstractSet[bytes]: ...
    def isdisjoint(self, other: _typing.AbstractSet[bytes]) -> bool: ...
    def union(self, other: _typing.AbstractSet[bytes]) -> 'Set__binary': ...
    def intersection(self, other: _typing.AbstractSet[bytes]) -> 'Set__binary': ...
    def difference(self, other: _typing.AbstractSet[bytes]) -> 'Set__binary': ...
    def symmetric_difference(self, other: _typing.AbstractSet[bytes]) -> 'Set__binary': ...
    def issubset(self, other: _typing.AbstractSet[bytes]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[bytes]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[bytes]: ...


_List__AnEnumT = _typing.TypeVar('_List__AnEnumT', bound=_typing.Sequence[AnEnum])


class List__AnEnum(_typing.Sequence[AnEnum], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[AnEnum]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[AnEnum]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> AnEnum: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[AnEnum]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[AnEnum]) -> 'List__AnEnum': ...
    def __radd__(self, other: _List__AnEnumT) -> _List__AnEnumT: ...
    def __reversed__(self) -> _typing.Iterator[AnEnum]: ...
    def __iter__(self) -> _typing.Iterator[AnEnum]: ...


class Map__i32_double(_typing.Mapping[int, float], _typing.Hashable):
    def __init__(self, items: _typing.Mapping[int, float]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Mapping[int, float]: ...
    def __getitem__(self, key: int) -> float: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


_List__Map__i32_doubleT = _typing.TypeVar('_List__Map__i32_doubleT', bound=_typing.Sequence[_typing.Mapping[int, float]])


class List__Map__i32_double(_typing.Sequence[_typing.Mapping[int, float]], _typing.Hashable):
    def __init__(self, items: _typing.Sequence[_typing.Mapping[int, float]]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __copy__(self) -> _typing.Sequence[_typing.Mapping[int, float]]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Mapping[int, float]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Mapping[int, float]]: ...
    def count(self, item: _typing.Any) -> int: ...
    def index(self, item: _typing.Any, start: int = ..., stop: int = ...) -> int: ...
    def __add__(self, other: _typing.Sequence[_typing.Mapping[int, float]]) -> 'List__Map__i32_double': ...
    def __radd__(self, other: _List__Map__i32_doubleT) -> _List__Map__i32_doubleT: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Mapping[int, float]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Mapping[int, float]]: ...


A_BOOL: bool = ...
A_BYTE: int = ...
THE_ANSWER: int = ...
A_NUMBER: int = ...
A_BIG_NUMBER: int = ...
A_REAL_NUMBER: float = ...
A_FAKE_NUMBER: float = ...
A_WORD: str = ...
SOME_BYTES: bytes = ...
A_STRUCT: SimpleStruct = ...
WORD_LIST: List__string = ...
SOME_MAP: List__Map__i32_double = ...
DIGITS: Set__i32 = ...
A_CONST_MAP: Map__string_SimpleStruct = ...
foo_bar = bytes
