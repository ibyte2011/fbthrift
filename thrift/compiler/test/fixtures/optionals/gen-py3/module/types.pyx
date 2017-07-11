#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from libcpp.memory cimport shared_ptr, make_shared, unique_ptr, make_unique
from libcpp.string cimport string
from libcpp cimport bool as cbool
from libcpp.iterator cimport inserter as cinserter
from cpython cimport bool as pbool
from libc.stdint cimport int8_t, int16_t, int32_t, int64_t, uint32_t
from cython.operator cimport dereference as deref, preincrement as inc
import thrift.py3.types
cimport thrift.py3.types
cimport thrift.py3.exceptions
from thrift.py3.types import NOTSET
from thrift.py3.types cimport translate_cpp_enum_to_python
cimport thrift.py3.std_libcpp as std_libcpp
from thrift.py3.serializer cimport IOBuf
from thrift.py3.serializer import Protocol
cimport thrift.py3.serializer as serializer
from thrift.py3.serializer import deserialize, serialize

import sys
from collections.abc import Sequence, Set, Mapping, Iterable
from enum import Enum


class Animal(Enum):
    DOG = <int> (Animal__DOG)
    CAT = <int> (Animal__CAT)
    TARANTULA = <int> (Animal__TARANTULA)

cdef cAnimal Animal_to_cpp(value):
    if value == Animal.DOG:
        return Animal__DOG
    elif value == Animal.CAT:
        return Animal__CAT
    elif value == Animal.TARANTULA:
        return Animal__TARANTULA


cdef cColor _Color_defaults = cColor()

cdef class Color(thrift.py3.types.Struct):

    def __init__(
        Color self,
        red=None,
        green=None,
        blue=None,
        alpha=None
    ):
        cdef shared_ptr[cColor] c_inst = make_shared[cColor]()
        inst = self
        if red is not None:
            deref(c_inst).red = red
            deref(c_inst).__isset.red = True

        if green is not None:
            deref(c_inst).green = green
            deref(c_inst).__isset.green = True

        if blue is not None:
            deref(c_inst).blue = blue
            deref(c_inst).__isset.blue = True

        if alpha is not None:
            deref(c_inst).alpha = alpha
            deref(c_inst).__isset.alpha = True

        self._cpp_obj = move_shared(c_inst)

    cdef bytes _serialize(Color self, proto):
        cdef string c_str
        if proto is Protocol.COMPACT:
            serializer.CompactSerialize[cColor](deref(self._cpp_obj.get()), &c_str)
        elif proto is Protocol.BINARY:
            serializer.BinarySerialize[cColor](deref(self._cpp_obj.get()), &c_str)
        elif proto is Protocol.JSON:
            serializer.JSONSerialize[cColor](deref(self._cpp_obj.get()), &c_str)
        return <bytes> c_str

    cdef uint32_t _deserialize(Color self, const IOBuf* buf, proto):
        cdef uint32_t needed
        if proto is Protocol.COMPACT:
            needed = serializer.CompactDeserialize[cColor](buf, deref(self._cpp_obj.get()))
        elif proto is Protocol.BINARY:
            needed = serializer.BinaryDeserialize[cColor](buf, deref(self._cpp_obj.get()))
        elif proto is Protocol.JSON:
            needed = serializer.JSONDeserialize[cColor](buf, deref(self._cpp_obj.get()))
        return needed

    def __reduce__(self):
        return (deserialize, (Color, serialize(self)))

    def __call__(
        Color self,
        red=NOTSET,
        green=NOTSET,
        blue=NOTSET,
        alpha=NOTSET
    ):
        changes = any((
            red is not NOTSET,

            green is not NOTSET,

            blue is not NOTSET,

            alpha is not NOTSET,
        ))

        if not changes:
            return self

        cdef shared_ptr[cColor] c_inst = make_shared[cColor](deref(self._cpp_obj))

        # Convert None's to default value.
        if red is None:
            deref(c_inst).red = _Color_defaults.red
            deref(c_inst).__isset.red = False
        if red is NOTSET:
            red = None
        if green is None:
            deref(c_inst).green = _Color_defaults.green
            deref(c_inst).__isset.green = False
        if green is NOTSET:
            green = None
        if blue is None:
            deref(c_inst).blue = _Color_defaults.blue
            deref(c_inst).__isset.blue = False
        if blue is NOTSET:
            blue = None
        if alpha is None:
            deref(c_inst).alpha = _Color_defaults.alpha
            deref(c_inst).__isset.alpha = False
        if alpha is NOTSET:
            alpha = None

        if red is not None:
            deref(c_inst).red = red
            deref(c_inst).__isset.red = True

        if green is not None:
            deref(c_inst).green = green
            deref(c_inst).__isset.green = True

        if blue is not None:
            deref(c_inst).blue = blue
            deref(c_inst).__isset.blue = True

        if alpha is not None:
            deref(c_inst).alpha = alpha
            deref(c_inst).__isset.alpha = True


        return Color.create(move_shared(c_inst))

    def __iter__(self):
        yield 'red', self.red
        yield 'green', self.green
        yield 'blue', self.blue
        yield 'alpha', self.alpha

    def __bool__(self):
        return deref(self._cpp_obj).__isset.red or deref(self._cpp_obj).__isset.green or deref(self._cpp_obj).__isset.blue or deref(self._cpp_obj).__isset.alpha

    @staticmethod
    cdef create(shared_ptr[cColor] cpp_obj):
        inst = <Color>Color.__new__(Color)
        inst._cpp_obj = cpp_obj
        return inst

    @property
    def red(self):
        if not deref(self._cpp_obj).__isset.red:
            return None

        return self._cpp_obj.get().red

    @property
    def green(self):
        if not deref(self._cpp_obj).__isset.green:
            return None

        return self._cpp_obj.get().green

    @property
    def blue(self):
        if not deref(self._cpp_obj).__isset.blue:
            return None

        return self._cpp_obj.get().blue

    @property
    def alpha(self):
        if not deref(self._cpp_obj).__isset.alpha:
            return None

        return self._cpp_obj.get().alpha


    def __richcmp__(self, other, op):
        cdef int cop = op
        if cop not in (2, 3):
            raise TypeError("unorderable types: {}, {}".format(self, other))
        if not (
                isinstance(self, Color) and
                isinstance(other, Color)):
            if cop == 2:  # different types are never equal
                return False
            else:         # different types are always notequal
                return True

        cdef cColor cself = deref((<Color>self)._cpp_obj)
        cdef cColor cother = deref((<Color>other)._cpp_obj)
        cdef cbool cmp = cself == cother
        if cop == 2:
            return cmp
        return not cmp

    def __hash__(Color self):
        if not self.__hash:
            self.__hash = hash((
            self.red,
            self.green,
            self.blue,
            self.alpha,
            ))
        return self.__hash

    def __repr__(Color self):
        return f'Color(red={repr(self.red)}, green={repr(self.green)}, blue={repr(self.blue)}, alpha={repr(self.alpha)})'


