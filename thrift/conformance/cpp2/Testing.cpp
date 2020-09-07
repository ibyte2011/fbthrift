/*
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <thrift/conformance/cpp2/Testing.h>

#include <folly/lang/Exception.h>
#include <gtest/gtest.h>

namespace apache::thrift::conformance {

const Protocol Number1Serializer::kProtocol = createProtocol("Number1");
const Protocol kFollyToStringProtocol = createProtocol("FollyToString");

void MultiSerializer::encode(any_ref value, folly::io::QueueAppender&& appender)
    const {
  if (value.type() == typeid(int)) {
    ++intEncCount;
    FollyToStringSerializer<int>().encode(value, std::move(appender));
  } else if (value.type() == typeid(double)) {
    ++dblEncCount;
    FollyToStringSerializer<double>().encode(value, std::move(appender));
  } else {
    folly::throw_exception<std::bad_any_cast>();
  }
}

void MultiSerializer::decode(
    const std::type_info& typeInfo,
    folly::io::Cursor& cursor,
    any_ref value) const {
  if (value.type() == typeid(std::any)) {
    // It is being decoded into an any.
    ++anyDecCount;
  }
  if (typeInfo == typeid(int)) {
    ++intDecCount;
    FollyToStringSerializer<int>().decode(typeInfo, cursor, value);
  } else if (typeInfo == typeid(double)) {
    ++dblDecCount;
    FollyToStringSerializer<double>().decode(typeInfo, cursor, value);
  } else {
    folly::throw_exception<std::bad_any_cast>();
  }
}

void MultiSerializer::checkAndResetInt(size_t enc, size_t dec) const {
  EXPECT_EQ(intEncCount, enc);
  EXPECT_EQ(intDecCount, dec);
  intEncCount = 0;
  intDecCount = 0;
}
void MultiSerializer::checkAndResetDbl(size_t enc, size_t dec) const {
  EXPECT_EQ(dblEncCount, enc);
  EXPECT_EQ(dblDecCount, dec);
  dblEncCount = 0;
  dblDecCount = 0;
}
void MultiSerializer::checkAndResetAny(size_t dec) const {
  EXPECT_EQ(anyDecCount, dec);
  anyDecCount = 0;
}
void MultiSerializer::checkAndResetAll() const {
  checkAndResetInt(0, 0);
  checkAndResetDbl(0, 0);
  checkAndResetAny(0);
}
void MultiSerializer::checkAnyDec() const {
  checkAndResetAny(1);
  checkAndResetAll();
}
void MultiSerializer::checkIntEnc() const {
  checkAndResetInt(1, 0);
  checkAndResetAll();
}
void MultiSerializer::checkIntDec() const {
  checkAndResetInt(0, 1);
  checkAndResetAll();
}
void MultiSerializer::checkDblEnc() const {
  checkAndResetDbl(1, 0);
  checkAndResetAll();
}
void MultiSerializer::checkDblDec() const {
  checkAndResetDbl(0, 1);
  checkAndResetAll();
}
void MultiSerializer::checkAnyIntDec() const {
  checkAndResetAny(1);
  checkAndResetInt(0, 1);
  checkAndResetAll();
}
void MultiSerializer::checkAnyDblDec() const {
  checkAndResetAny(1);
  checkAndResetDbl(0, 1);
  checkAndResetAll();
}

} // namespace apache::thrift::conformance
