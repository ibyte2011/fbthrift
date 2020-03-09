/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package test.fixtures.enumstrict;

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
public class MyStruct implements TBase, java.io.Serializable, Cloneable, Comparable<MyStruct> {
  private static final TStruct STRUCT_DESC = new TStruct("MyStruct");
  private static final TField MY_ENUM_FIELD_DESC = new TField("myEnum", TType.I32, (short)1);
  private static final TField MY_BIG_ENUM_FIELD_DESC = new TField("myBigEnum", TType.I32, (short)2);

  /**
   * 
   * @see MyEnum
   */
  public MyEnum myEnum;
  /**
   * 
   * @see MyBigEnum
   */
  public MyBigEnum myBigEnum;
  public static final int MYENUM = 1;
  public static final int MYBIGENUM = 2;

  // isset id assignments

  public static final Map<Integer, FieldMetaData> metaDataMap;

  static {
    Map<Integer, FieldMetaData> tmpMetaDataMap = new HashMap<Integer, FieldMetaData>();
    tmpMetaDataMap.put(MYENUM, new FieldMetaData("myEnum", TFieldRequirementType.DEFAULT, 
        new FieldValueMetaData(TType.I32)));
    tmpMetaDataMap.put(MYBIGENUM, new FieldMetaData("myBigEnum", TFieldRequirementType.DEFAULT, 
        new FieldValueMetaData(TType.I32)));
    metaDataMap = Collections.unmodifiableMap(tmpMetaDataMap);
  }

  static {
    FieldMetaData.addStructMetaDataMap(MyStruct.class, metaDataMap);
  }

  public MyStruct() {
    this.myBigEnum = test.fixtures.enumstrict.MyBigEnum.ONE;

  }

  public MyStruct(
    MyEnum myEnum,
    MyBigEnum myBigEnum)
  {
    this();
    this.myEnum = myEnum;
    this.myBigEnum = myBigEnum;
  }

  public static class Builder {
    private MyEnum myEnum;
    private MyBigEnum myBigEnum;

    public Builder() {
    }

    public Builder setMyEnum(final MyEnum myEnum) {
      this.myEnum = myEnum;
      return this;
    }

    public Builder setMyBigEnum(final MyBigEnum myBigEnum) {
      this.myBigEnum = myBigEnum;
      return this;
    }

    public MyStruct build() {
      MyStruct result = new MyStruct();
      result.setMyEnum(this.myEnum);
      result.setMyBigEnum(this.myBigEnum);
      return result;
    }
  }