cdef cVehicle _Vehicle_defaults = cVehicle()

cdef class Vehicle(thrift.py3.types.Struct):

    def __init__(
        Vehicle self,
        color=None,
        licensePlate=None,
        description=None,
        name=None,
        hasAC=None
    ):
        cdef shared_ptr[cVehicle] c_inst = make_shared[cVehicle]()
        inst = self
        if color is not None:
            deref(c_inst).color = deref((<Color?> color)._cpp_obj)
            deref(c_inst).__isset.color = True

        if licensePlate is not None:
            deref(c_inst).licensePlate = licensePlate.encode('UTF-8')
            deref(c_inst).__isset.licensePlate = True

        if description is not None:
            deref(c_inst).description = description.encode('UTF-8')
            deref(c_inst).__isset.description = True

        if name is not None:
            deref(c_inst).name = name.encode('UTF-8')
            deref(c_inst).__isset.name = True

        if hasAC is not None:
            deref(c_inst).hasAC = hasAC
            deref(c_inst).__isset.hasAC = True

        self._cpp_obj = move_shared(c_inst)

    cdef bytes _serialize(Vehicle self, proto):
        cdef string c_str
        if proto is Protocol.COMPACT:
            serializer.CompactSerialize[cVehicle](deref(self._cpp_obj.get()), &c_str)
        elif proto is Protocol.BINARY:
            serializer.BinarySerialize[cVehicle](deref(self._cpp_obj.get()), &c_str)
        elif proto is Protocol.JSON:
            serializer.JSONSerialize[cVehicle](deref(self._cpp_obj.get()), &c_str)
        return <bytes> c_str

    cdef uint32_t _deserialize(Vehicle self, const IOBuf* buf, proto):
        cdef uint32_t needed
        if proto is Protocol.COMPACT:
            needed = serializer.CompactDeserialize[cVehicle](buf, deref(self._cpp_obj.get()))
        elif proto is Protocol.BINARY:
            needed = serializer.BinaryDeserialize[cVehicle](buf, deref(self._cpp_obj.get()))
        elif proto is Protocol.JSON:
            needed = serializer.JSONDeserialize[cVehicle](buf, deref(self._cpp_obj.get()))
        return needed

    def __reduce__(self):
        return (deserialize, (Vehicle, serialize(self)))

    def __call__(
        Vehicle self,
        color=NOTSET,
        licensePlate=NOTSET,
        description=NOTSET,
        name=NOTSET,
        hasAC=NOTSET
    ):
        changes = any((
            color is not NOTSET,

            licensePlate is not NOTSET,

            description is not NOTSET,

            name is not NOTSET,

            hasAC is not NOTSET,
        ))

        if not changes:
            return self

        cdef shared_ptr[cVehicle] c_inst = make_shared[cVehicle](deref(self._cpp_obj))

        # Convert None's to default value.
        if color is None:
            deref(c_inst).color = _Vehicle_defaults.color
            deref(c_inst).__isset.color = False
        if color is NOTSET:
            color = None
        if licensePlate is None:
            deref(c_inst).licensePlate = _Vehicle_defaults.licensePlate
            deref(c_inst).__isset.licensePlate = False
        if licensePlate is NOTSET:
            licensePlate = None
        if description is None:
            deref(c_inst).description = _Vehicle_defaults.description
            deref(c_inst).__isset.description = False
        if description is NOTSET:
            description = None
        if name is None:
            deref(c_inst).name = _Vehicle_defaults.name
            deref(c_inst).__isset.name = False
        if name is NOTSET:
            name = None
        if hasAC is None:
            deref(c_inst).hasAC = _Vehicle_defaults.hasAC
            deref(c_inst).__isset.hasAC = False
        if hasAC is NOTSET:
            hasAC = None

        if color is not None:
            deref(c_inst).color = deref((<Color?> color)._cpp_obj)
            deref(c_inst).__isset.color = True

        if licensePlate is not None:
            deref(c_inst).licensePlate = licensePlate.encode('UTF-8')
            deref(c_inst).__isset.licensePlate = True

        if description is not None:
            deref(c_inst).description = description.encode('UTF-8')
            deref(c_inst).__isset.description = True

        if name is not None:
            deref(c_inst).name = name.encode('UTF-8')
            deref(c_inst).__isset.name = True

        if hasAC is not None:
            deref(c_inst).hasAC = hasAC
            deref(c_inst).__isset.hasAC = True


        return Vehicle.create(move_shared(c_inst))

    def __iter__(self):
        yield 'color', self.color
        yield 'licensePlate', self.licensePlate
        yield 'description', self.description
        yield 'name', self.name
        yield 'hasAC', self.hasAC

    def __bool__(self):
        return deref(self._cpp_obj).__isset.color or deref(self._cpp_obj).__isset.licensePlate or deref(self._cpp_obj).__isset.description or deref(self._cpp_obj).__isset.name or deref(self._cpp_obj).__isset.hasAC

    @staticmethod
    cdef create(shared_ptr[cVehicle] cpp_obj):
        inst = <Vehicle>Vehicle.__new__(Vehicle)
        inst._cpp_obj = cpp_obj
        return inst

    @property
    def color(self):
        if not deref(self._cpp_obj).__isset.color:
            return None

        if self.__color is None:
            self.__color = Color.create(make_shared[cColor](deref(self._cpp_obj).color))
        return self.__color

    @property
    def licensePlate(self):
        if not deref(self._cpp_obj).__isset.licensePlate:
            return None

        return self._cpp_obj.get().licensePlate.decode('UTF-8')

    @property
    def description(self):
        if not deref(self._cpp_obj).__isset.description:
            return None

        return self._cpp_obj.get().description.decode('UTF-8')

    @property
    def name(self):
        if not deref(self._cpp_obj).__isset.name:
            return None

        return self._cpp_obj.get().name.decode('UTF-8')

    @property
    def hasAC(self):

        return <pbool> self._cpp_obj.get().hasAC


    def __richcmp__(self, other, op):
        cdef int cop = op
        if cop not in (2, 3):
            raise TypeError("unorderable types: {}, {}".format(self, other))
        if not (
                isinstance(self, Vehicle) and
                isinstance(other, Vehicle)):
            if cop == 2:  # different types are never equal
                return False
            else:         # different types are always notequal
                return True

        cdef cVehicle cself = deref((<Vehicle>self)._cpp_obj)
        cdef cVehicle cother = deref((<Vehicle>other)._cpp_obj)
        cdef cbool cmp = cself == cother
        if cop == 2:
            return cmp
        return not cmp

    def __hash__(Vehicle self):
        if not self.__hash:
            self.__hash = hash((
            self.color,
            self.licensePlate,
            self.description,
            self.name,
            self.hasAC,
            ))
        return self.__hash

    def __repr__(Vehicle self):
        return f'Vehicle(color={repr(self.color)}, licensePlate={repr(self.licensePlate)}, description={repr(self.description)}, name={repr(self.name)}, hasAC={repr(self.hasAC)})'


