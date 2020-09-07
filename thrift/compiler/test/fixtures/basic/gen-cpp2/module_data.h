/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <thrift/lib/cpp2/gen/module_data_h.h>

#include "thrift/compiler/test/fixtures/basic/gen-cpp2/module_types.h"

namespace apache { namespace thrift {

template <> struct TEnumDataStorage<::cpp2::MyEnum> {
  using type = ::cpp2::MyEnum;
  static constexpr const std::size_t size = 2;
  static constexpr const std::array<type, size> values = {{
    type::MyValue1,
    type::MyValue2,
  }};
  static constexpr const std::array<folly::StringPiece, size> names = {{
    "MyValue1",
    "MyValue2",
  }};
};

template <> struct TEnumDataStorage<::cpp2::MyUnion::Type> {
  using type = ::cpp2::MyUnion::Type;
  static constexpr const std::size_t size = 3;
  static constexpr const std::array<type, size> values = {{
    type::myEnum,
    type::myStruct,
    type::myDataItem,
  }};
  static constexpr const std::array<folly::StringPiece, size> names = {{
    "myEnum",
    "myStruct",
    "myDataItem",
  }};
};

}} // apache::thrift
