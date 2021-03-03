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

#ifndef T_LIST_H
#define T_LIST_H

#include <thrift/compiler/ast/t_container.h>

namespace apache {
namespace thrift {
namespace compiler {

/**
 * A list is a lightweight container type that just wraps another data type.
 *
 */
class t_list : public t_container {
 public:
  explicit t_list(const t_type* elem_type) : elem_type_(elem_type) {}

  const t_type* get_elem_type() const {
    return elem_type_;
  }

  bool is_list() const override {
    return true;
  }

  std::string get_full_name() const override {
    return "list<" + elem_type_->get_full_name() + ">";
  }

  type get_type_value() const override {
    return type::t_list;
  }

 private:
  const t_type* elem_type_;
};

} // namespace compiler
} // namespace thrift
} // namespace apache

#endif
