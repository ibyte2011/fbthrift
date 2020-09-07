/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#include <src/gen-py3/module/clients_wrapper.h>

namespace cpp2 {


folly::Future<folly::Unit>
MyServiceClientWrapper::ping(
    apache::thrift::RpcOptions& rpcOptions) {
  folly::Promise<folly::Unit> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServiceAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<folly::Unit>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_ping, channel_);
  client->ping(
    rpcOptions,
    std::move(callback)
  );
  return _future;
}

folly::Future<std::string>
MyServiceClientWrapper::getRandomData(
    apache::thrift::RpcOptions& rpcOptions) {
  folly::Promise<std::string> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServiceAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<std::string>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_getRandomData, channel_);
  client->getRandomData(
    rpcOptions,
    std::move(callback)
  );
  return _future;
}

folly::Future<bool>
MyServiceClientWrapper::hasDataById(
    apache::thrift::RpcOptions& rpcOptions,
    int64_t arg_id) {
  folly::Promise<bool> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServiceAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<bool>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_hasDataById, channel_);
  client->hasDataById(
    rpcOptions,
    std::move(callback),
    arg_id
  );
  return _future;
}

folly::Future<std::string>
MyServiceClientWrapper::getDataById(
    apache::thrift::RpcOptions& rpcOptions,
    int64_t arg_id) {
  folly::Promise<std::string> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServiceAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<std::string>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_getDataById, channel_);
  client->getDataById(
    rpcOptions,
    std::move(callback),
    arg_id
  );
  return _future;
}

folly::Future<folly::Unit>
MyServiceClientWrapper::putDataById(
    apache::thrift::RpcOptions& rpcOptions,
    int64_t arg_id,
    std::string arg_data) {
  folly::Promise<folly::Unit> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServiceAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<folly::Unit>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_putDataById, channel_);
  client->putDataById(
    rpcOptions,
    std::move(callback),
    arg_id,
    arg_data
  );
  return _future;
}

folly::Future<folly::Unit>
MyServiceClientWrapper::lobDataById(
    apache::thrift::RpcOptions& rpcOptions,
    int64_t arg_id,
    std::string arg_data) {
  folly::Promise<folly::Unit> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServiceAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::apache::thrift::OneWayFutureCallback>(
    std::move(_promise), channel_);
  client->lobDataById(
    rpcOptions,
    std::move(callback),
    arg_id,
    arg_data
  );
  return _future;
}

folly::Future<folly::Unit>
MyServiceClientWrapper::doNothing(
    apache::thrift::RpcOptions& rpcOptions) {
  folly::Promise<folly::Unit> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServiceAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<folly::Unit>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_doNothing, channel_);
  client->doNothing(
    rpcOptions,
    std::move(callback)
  );
  return _future;
}

folly::Future<folly::Unit>
MyServicePrioParentClientWrapper::ping(
    apache::thrift::RpcOptions& rpcOptions) {
  folly::Promise<folly::Unit> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServicePrioParentAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<folly::Unit>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_ping, channel_);
  client->ping(
    rpcOptions,
    std::move(callback)
  );
  return _future;
}

folly::Future<folly::Unit>
MyServicePrioParentClientWrapper::pong(
    apache::thrift::RpcOptions& rpcOptions) {
  folly::Promise<folly::Unit> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServicePrioParentAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<folly::Unit>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_pong, channel_);
  client->pong(
    rpcOptions,
    std::move(callback)
  );
  return _future;
}

folly::Future<folly::Unit>
MyServicePrioChildClientWrapper::pang(
    apache::thrift::RpcOptions& rpcOptions) {
  folly::Promise<folly::Unit> _promise;
  auto _future = _promise.getFuture();
  auto* client = static_cast<::cpp2::MyServicePrioChildAsyncClient*>(async_client_.get());
  auto callback = std::make_unique<::thrift::py3::FutureCallback<folly::Unit>>(
    std::move(_promise), rpcOptions, client->recv_wrapped_pang, channel_);
  client->pang(
    rpcOptions,
    std::move(callback)
  );
  return _future;
}

} // namespace cpp2
