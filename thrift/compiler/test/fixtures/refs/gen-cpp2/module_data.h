/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <thrift/lib/cpp2/gen/module_data_h.h>

#include "thrift/compiler/test/fixtures/refs/gen-cpp2/module_types.h"

namespace apache { namespace thrift {

template <> struct TEnumDataStorage<::cpp2::TypedEnum> {
  using type = ::cpp2::TypedEnum;
  static constexpr const std::size_t size = 2;
  static constexpr const std::array<type, size> values = {{
    type::VAL1,
    type::VAL2,
  }};
  static constexpr const std::array<folly::StringPiece, size> names = {{
    "VAL1",
    "VAL2",
  }};
};

template <> struct TEnumDataStorage<::cpp2::MyUnion::Type> {
  using type = ::cpp2::MyUnion::Type;
  static constexpr const std::size_t size = 2;
  static constexpr const std::array<type, size> values = {{
    type::anInteger,
    type::aString,
  }};
  static constexpr const std::array<folly::StringPiece, size> names = {{
    "anInteger",
    "aString",
  }};
};

}} // apache::thrift
