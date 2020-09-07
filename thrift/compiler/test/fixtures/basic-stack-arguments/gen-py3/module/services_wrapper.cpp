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

MyServiceWrapper::MyServiceWrapper(PyObject *obj, folly::Executor* exc)
  : if_object(obj), executor(exc)
  {
    import_module__services();
  }


void MyServiceWrapper::async_tm_hasDataById(
  std::unique_ptr<apache::thrift::HandlerCallback<bool>> callback
    , int64_t id
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<bool>();
        call_cy_MyService_hasDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<bool>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
void MyServiceWrapper::async_tm_getDataById(
  std::unique_ptr<apache::thrift::HandlerCallback<std::string>> callback
    , int64_t id
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<std::string>();
        call_cy_MyService_getDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<std::string>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
void MyServiceWrapper::async_tm_putDataById(
  std::unique_ptr<apache::thrift::HandlerCallback<void>> callback
    , int64_t id
    , const std::string& data
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id,
data = std::move(data)    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<folly::Unit>();
        call_cy_MyService_putDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id,
            std::move(data)        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<folly::Unit>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
void MyServiceWrapper::async_tm_lobDataById(
  std::unique_ptr<apache::thrift::HandlerCallbackBase> callback
    , int64_t id
    , const std::string& data
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id,
data = std::move(data)    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<folly::Unit>();
        call_cy_MyService_lobDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id,
            std::move(data)        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<folly::Unit>&& t) {
          (void)t;
          
        });
    });
}
std::shared_ptr<apache::thrift::ServerInterface> MyServiceInterface(PyObject *if_object, folly::Executor *exc) {
  return std::make_shared<MyServiceWrapper>(if_object, exc);
}


MyServiceFastWrapper::MyServiceFastWrapper(PyObject *obj, folly::Executor* exc)
  : if_object(obj), executor(exc)
  {
    import_module__services();
  }


void MyServiceFastWrapper::async_eb_hasDataById(
  std::unique_ptr<apache::thrift::HandlerCallback<bool>> callback
    , int64_t id
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<bool>();
        call_cy_MyServiceFast_hasDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<bool>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
void MyServiceFastWrapper::async_eb_getDataById(
  std::unique_ptr<apache::thrift::HandlerCallback<std::string>> callback
    , int64_t id
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<std::string>();
        call_cy_MyServiceFast_getDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<std::string>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
void MyServiceFastWrapper::async_eb_putDataById(
  std::unique_ptr<apache::thrift::HandlerCallback<void>> callback
    , int64_t id
    , const std::string& data
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id,
data = std::move(data)    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<folly::Unit>();
        call_cy_MyServiceFast_putDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id,
            std::move(data)        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<folly::Unit>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
void MyServiceFastWrapper::async_eb_lobDataById(
  std::unique_ptr<apache::thrift::HandlerCallbackBase> callback
    , int64_t id
    , const std::string& data
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
id,
data = std::move(data)    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<folly::Unit>();
        call_cy_MyServiceFast_lobDataById(
            this->if_object,
            ctx,
            std::move(promise),
            id,
            std::move(data)        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<folly::Unit>&& t) {
          (void)t;
          
        });
    });
}
std::shared_ptr<apache::thrift::ServerInterface> MyServiceFastInterface(PyObject *if_object, folly::Executor *exc) {
  return std::make_shared<MyServiceFastWrapper>(if_object, exc);
}


DbMixedStackArgumentsWrapper::DbMixedStackArgumentsWrapper(PyObject *obj, folly::Executor* exc)
  : if_object(obj), executor(exc)
  {
    import_module__services();
  }


void DbMixedStackArgumentsWrapper::async_tm_getDataByKey0(
  std::unique_ptr<apache::thrift::HandlerCallback<std::unique_ptr<std::string>>> callback
    , std::unique_ptr<std::string> key
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
key = std::move(key)    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<std::unique_ptr<std::string>>();
        call_cy_DbMixedStackArguments_getDataByKey0(
            this->if_object,
            ctx,
            std::move(promise),
            std::move(key)        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<std::unique_ptr<std::string>>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
void DbMixedStackArgumentsWrapper::async_tm_getDataByKey1(
  std::unique_ptr<apache::thrift::HandlerCallback<std::string>> callback
    , const std::string& key
) {
  auto ctx = callback->getConnectionContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
key = std::move(key)    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<std::string>();
        call_cy_DbMixedStackArguments_getDataByKey1(
            this->if_object,
            ctx,
            std::move(promise),
            std::move(key)        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<std::string>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
std::shared_ptr<apache::thrift::ServerInterface> DbMixedStackArgumentsInterface(PyObject *if_object, folly::Executor *exc) {
  return std::make_shared<DbMixedStackArgumentsWrapper>(if_object, exc);
}
} // namespace cpp2
