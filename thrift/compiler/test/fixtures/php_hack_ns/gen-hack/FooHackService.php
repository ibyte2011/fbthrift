<?hh // strict
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

/**
 * Original thrift service:-
 * FooHackService
 */
interface FooHackServiceAsyncIf extends \IThriftAsyncIf {
}

/**
 * Original thrift service:-
 * FooHackService
 */
interface FooHackServiceIf extends \IThriftSyncIf {
}

/**
 * Original thrift service:-
 * FooHackService
 */
interface FooHackServiceClientIf extends \IThriftSyncIf {
}

/**
 * Original thrift service:-
 * FooHackService
 */
interface FooHackServiceAsyncRpcOptionsIf extends \IThriftAsyncRpcOptionsIf {
}

/**
 * Original thrift service:-
 * FooHackService
 */
trait FooHackServiceClientBase {
  require extends \ThriftClientBase;

}

class FooHackServiceAsyncClient extends \ThriftClientBase implements FooHackServiceAsyncIf {
  use FooHackServiceClientBase;

}

class FooHackServiceClient extends \ThriftClientBase implements FooHackServiceClientIf {
  use FooHackServiceClientBase;

  /* send and recv functions */
}

class FooHackServiceAsyncRpcOptionsClient extends \ThriftClientBase implements FooHackServiceAsyncRpcOptionsIf {
  use FooHackServiceClientBase;

}

// HELPER FUNCTIONS AND STRUCTURES

class FooHackServiceStaticMetadata implements \IThriftServiceStaticMetadata {
  public static function getAllStructuredAnnotations(): \TServiceAnnotations {
    return shape(
      'service' => dict[],
      'functions' => dict[
      ],
    );
  }
}