cdef cPerson _Person_defaults = cPerson()

cdef class Person(thrift.py3.types.Struct):

    def __init__(
        Person self,
        id=None,
        name=None,
        age=None,
        address=None,
        favoriteColor=None,
        friends=None,
        bestFriend=None,
        petNames=None,
        afraidOfAnimal=None,
        vehicles=None
    ):
        cdef shared_ptr[cPerson] c_inst = make_shared[cPerson]()
        inst = self
        if id is not None:
            deref(c_inst).id = id
            deref(c_inst).__isset.id = True

        if name is not None:
            deref(c_inst).name = name.encode('UTF-8')
            deref(c_inst).__isset.name = True

        if age is not None:
            deref(c_inst).age = age
            deref(c_inst).__isset.age = True

        if address is not None:
            deref(c_inst).address = address.encode('UTF-8')
            deref(c_inst).__isset.address = True

        if favoriteColor is not None:
            deref(c_inst).favoriteColor = deref((<Color?> favoriteColor)._cpp_obj)
            deref(c_inst).__isset.favoriteColor = True

        if friends is not None:
            deref(c_inst).friends = <cset[int64_t]>deref(Set__PersonID(friends)._cpp_obj)
            deref(c_inst).__isset.friends = True

        if bestFriend is not None:
            deref(c_inst).bestFriend = bestFriend
            deref(c_inst).__isset.bestFriend = True

        if petNames is not None:
            deref(c_inst).petNames = <cmap[cAnimal,string]>deref(Map__Animal_string(petNames)._cpp_obj)
            deref(c_inst).__isset.petNames = True

        if afraidOfAnimal is not None:
            deref(c_inst).afraidOfAnimal = Animal_to_cpp(afraidOfAnimal)
            deref(c_inst).__isset.afraidOfAnimal = True

        if vehicles is not None:
            deref(c_inst).vehicles = <vector[cVehicle]>deref(List__Vehicle(vehicles)._cpp_obj)
            deref(c_inst).__isset.vehicles = True

        self._cpp_obj = move_shared(c_inst)

    cdef bytes _serialize(Person self, proto):
        cdef string c_str
        if proto is Protocol.COMPACT:
            serializer.CompactSerialize[cPerson](deref(self._cpp_obj.get()), &c_str)
        elif proto is Protocol.BINARY:
            serializer.BinarySerialize[cPerson](deref(self._cpp_obj.get()), &c_str)
        elif proto is Protocol.JSON:
            serializer.JSONSerialize[cPerson](deref(self._cpp_obj.get()), &c_str)
        return <bytes> c_str

    cdef uint32_t _deserialize(Person self, const IOBuf* buf, proto):
        cdef uint32_t needed
        if proto is Protocol.COMPACT:
            needed = serializer.CompactDeserialize[cPerson](buf, deref(self._cpp_obj.get()))
        elif proto is Protocol.BINARY:
            needed = serializer.BinaryDeserialize[cPerson](buf, deref(self._cpp_obj.get()))
        elif proto is Protocol.JSON:
            needed = serializer.JSONDeserialize[cPerson](buf, deref(self._cpp_obj.get()))
        return needed

    def __reduce__(self):
        return (deserialize, (Person, serialize(self)))

    def __call__(
        Person self,
        id=NOTSET,
        name=NOTSET,
        age=NOTSET,
        address=NOTSET,
        favoriteColor=NOTSET,
        friends=NOTSET,
        bestFriend=NOTSET,
        petNames=NOTSET,
        afraidOfAnimal=NOTSET,
        vehicles=NOTSET
    ):
        changes = any((
            id is not NOTSET,

            name is not NOTSET,

            age is not NOTSET,

            address is not NOTSET,

            favoriteColor is not NOTSET,

            friends is not NOTSET,

            bestFriend is not NOTSET,

            petNames is not NOTSET,

            afraidOfAnimal is not NOTSET,

            vehicles is not NOTSET,
        ))

        if not changes:
            return self

        cdef shared_ptr[cPerson] c_inst = make_shared[cPerson](deref(self._cpp_obj))

        # Convert None's to default value.
        if id is None:
            deref(c_inst).id = _Person_defaults.id
            deref(c_inst).__isset.id = False
        if id is NOTSET:
            id = None
        if name is None:
            deref(c_inst).name = _Person_defaults.name
            deref(c_inst).__isset.name = False
        if name is NOTSET:
            name = None
        if age is None:
            deref(c_inst).age = _Person_defaults.age
            deref(c_inst).__isset.age = False
        if age is NOTSET:
            age = None
        if address is None:
            deref(c_inst).address = _Person_defaults.address
            deref(c_inst).__isset.address = False
        if address is NOTSET:
            address = None
        if favoriteColor is None:
            deref(c_inst).favoriteColor = _Person_defaults.favoriteColor
            deref(c_inst).__isset.favoriteColor = False
        if favoriteColor is NOTSET:
            favoriteColor = None
        if friends is None:
            deref(c_inst).friends = _Person_defaults.friends
            deref(c_inst).__isset.friends = False
        if friends is NOTSET:
            friends = None
        if bestFriend is None:
            deref(c_inst).bestFriend = _Person_defaults.bestFriend
            deref(c_inst).__isset.bestFriend = False
        if bestFriend is NOTSET:
            bestFriend = None
        if petNames is None:
            deref(c_inst).petNames = _Person_defaults.petNames
            deref(c_inst).__isset.petNames = False
        if petNames is NOTSET:
            petNames = None
        if afraidOfAnimal is None:
            deref(c_inst).afraidOfAnimal = _Person_defaults.afraidOfAnimal
            deref(c_inst).__isset.afraidOfAnimal = False
        if afraidOfAnimal is NOTSET:
            afraidOfAnimal = None
        if vehicles is None:
            deref(c_inst).vehicles = _Person_defaults.vehicles
            deref(c_inst).__isset.vehicles = False
        if vehicles is NOTSET:
            vehicles = None

        if id is not None:
            deref(c_inst).id = id
            deref(c_inst).__isset.id = True

        if name is not None:
            deref(c_inst).name = name.encode('UTF-8')
            deref(c_inst).__isset.name = True

        if age is not None:
            deref(c_inst).age = age
            deref(c_inst).__isset.age = True

        if address is not None:
            deref(c_inst).address = address.encode('UTF-8')
            deref(c_inst).__isset.address = True

        if favoriteColor is not None:
            deref(c_inst).favoriteColor = deref((<Color?> favoriteColor)._cpp_obj)
            deref(c_inst).__isset.favoriteColor = True

        if friends is not None:
            deref(c_inst).friends = <cset[int64_t]>deref(Set__PersonID(friends)._cpp_obj)
            deref(c_inst).__isset.friends = True

        if bestFriend is not None:
            deref(c_inst).bestFriend = bestFriend
            deref(c_inst).__isset.bestFriend = True

        if petNames is not None:
            deref(c_inst).petNames = <cmap[cAnimal,string]>deref(Map__Animal_string(petNames)._cpp_obj)
            deref(c_inst).__isset.petNames = True

        if afraidOfAnimal is not None:
            deref(c_inst).afraidOfAnimal = Animal_to_cpp(afraidOfAnimal)
            deref(c_inst).__isset.afraidOfAnimal = True

        if vehicles is not None:
            deref(c_inst).vehicles = <vector[cVehicle]>deref(List__Vehicle(vehicles)._cpp_obj)
            deref(c_inst).__isset.vehicles = True


        return Person.create(move_shared(c_inst))

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'age', self.age
        yield 'address', self.address
        yield 'favoriteColor', self.favoriteColor
        yield 'friends', self.friends
        yield 'bestFriend', self.bestFriend
        yield 'petNames', self.petNames
        yield 'afraidOfAnimal', self.afraidOfAnimal
        yield 'vehicles', self.vehicles

    def __bool__(self):
        return deref(self._cpp_obj).__isset.id or deref(self._cpp_obj).__isset.name or deref(self._cpp_obj).__isset.age or deref(self._cpp_obj).__isset.address or deref(self._cpp_obj).__isset.favoriteColor or deref(self._cpp_obj).__isset.friends or deref(self._cpp_obj).__isset.bestFriend or deref(self._cpp_obj).__isset.petNames or deref(self._cpp_obj).__isset.afraidOfAnimal or deref(self._cpp_obj).__isset.vehicles

    @staticmethod
    cdef create(shared_ptr[cPerson] cpp_obj):
        inst = <Person>Person.__new__(Person)
        inst._cpp_obj = cpp_obj
        return inst

    @property
    def id(self):
        if not deref(self._cpp_obj).__isset.id:
            return None

        return self._cpp_obj.get().id

    @property
    def name(self):
        if not deref(self._cpp_obj).__isset.name:
            return None

        return self._cpp_obj.get().name.decode('UTF-8')

    @property
    def age(self):
        if not deref(self._cpp_obj).__isset.age:
            return None

        return self._cpp_obj.get().age

    @property
    def address(self):
        if not deref(self._cpp_obj).__isset.address:
            return None

        return self._cpp_obj.get().address.decode('UTF-8')

    @property
    def favoriteColor(self):
        if not deref(self._cpp_obj).__isset.favoriteColor:
            return None

        if self.__favoriteColor is None:
            self.__favoriteColor = Color.create(make_shared[cColor](deref(self._cpp_obj).favoriteColor))
        return self.__favoriteColor

    @property
    def friends(self):
        if not deref(self._cpp_obj).__isset.friends:
            return None

        if self.__friends is None:
            self.__friends = Set__PersonID.create(make_shared[cset[int64_t]](deref(self._cpp_obj).friends))
        return self.__friends

    @property
    def bestFriend(self):
        if not deref(self._cpp_obj).__isset.bestFriend:
            return None

        return self._cpp_obj.get().bestFriend

    @property
    def petNames(self):
        if not deref(self._cpp_obj).__isset.petNames:
            return None

        if self.__petNames is None:
            self.__petNames = Map__Animal_string.create(make_shared[cmap[cAnimal,string]](deref(self._cpp_obj).petNames))
        return self.__petNames

    @property
    def afraidOfAnimal(self):
        if not deref(self._cpp_obj).__isset.afraidOfAnimal:
            return None

        return translate_cpp_enum_to_python(Animal, <int>deref(self._cpp_obj).afraidOfAnimal)

    @property
    def vehicles(self):
        if not deref(self._cpp_obj).__isset.vehicles:
            return None

        if self.__vehicles is None:
            self.__vehicles = List__Vehicle.create(make_shared[vector[cVehicle]](deref(self._cpp_obj).vehicles))
        return self.__vehicles


    def __richcmp__(self, other, op):
        cdef int cop = op
        if cop not in (2, 3):
            raise TypeError("unorderable types: {}, {}".format(self, other))
        if not (
                isinstance(self, Person) and
                isinstance(other, Person)):
            if cop == 2:  # different types are never equal
                return False
            else:         # different types are always notequal
                return True

        cdef cPerson cself = deref((<Person>self)._cpp_obj)
        cdef cPerson cother = deref((<Person>other)._cpp_obj)
        cdef cbool cmp = cself == cother
        if cop == 2:
            return cmp
        return not cmp

    def __hash__(Person self):
        if not self.__hash:
            self.__hash = hash((
            self.id,
            self.name,
            self.age,
            self.address,
            self.favoriteColor,
            self.friends,
            self.bestFriend,
            self.petNames,
            self.afraidOfAnimal,
            self.vehicles,
            ))
        return self.__hash

    def __repr__(Person self):
        return f'Person(id={repr(self.id)}, name={repr(self.name)}, age={repr(self.age)}, address={repr(self.address)}, favoriteColor={repr(self.favoriteColor)}, friends={repr(self.friends)}, bestFriend={repr(self.bestFriend)}, petNames={repr(self.petNames)}, afraidOfAnimal={repr(self.afraidOfAnimal)}, vehicles={repr(self.vehicles)})'