  public static Builder builder() {
    return new Builder();
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public MyStruct(MyStruct other) {
    if (other.isSetMyEnum()) {
      this.myEnum = TBaseHelper.deepCopy(other.myEnum);
    }
    if (other.isSetMyBigEnum()) {
      this.myBigEnum = TBaseHelper.deepCopy(other.myBigEnum);
    }
  }

  public MyStruct deepCopy() {
    return new MyStruct(this);
  }

  /**
   * 
   * @see MyEnum
   */
  public MyEnum getMyEnum() {
    return this.myEnum;
  }

  /**
   * 
   * @see MyEnum
   */
  public MyStruct setMyEnum(MyEnum myEnum) {
    this.myEnum = myEnum;
    return this;
  }

  public void unsetMyEnum() {
    this.myEnum = null;
  }

  // Returns true if field myEnum is set (has been assigned a value) and false otherwise
  public boolean isSetMyEnum() {
    return this.myEnum != null;
  }

  public void setMyEnumIsSet(boolean __value) {
    if (!__value) {
      this.myEnum = null;
    }
  }

  /**
   * 
   * @see MyBigEnum
   */
  public MyBigEnum getMyBigEnum() {
    return this.myBigEnum;
  }

  /**
   * 
   * @see MyBigEnum
   */
  public MyStruct setMyBigEnum(MyBigEnum myBigEnum) {
    this.myBigEnum = myBigEnum;
    return this;
  }

  public void unsetMyBigEnum() {
    this.myBigEnum = null;
  }

  // Returns true if field myBigEnum is set (has been assigned a value) and false otherwise
  public boolean isSetMyBigEnum() {
    return this.myBigEnum != null;
  }

  public void setMyBigEnumIsSet(boolean __value) {
    if (!__value) {
      this.myBigEnum = null;
    }
  }

  public void setFieldValue(int fieldID, Object __value) {
    switch (fieldID) {
    case MYENUM:
      if (__value == null) {
        unsetMyEnum();
      } else {
        setMyEnum((MyEnum)__value);
      }
      break;

    case MYBIGENUM:
      if (__value == null) {
        unsetMyBigEnum();
      } else {
        setMyBigEnum((MyBigEnum)__value);
      }
      break;

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  public Object getFieldValue(int fieldID) {
    switch (fieldID) {
    case MYENUM:
      return getMyEnum();

    case MYBIGENUM:
      return getMyBigEnum();

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  @Override
  public boolean equals(Object _that) {
    if (_that == null)
      return false;
    if (this == _that)
      return true;
    MyStruct that = (MyStruct)_that;

    if (!TBaseHelper.equalsNobinary(this.isSetMyEnum(), that.isSetMyEnum(), this.myEnum, that.myEnum)) { return false; }

    if (!TBaseHelper.equalsNobinary(this.isSetMyBigEnum(), that.isSetMyBigEnum(), this.myBigEnum, that.myBigEnum)) { return false; }

    return true;
  }

  @Override
  public int hashCode() {
    return Arrays.deepHashCode(new Object[] {myEnum, myBigEnum});
  }

  @Override
  public int compareTo(MyStruct other) {
    if (other == null) {
      // See java.lang.Comparable docs
      throw new NullPointerException();
    }

    if (other == this) {
      return 0;
    }
    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetMyEnum()).compareTo(other.isSetMyEnum());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(myEnum, other.myEnum);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    lastComparison = Boolean.valueOf(isSetMyBigEnum()).compareTo(other.isSetMyBigEnum());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(myBigEnum, other.myBigEnum);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    return 0;
  }

  public void read(TProtocol iprot) throws TException {
    TField __field;
    iprot.readStructBegin(metaDataMap);
    while (true)
    {
      __field = iprot.readFieldBegin();
      if (__field.type == TType.STOP) { 
        break;
      }
      switch (__field.id)
      {
        case MYENUM:
          if (__field.type == TType.I32) {
            this.myEnum = MyEnum.findByValue(iprot.readI32());
          } else { 
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        case MYBIGENUM:
          if (__field.type == TType.I32) {
            this.myBigEnum = MyBigEnum.findByValue(iprot.readI32());
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


    // check for required fields of primitive type, which can't be checked in the validate method
    validate();
  }

  public void write(TProtocol oprot) throws TException {
    validate();

    oprot.writeStructBegin(STRUCT_DESC);
    if (this.myEnum != null) {
      oprot.writeFieldBegin(MY_ENUM_FIELD_DESC);
      oprot.writeI32(this.myEnum == null ? 0 : this.myEnum.getValue());
      oprot.writeFieldEnd();
    }
    if (this.myBigEnum != null) {
      oprot.writeFieldBegin(MY_BIG_ENUM_FIELD_DESC);
      oprot.writeI32(this.myBigEnum == null ? 0 : this.myBigEnum.getValue());
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
    String indentStr = prettyPrint ? TBaseHelper.getIndentedString(indent) : "";
    String newLine = prettyPrint ? "\n" : "";
    String space = prettyPrint ? " " : "";
    StringBuilder sb = new StringBuilder("MyStruct");
    sb.append(space);
    sb.append("(");
    sb.append(newLine);
    boolean first = true;

    sb.append(indentStr);
    sb.append("myEnum");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getMyEnum() == null) {
      sb.append("null");
    } else {
      String myEnum_name = this.getMyEnum() == null ? "null" : this.getMyEnum().name();
      if (myEnum_name != null) {
        sb.append(myEnum_name);
        sb.append(" (");
      }
      sb.append(this.getMyEnum());
      if (myEnum_name != null) {
        sb.append(")");
      }
    }
    first = false;
    if (!first) sb.append("," + newLine);
    sb.append(indentStr);
    sb.append("myBigEnum");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getMyBigEnum() == null) {
      sb.append("null");
    } else {
      String myBigEnum_name = this.getMyBigEnum() == null ? "null" : this.getMyBigEnum().name();
      if (myBigEnum_name != null) {
        sb.append(myBigEnum_name);
        sb.append(" (");
      }
      sb.append(this.getMyBigEnum());
      if (myBigEnum_name != null) {
        sb.append(")");
      }
    }
    first = false;
    sb.append(newLine + TBaseHelper.reduceIndent(indentStr));
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws TException {
    // check for required fields
  }

}

