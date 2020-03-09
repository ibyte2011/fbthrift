/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package one.two.three;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;
import java.util.BitSet;
import java.util.Arrays;
import com.facebook.thrift.*;
import com.facebook.thrift.async.*;
import com.facebook.thrift.meta_data.*;
import com.facebook.thrift.server.*;
import com.facebook.thrift.transport.*;
import com.facebook.thrift.protocol.*;

@SuppressWarnings({ "unused", "serial" })
public class Included implements TBase, java.io.Serializable, Cloneable {
  private static final TStruct STRUCT_DESC = new TStruct("Included");
  private static final TField MY_INT_FIELD_FIELD_DESC = new TField("MyIntField", TType.I64, (short)1);
  private static final TField MY_TRANSITIVE_FIELD_FIELD_DESC = new TField("MyTransitiveField", TType.STRUCT, (short)2);

  public final Long MyIntField;
  public final Foo MyTransitiveField;
  public static final int MYINTFIELD = 1;
  public static final int MYTRANSITIVEFIELD = 2;

  public Included(
    Long MyIntField,
    Foo MyTransitiveField)
  {
    this.MyIntField = MyIntField;
    this.MyTransitiveField = MyTransitiveField;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public Included(Included other) {
    if (other.isSetMyIntField()) {
      this.MyIntField = TBaseHelper.deepCopy(other.MyIntField);
    } else {
      this.MyIntField = null;
    }
    if (other.isSetMyTransitiveField()) {
      this.MyTransitiveField = TBaseHelper.deepCopy(other.MyTransitiveField);
    } else {
      this.MyTransitiveField = null;
    }
  }

  public Included deepCopy() {
    return new Included(this);
  }

  public Long getMyIntField() {
    return this.MyIntField;
  }

  // Returns true if field MyIntField is set (has been assigned a value) and false otherwise
  public boolean isSetMyIntField() {
    return this.MyIntField != null;
  }

  public Foo getMyTransitiveField() {
    return this.MyTransitiveField;
  }

  // Returns true if field MyTransitiveField is set (has been assigned a value) and false otherwise
  public boolean isSetMyTransitiveField() {
    return this.MyTransitiveField != null;
  }

  @Override
  public boolean equals(Object _that) {
    if (_that == null)
      return false;
    if (this == _that)
      return true;
    Included that = (Included)_that;

    if (!TBaseHelper.equalsNobinary(this.isSetMyIntField(), that.isSetMyIntField(), this.MyIntField, that.MyIntField)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetMyTransitiveField(), that.isSetMyTransitiveField(), this.MyTransitiveField, that.MyTransitiveField)) { return false; }

    return true;
  }

  @Override
  public int hashCode() {
    return Arrays.deepHashCode(new Object[] {MyIntField, MyTransitiveField});
  }

  // This is required to satisfy the TBase interface, but can't be implemented on immutable struture.
  public void read(TProtocol iprot) throws TException {
    throw new TException("unimplemented in android immutable structure");
  }

  public static Included deserialize(TProtocol iprot) throws TException {
    Long tmp_MyIntField = null;
    Foo tmp_MyTransitiveField = null;
    TField __field;
    iprot.readStructBegin();
    while (true)
    {
      __field = iprot.readFieldBegin();
      if (__field.type == TType.STOP) { 
        break;
      }
      switch (__field.id)
      {
        case MYINTFIELD:
          if (__field.type == TType.I64) {
            tmp_MyIntField = iprot.readI64();
          } else { 
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case MYTRANSITIVEFIELD:
          if (__field.type == TType.STRUCT) {
            tmp_MyTransitiveField = Foo.deserialize(iprot);
          } else { 
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        default:
          TProtocolUtil.skip(iprot, __field.type);
          break;
      }
      iprot.readFieldEnd();
    }
    iprot.readStructEnd();

    Included _that;
    _that = new Included(
      tmp_MyIntField
      ,tmp_MyTransitiveField
    );
    _that.validate();
    return _that;
  }

  public void write(TProtocol oprot) throws TException {
    validate();

    oprot.writeStructBegin(STRUCT_DESC);
    if (this.MyIntField != null) {
      oprot.writeFieldBegin(MY_INT_FIELD_FIELD_DESC);
      oprot.writeI64(this.MyIntField);
      oprot.writeFieldEnd();
    }
    if (this.MyTransitiveField != null) {
      oprot.writeFieldBegin(MY_TRANSITIVE_FIELD_FIELD_DESC);
      this.MyTransitiveField.write(oprot);
      oprot.writeFieldEnd();
    }
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  @Override
  public String toString() {
    return toString(1, true);
  }

  @Override
  public String toString(int indent, boolean prettyPrint) {
    return TBaseHelper.toStringHelper(this, indent, prettyPrint);
  }

  public void validate() throws TException {
    // check for required fields
  }

}