cdef class Set__PersonID:
    def __init__(self, items=None):
        if isinstance(items, Set__PersonID):
            self._cpp_obj = (<Set__PersonID> items)._cpp_obj
        else:
          self._cpp_obj = make_shared[cset[int64_t]]()
          if items:
              for item in items:
                  deref(self._cpp_obj).insert(item)

    @staticmethod
    cdef create(shared_ptr[cset[int64_t]] c_items):
        inst = <Set__PersonID>Set__PersonID.__new__(Set__PersonID)
        inst._cpp_obj = c_items
        return inst

    def __contains__(self, item):
        if not self:
            return False
        return pbool(deref(self._cpp_obj).count(item))

    def __len__(self):
        return deref(self._cpp_obj).size()

    def __iter__(self):
        if not self:
            raise StopIteration
        for citem in deref(self._cpp_obj):
            yield citem

    def __repr__(self):
        if not self:
            return 'iset()'
        return f'i{{{", ".join(map(repr, self))}}}'

    def __richcmp__(self, other, op):
        cdef int cop = op
        cdef cset[int64_t] cself, cother
        cdef cbool retval
        if (isinstance(self, Set__PersonID) and
                isinstance(other, Set__PersonID)):
            cself = deref((<Set__PersonID> self)._cpp_obj)
            cother = deref((<Set__PersonID> other)._cpp_obj)
            # C level comparisons
            if cop == 0:    # Less Than (strict subset)
                if not cself.size() < cother.size():
                    return False
                for item in cself:
                    if not cother.count(item):
                        return False
                return True
            elif cop == 1:  # Less Than or Equal To  (subset)
                for item in cself:
                    if not cother.count(item):
                        return False
                return True
            elif cop == 2:  # Equivalent
                if cself.size() != cother.size():
                    return False
                for item in cself:
                    if not cother.count(item):
                        return False
                return True
            elif cop == 3:  # Not Equivalent
                for item in cself:
                    if not cother.count(item):
                        return True
                return cself.size() != cother.size()
            elif cop == 4:  # Greater Than (strict superset)
                if not cself.size() > cother.size():
                    return False
                for item in cother:
                    if not cself.count(item):
                        return False
                return True
            elif cop == 5:  # Greater Than or Equal To (superset)
                for item in cother:
                    if not cself.count(item):
                        return False
                return True

        # Python level comparisons
        if cop == 0:
            return Set.__lt__(self, other)
        elif cop == 1:
            return Set.__le__(self, other)
        elif cop == 2:
            return Set.__eq__(self, other)
        elif cop == 3:
            return Set.__ne__(self, other)
        elif cop == 4:
            return Set.__gt__(self, other)
        elif cop == 5:
            return Set.__ge__(self, other)

    def __hash__(self):
        if not self.__hash:
            self.__hash = hash(tuple(self))
        return self.__hash

    def __and__(self, other):
        if not isinstance(self, Set__PersonID):
            self = Set__PersonID(self)
        if not isinstance(other, Set__PersonID):
            other = Set__PersonID(other)

        cdef shared_ptr[cset[int64_t]] shretval = \
            make_shared[cset[int64_t]]()
        for citem in deref((<Set__PersonID> self)._cpp_obj):
            if deref((<Set__PersonID> other)._cpp_obj).count(citem) > 0:
                deref(shretval).insert(citem)
        return Set__PersonID.create(shretval)

    def __sub__(self, other):
        if not isinstance(self, Set__PersonID):
            self = Set__PersonID(self)
        if not isinstance(other, Set__PersonID):
            other = Set__PersonID(other)

        cdef shared_ptr[cset[int64_t]] shretval = \
            make_shared[cset[int64_t]]()
        for citem in deref((<Set__PersonID> self)._cpp_obj):
            if deref((<Set__PersonID> other)._cpp_obj).count(citem) == 0:
                deref(shretval).insert(citem)
        return Set__PersonID.create(shretval)

    def __or__(self, other):
        if not isinstance(self, Set__PersonID):
            self = Set__PersonID(self)
        if not isinstance(other, Set__PersonID):
            other = Set__PersonID(other)

        cdef shared_ptr[cset[int64_t]] shretval = \
            make_shared[cset[int64_t]]()
        for citem in deref((<Set__PersonID> self)._cpp_obj):
                deref(shretval).insert(citem)
        for citem in deref((<Set__PersonID> other)._cpp_obj):
                deref(shretval).insert(citem)
        return Set__PersonID.create(shretval)

    def __xor__(self, other):
        if not isinstance(self, Set__PersonID):
            self = Set__PersonID(self)
        if not isinstance(other, Set__PersonID):
            other = Set__PersonID(other)

        cdef shared_ptr[cset[int64_t]] shretval = \
            make_shared[cset[int64_t]]()
        for citem in deref((<Set__PersonID> self)._cpp_obj):
            if deref((<Set__PersonID> other)._cpp_obj).count(citem) == 0:
                deref(shretval).insert(citem)
        for citem in deref((<Set__PersonID> other)._cpp_obj):
            if deref((<Set__PersonID> self)._cpp_obj).count(citem) == 0:
                deref(shretval).insert(citem)
        return Set__PersonID.create(shretval)

    def isdisjoint(self, other):
        return len(self & other) == 0

    def union(self, other):
        return self | other

    def intersection(self, other):
        return self & other

    def difference(self, other):
        return self - other

    def symmetric_difference(self, other):
        return self ^ other

    def issubset(self, other):
        return self <= other

    def issuperset(self, other):
        return self >= other


