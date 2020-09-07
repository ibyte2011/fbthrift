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

#pragma once

#include <memory>

#include <thrift/compiler/ast/t_annotated.h>
#include <thrift/compiler/ast/t_const_value.h>

namespace apache {
namespace thrift {
namespace compiler {

class t_program;

/**
 *  class t_const
 *
 * A const is a constant value defined across languages that has a type and
 * a value. The trick here is that the declared type might not match the type
 * of the value object, since that is not determined until after parsing the
 * whole thing out.
 *
 */
class t_const : public t_annotated {
 public:
  /**
   * Constructor for t_const
   *
   * @param program - An entire thrift program
   * @param type    - A thrift type
   * @param name    - The name of the constant variable
   * @param value   - The constant value
   */
  t_const(
      t_program* program,
      t_type* type,
      std::string name,
      std::unique_ptr<t_const_value> value)
      : program_(program), type_(type), name_(name), value_(std::move(value)) {
    // value->get_owner() is set when rhs is referencing another constant.
    if (value_ && value_->get_owner() == nullptr) {
      value_->set_owner(this);
    }
  }

  /**
   * t_const getters
   */
  t_program* get_program() const {
    return program_;
  }

  t_type* get_type() const {
    return type_;
  }

  std::string get_name() const {
    return name_;
  }

  t_const_value* get_value() const {
    return value_.get();
  }

 private:
  t_program* program_;
  t_type* type_;
  std::string name_;

  std::unique_ptr<t_const_value> value_;
};

} // namespace compiler
} // namespace thrift
} // namespace apache
