// Autogenerated by Thrift Compiler (facebook)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
// @generated

package module

import (
	"bytes"
	"sync"
	"fmt"
	"github.com/facebook/fbthrift-go"
	includes0 "includes"

)

// (needed to ensure safety because of naive import list construction.)
var _ = thrift.ZERO
var _ = fmt.Printf
var _ = sync.Mutex{}
var _ = bytes.Equal

var _ = includes0.GoUnusedProtection__
var GoUnusedProtection__ int;

// Attributes:
//  - MyIncludedField
//  - MyOtherIncludedField
//  - MyIncludedInt
type MyStruct struct {
  MyIncludedField *includes0.Included `thrift:"MyIncludedField,1" db:"MyIncludedField" json:"MyIncludedField"`
  MyOtherIncludedField *includes0.Included `thrift:"MyOtherIncludedField,2" db:"MyOtherIncludedField" json:"MyOtherIncludedField"`
  MyIncludedInt includes0.IncludedInt64 `thrift:"MyIncludedInt,3" db:"MyIncludedInt" json:"MyIncludedInt"`
}

func NewMyStruct() *MyStruct {
  return &MyStruct{
MyIncludedInt: 42,
}
}

var MyStruct_MyIncludedField_DEFAULT *includes0.Included = &includes0.Included{
  MyIntField: 2,
  MyTransitiveField: &.Foo{
    A: 2,
  },
}
func (p *MyStruct) GetMyIncludedField() *includes0.Included {
  if !p.IsSetMyIncludedField() {
    return MyStruct_MyIncludedField_DEFAULT
  }
return p.MyIncludedField
}
var MyStruct_MyOtherIncludedField_DEFAULT *includes0.Included
func (p *MyStruct) GetMyOtherIncludedField() *includes0.Included {
  if !p.IsSetMyOtherIncludedField() {
    return MyStruct_MyOtherIncludedField_DEFAULT
  }
return p.MyOtherIncludedField
}

func (p *MyStruct) GetMyIncludedInt() includes0.IncludedInt64 {
  return p.MyIncludedInt
}
func (p *MyStruct) IsSetMyIncludedField() bool {
  return p.MyIncludedField != nil
}

func (p *MyStruct) IsSetMyOtherIncludedField() bool {
  return p.MyOtherIncludedField != nil
}

func (p *MyStruct) Read(iprot thrift.Protocol) error {
  if _, err := iprot.ReadStructBegin(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read error: ", p), err)
  }


  for {
    _, fieldTypeId, fieldId, err := iprot.ReadFieldBegin()
    if err != nil {
      return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", p, fieldId), err)
    }
    if fieldTypeId == thrift.STOP { break; }
    switch fieldId {
    case 1:
      if err := p.ReadField1(iprot); err != nil {
        return err
      }
    case 2:
      if err := p.ReadField2(iprot); err != nil {
        return err
      }
    case 3:
      if err := p.ReadField3(iprot); err != nil {
        return err
      }
    default:
      if err := iprot.Skip(fieldTypeId); err != nil {
        return err
      }
    }
    if err := iprot.ReadFieldEnd(); err != nil {
      return err
    }
  }
  if err := iprot.ReadStructEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", p), err)
  }
  return nil
}

func (p *MyStruct)  ReadField1(iprot thrift.Protocol) error {
  p.MyIncludedField = includes0.NewIncluded()
  if err := p.MyIncludedField.Read(iprot); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T error reading struct: ", p.MyIncludedField), err)
  }
  return nil
}

func (p *MyStruct)  ReadField2(iprot thrift.Protocol) error {
  p.MyOtherIncludedField = includes0.NewIncluded()
  if err := p.MyOtherIncludedField.Read(iprot); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T error reading struct: ", p.MyOtherIncludedField), err)
  }
  return nil
}

func (p *MyStruct)  ReadField3(iprot thrift.Protocol) error {
  if v, err := iprot.ReadI64(); err != nil {
  return thrift.PrependError("error reading field 3: ", err)
} else {
  temp := includes0.IncludedInt64(v)
  p.MyIncludedInt = temp
}
  return nil
}

func (p *MyStruct) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("MyStruct"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := p.writeField2(oprot); err != nil { return err }
  if err := p.writeField3(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *MyStruct) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("MyIncludedField", thrift.STRUCT, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:MyIncludedField: ", p), err) }
  if err := p.MyIncludedField.Write(oprot); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T error writing struct: ", p.MyIncludedField), err)
  }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:MyIncludedField: ", p), err) }
  return err
}

func (p *MyStruct) writeField2(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("MyOtherIncludedField", thrift.STRUCT, 2); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 2:MyOtherIncludedField: ", p), err) }
  if err := p.MyOtherIncludedField.Write(oprot); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T error writing struct: ", p.MyOtherIncludedField), err)
  }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 2:MyOtherIncludedField: ", p), err) }
  return err
}

func (p *MyStruct) writeField3(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("MyIncludedInt", thrift.I64, 3); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 3:MyIncludedInt: ", p), err) }
  if err := oprot.WriteI64(int64(p.MyIncludedInt)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.MyIncludedInt (3) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 3:MyIncludedInt: ", p), err) }
  return err
}

func (p *MyStruct) String() string {
  if p == nil {
    return "<nil>"
  }
  return fmt.Sprintf("MyStruct(%+v)", *p)
}