Set.register(Set__PersonID)

cdef class Map__Animal_string:
    def __init__(self, items=None):
        if isinstance(items, Map__Animal_string):
            self._cpp_obj = (<Map__Animal_string> items)._cpp_obj
        else:
          self._cpp_obj = make_shared[cmap[cAnimal,string]]()
          if items:
              for key, item in items.items():
                  deref(self._cpp_obj).insert(
                      cpair[cAnimal,string](
                          Animal_to_cpp(key),
                          item.encode('UTF-8')))

    @staticmethod
    cdef create(shared_ptr[cmap[cAnimal,string]] c_items):
        inst = <Map__Animal_string>Map__Animal_string.__new__(Map__Animal_string)
        inst._cpp_obj = c_items
        return inst

    def __getitem__(self, key):
        if not self:
            raise KeyError(f'{key}')
        cdef cAnimal ckey = Animal_to_cpp(key)
        cdef cmap[cAnimal,string].iterator iter = deref(
            self._cpp_obj).find(ckey)
        if iter == deref(self._cpp_obj).end():
            raise KeyError(f'{key}')
        cdef string citem = deref(iter).second
        return bytes(citem).decode('UTF-8')

    def __len__(self):
        return deref(self._cpp_obj).size()

    def __iter__(self):
        if not self:
            raise StopIteration
        cdef cAnimal citem
        for pair in deref(self._cpp_obj):
            citem = pair.first
            yield Animal(<int> citem)

    def __richcmp__(self, other, op):
        cdef int cop = op
        if cop not in (2, 3):
            raise TypeError("unorderable types: {}, {}".format(type(self), type(other)))
        if not (isinstance(self, Mapping) and isinstance(other, Mapping)):
            return cop != 2
        if (len(self) != len(other)):
            return cop != 2

        for key in self:
            if key not in other:
                return cop != 2
            if other[key] != self[key]:
                return cop != 2

        return cop == 2

    def __hash__(self):
        if not self.__hash:
            self.__hash = hash(tuple(self.items()))
        return self.__hash

    def __repr__(self):
        if not self:
            return 'i{}'
        return f'i{{{", ".join(map(lambda i: f"{i[0]}: {i[1]}", self.items()))}}}'



    def __contains__(self, key):
        cdef cAnimal ckey = Animal_to_cpp(key)
        return deref(self._cpp_obj).count(ckey) > 0

    def get(self, key, default=None):
        if not self:
            return default
        cdef cAnimal ckey = Animal_to_cpp(key)
        cdef cmap[cAnimal,string].iterator iter = \
            deref(self._cpp_obj).find(ckey)
        if iter == deref(self._cpp_obj).end():
            return default
        cdef string citem = deref(iter).second
        return bytes(citem).decode('UTF-8')

    def keys(self):
        return self.__iter__()

    def values(self):
        if not self:
            raise StopIteration
        cdef string citem
        for pair in deref(self._cpp_obj):
            citem = pair.second
            yield bytes(citem).decode('UTF-8')

    def items(self):
        if not self:
            raise StopIteration
        cdef cAnimal ckey
        cdef string citem
        for pair in deref(self._cpp_obj):
            ckey = pair.first
            citem = pair.second

            yield (Animal(<int> ckey), bytes(citem).decode('UTF-8'))



