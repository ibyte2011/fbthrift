/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

package test.fixtures.stream;

import com.facebook.swift.codec.*;
import com.facebook.swift.codec.ThriftField.Requiredness;
import com.facebook.swift.codec.ThriftField.Recursiveness;
import java.util.*;
import org.apache.thrift.*;
import org.apache.thrift.async.*;
import org.apache.thrift.meta_data.*;
import org.apache.thrift.server.*;
import org.apache.thrift.transport.*;
import org.apache.thrift.protocol.*;
import org.apache.thrift.meta_data.FieldMetaData;
import org.apache.thrift.meta_data.FieldValueMetaData;

@SwiftGenerated
@ThriftStruct("FooEx")
public final class FooEx extends java.lang.Exception {
    private static final long serialVersionUID = 1L;

    private BitSet __isset_bit_vector = new BitSet();

    public static final Map<String, Integer> NAMES_TO_IDS = new HashMap();
    public static final Map<Integer, Object> FIELD_METADATA = new HashMap<>();

    private static final TStruct STRUCT_DESC = new TStruct("FooEx");

    @ThriftConstructor
    public FooEx(
    ) {
    }
    
    
    
    public static class Builder {
        private final BitSet __optional_isset = new BitSet();
    
    
    public Builder() { }
        public Builder(FooEx other) {
        }
    
        @ThriftConstructor
        public FooEx build() {
            FooEx result = new FooEx (
            );
            result.__isset_bit_vector.or(__optional_isset);
            return result;
        }
    }
    

    
    public static FooEx read0(TProtocol oprot) throws TException {
      TField __field;
      oprot.readStructBegin(FooEx.NAMES_TO_IDS, FooEx.FIELD_METADATA);
      FooEx.Builder builder = new FooEx.Builder();
      while (true) {
        __field = oprot.readFieldBegin();
        if (__field.type == TType.STOP) { break; }
        switch (__field.id) {
        default:
          TProtocolUtil.skip(oprot, __field.type);
          break;
        }
        oprot.readFieldEnd();
      }
      oprot.readStructEnd();
      return builder.build();
    }
    
    public void write0(TProtocol oprot) throws TException {
      oprot.writeStructBegin(STRUCT_DESC);
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }
    
}
