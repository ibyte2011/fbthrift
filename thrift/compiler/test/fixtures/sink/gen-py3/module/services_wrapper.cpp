/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#include <src/gen-py3/module/services_wrapper.h>
#include <src/gen-py3/module/services_api.h>
#include <thrift/lib/cpp2/async/AsyncProcessor.h>

namespace cpp2 {

SinkServiceWrapper::SinkServiceWrapper(PyObject *obj, folly::Executor* exc)
  : if_object(obj), executor(exc)
  {
    import_module__services();
  }


std::shared_ptr<apache::thrift::ServerInterface> SinkServiceInterface(PyObject *if_object, folly::Executor *exc) {
  return std::make_shared<SinkServiceWrapper>(if_object, exc);
}
} // namespace cpp2
