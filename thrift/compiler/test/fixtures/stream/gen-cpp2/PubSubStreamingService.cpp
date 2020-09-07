/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "thrift/compiler/test/fixtures/stream/gen-cpp2/PubSubStreamingService.h"
#include "thrift/compiler/test/fixtures/stream/gen-cpp2/PubSubStreamingService.tcc"
#include "thrift/compiler/test/fixtures/stream/gen-cpp2/module_metadata.h"
#include <thrift/lib/cpp2/gen/service_cpp.h>

namespace cpp2 {
std::unique_ptr<apache::thrift::AsyncProcessor> PubSubStreamingServiceSvIf::getProcessor() {
  return std::make_unique<PubSubStreamingServiceAsyncProcessor>(this);
}


apache::thrift::ServerStream<int32_t> PubSubStreamingServiceSvIf::returnstream(int32_t /*i32_from*/, int32_t /*i32_to*/) {
  apache::thrift::detail::si::throw_app_exn_unimplemented("returnstream");
}

folly::SemiFuture<apache::thrift::ServerStream<int32_t>> PubSubStreamingServiceSvIf::semifuture_returnstream(int32_t i32_from, int32_t i32_to) {
  return apache::thrift::detail::si::semifuture([&] {
    return returnstream(i32_from, i32_to);
  });
}

folly::Future<apache::thrift::ServerStream<int32_t>> PubSubStreamingServiceSvIf::future_returnstream(int32_t i32_from, int32_t i32_to) {
  return apache::thrift::detail::si::future(semifuture_returnstream(i32_from, i32_to), getThreadManager());
}


void PubSubStreamingServiceSvIf::async_tm_returnstream(std::unique_ptr<apache::thrift::HandlerCallback<apache::thrift::ServerStream<int32_t>>> callback, int32_t i32_from, int32_t i32_to) {
  apache::thrift::detail::si::async_tm(this, std::move(callback), [&] {
    return future_returnstream(i32_from, i32_to);
  });
}

apache::thrift::ServerStream<int32_t> PubSubStreamingServiceSvIf::streamthrows(int32_t /*foo*/) {
  apache::thrift::detail::si::throw_app_exn_unimplemented("streamthrows");
}

folly::SemiFuture<apache::thrift::ServerStream<int32_t>> PubSubStreamingServiceSvIf::semifuture_streamthrows(int32_t foo) {
  return apache::thrift::detail::si::semifuture([&] {
    return streamthrows(foo);
  });
}

folly::Future<apache::thrift::ServerStream<int32_t>> PubSubStreamingServiceSvIf::future_streamthrows(int32_t foo) {
  return apache::thrift::detail::si::future(semifuture_streamthrows(foo), getThreadManager());
}


void PubSubStreamingServiceSvIf::async_tm_streamthrows(std::unique_ptr<apache::thrift::HandlerCallback<apache::thrift::ServerStream<int32_t>>> callback, int32_t foo) {
  apache::thrift::detail::si::async_tm(this, std::move(callback), [&] {
    return future_streamthrows(foo);
  });
}

apache::thrift::ServerStream<int32_t> PubSubStreamingServiceSvIf::boththrows(int32_t /*foo*/) {
  apache::thrift::detail::si::throw_app_exn_unimplemented("boththrows");
}

folly::SemiFuture<apache::thrift::ServerStream<int32_t>> PubSubStreamingServiceSvIf::semifuture_boththrows(int32_t foo) {
  return apache::thrift::detail::si::semifuture([&] {
    return boththrows(foo);
  });
}

folly::Future<apache::thrift::ServerStream<int32_t>> PubSubStreamingServiceSvIf::future_boththrows(int32_t foo) {
  return apache::thrift::detail::si::future(semifuture_boththrows(foo), getThreadManager());
}


void PubSubStreamingServiceSvIf::async_tm_boththrows(std::unique_ptr<apache::thrift::HandlerCallback<apache::thrift::ServerStream<int32_t>>> callback, int32_t foo) {
  apache::thrift::detail::si::async_tm(this, std::move(callback), [&] {
    return future_boththrows(foo);
  });
}

apache::thrift::ResponseAndServerStream<int32_t,int32_t> PubSubStreamingServiceSvIf::responseandstreamthrows(int32_t /*foo*/) {
  apache::thrift::detail::si::throw_app_exn_unimplemented("responseandstreamthrows");
}

folly::SemiFuture<apache::thrift::ResponseAndServerStream<int32_t,int32_t>> PubSubStreamingServiceSvIf::semifuture_responseandstreamthrows(int32_t foo) {
  return apache::thrift::detail::si::semifuture([&] {
    return responseandstreamthrows(foo);
  });
}

folly::Future<apache::thrift::ResponseAndServerStream<int32_t,int32_t>> PubSubStreamingServiceSvIf::future_responseandstreamthrows(int32_t foo) {
  return apache::thrift::detail::si::future(semifuture_responseandstreamthrows(foo), getThreadManager());
}


void PubSubStreamingServiceSvIf::async_tm_responseandstreamthrows(std::unique_ptr<apache::thrift::HandlerCallback<apache::thrift::ResponseAndServerStream<int32_t,int32_t>>> callback, int32_t foo) {
  apache::thrift::detail::si::async_tm(this, std::move(callback), [&] {
    return future_responseandstreamthrows(foo);
  });
}

const char* PubSubStreamingServiceAsyncProcessor::getServiceName() {
  return "PubSubStreamingService";
}

void PubSubStreamingServiceAsyncProcessor::getServiceMetadata(apache::thrift::metadata::ThriftServiceMetadataResponse& response) {
  ::apache::thrift::detail::md::ServiceMetadata<PubSubStreamingServiceSvIf>::gen(*response.metadata_ref(), *response.context_ref());
}

void PubSubStreamingServiceAsyncProcessor::processSerializedRequest(apache::thrift::ResponseChannelRequest::UniquePtr req, apache::thrift::SerializedRequest&& serializedRequest, apache::thrift::protocol::PROTOCOL_TYPES protType, apache::thrift::Cpp2RequestContext* context, folly::EventBase* eb, apache::thrift::concurrency::ThreadManager* tm) {
  apache::thrift::detail::ap::process(this, std::move(req), std::move(serializedRequest), protType, context, eb, tm);
}

std::shared_ptr<folly::RequestContext> PubSubStreamingServiceAsyncProcessor::getBaseContextForRequest() {
  return iface_->getBaseContextForRequest();
}

const PubSubStreamingServiceAsyncProcessor::ProcessMap& PubSubStreamingServiceAsyncProcessor::getBinaryProtocolProcessMap() {
  return binaryProcessMap_;
}

const PubSubStreamingServiceAsyncProcessor::ProcessMap PubSubStreamingServiceAsyncProcessor::binaryProcessMap_ {
  {"returnstream", &PubSubStreamingServiceAsyncProcessor::_processInThread_returnstream<apache::thrift::BinaryProtocolReader, apache::thrift::BinaryProtocolWriter>},
  {"streamthrows", &PubSubStreamingServiceAsyncProcessor::_processInThread_streamthrows<apache::thrift::BinaryProtocolReader, apache::thrift::BinaryProtocolWriter>},
  {"boththrows", &PubSubStreamingServiceAsyncProcessor::_processInThread_boththrows<apache::thrift::BinaryProtocolReader, apache::thrift::BinaryProtocolWriter>},
  {"responseandstreamthrows", &PubSubStreamingServiceAsyncProcessor::_processInThread_responseandstreamthrows<apache::thrift::BinaryProtocolReader, apache::thrift::BinaryProtocolWriter>},
};

const PubSubStreamingServiceAsyncProcessor::ProcessMap& PubSubStreamingServiceAsyncProcessor::getCompactProtocolProcessMap() {
  return compactProcessMap_;
}

const PubSubStreamingServiceAsyncProcessor::ProcessMap PubSubStreamingServiceAsyncProcessor::compactProcessMap_ {
  {"returnstream", &PubSubStreamingServiceAsyncProcessor::_processInThread_returnstream<apache::thrift::CompactProtocolReader, apache::thrift::CompactProtocolWriter>},
  {"streamthrows", &PubSubStreamingServiceAsyncProcessor::_processInThread_streamthrows<apache::thrift::CompactProtocolReader, apache::thrift::CompactProtocolWriter>},
  {"boththrows", &PubSubStreamingServiceAsyncProcessor::_processInThread_boththrows<apache::thrift::CompactProtocolReader, apache::thrift::CompactProtocolWriter>},
  {"responseandstreamthrows", &PubSubStreamingServiceAsyncProcessor::_processInThread_responseandstreamthrows<apache::thrift::CompactProtocolReader, apache::thrift::CompactProtocolWriter>},
};

} // cpp2