Mapping.register(Map__Animal_string)

cdef class List__Vehicle:
    def __init__(self, items=None):
        if isinstance(items, List__Vehicle):
            self._cpp_obj = (<List__Vehicle> items)._cpp_obj
        else:
          self._cpp_obj = make_shared[vector[cVehicle]]()
          if items:
              for item in items:
                  deref(self._cpp_obj).push_back(deref((<Vehicle> item)._cpp_obj))

    @staticmethod
    cdef create(
            shared_ptr[vector[cVehicle]] c_items):
        inst = <List__Vehicle>List__Vehicle.__new__(List__Vehicle)
        inst._cpp_obj = c_items
        return inst

    def __getitem__(self, int index):
        size = len(self)
        # Convert a negative index
        if index < 0:
            index = size - index
        if index >= size:
            raise IndexError('list index out of range')
        # Support negative indexes
        if index < 0:
            index = size - index
        cdef cVehicle citem = (
            deref(self._cpp_obj.get())[index])
        return Vehicle.create(make_shared[cVehicle](citem))

    def __len__(self):
        return deref(self._cpp_obj).size()

    def __richcmp__(self, other, op):
        cdef int cop = op
        if cop not in (2, 3):
            raise TypeError("unorderable types: {}, {}".format(type(self), type(other)))
        if not (isinstance(self, Iterable) and isinstance(other, Iterable)):
            return cop != 2
        if (len(self) != len(other)):
            return cop != 2

        for one, two in zip(self, other):
            if one != two:
                return cop != 2

        return cop == 2

    def __hash__(self):
        if not self.__hash:
            self.__hash = hash(tuple(self))
        return self.__hash

    def __contains__(self, item):
        if not self:
            return False
        cdef cVehicle citem = deref((<Vehicle> item)._cpp_obj)
        cdef vector[cVehicle] vec = deref(
            self._cpp_obj.get())
        return std_libcpp.find(vec.begin(), vec.end(), citem) != vec.end()

    def __iter__(self):
        if not self:
            raise StopIteration
        cdef cVehicle citem
        for citem in deref(self._cpp_obj):
            yield Vehicle.create(make_shared[cVehicle](citem))

    def __repr__(self):
        if not self:
            return 'i[]'
        return f'i[{", ".join(map(repr, self))}]'

    def __reversed__(self):
        if not self:
            raise StopIteration
        cdef cVehicle citem
        cdef vector[cVehicle] vec = deref(
            self._cpp_obj.get())
        cdef vector[cVehicle].reverse_iterator loc = vec.rbegin()
        while loc != vec.rend():
            citem = deref(loc)
            yield Vehicle.create(make_shared[cVehicle](citem))
            inc(loc)

    def index(self, item):
        if not self:
            raise ValueError(f'{item} is not in list')
        cdef cVehicle citem = deref((<Vehicle> item)._cpp_obj)
        cdef vector[cVehicle] vec = deref(self._cpp_obj.get())
        cdef vector[cVehicle].iterator loc = std_libcpp.find(vec.begin(), vec.end(), citem)
        if loc != vec.end():
            return <int64_t> std_libcpp.distance(vec.begin(), loc)
        raise ValueError(f'{item} is not in list')

    def count(self, item):
        if not self:
            return 0
        cdef cVehicle citem = deref((<Vehicle> item)._cpp_obj)
        cdef vector[cVehicle] vec = deref(self._cpp_obj.get())
        return <int64_t> std_libcpp.count(vec.begin(), vec.end(), citem)


Sequence.register(List__Vehicle)

PersonID = int
