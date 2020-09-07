// Autogenerated by Thrift Compiler (facebook)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
// @generated

package includes

import (
	"bytes"
	"context"
	"sync"
	"fmt"
	thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift"
	transitive0 "transitive"

)

// (needed to ensure safety because of naive import list construction.)
var _ = thrift.ZERO
var _ = fmt.Printf
var _ = sync.Mutex{}
var _ = bytes.Equal
var _ = context.Background

var _ = transitive0.GoUnusedProtection__
var GoUnusedProtection__ int;

type IncludedInt64 = int64

func IncludedInt64Ptr(v IncludedInt64) *IncludedInt64 { return &v }

type TransitiveFoo = transitive0.Foo

func TransitiveFooPtr(v TransitiveFoo) *TransitiveFoo { return &v }

func NewTransitiveFoo() *TransitiveFoo { return transitive0.NewFoo() }

// Attributes:
//  - MyIntField
//  - MyTransitiveField
type Included struct {
  MyIntField int64 `thrift:"MyIntField,1" db:"MyIntField" json:"MyIntField"`
  MyTransitiveField *transitive0.Foo `thrift:"MyTransitiveField,2" db:"MyTransitiveField" json:"MyTransitiveField"`
}

func NewIncluded() *Included {
  return &Included{
MyTransitiveField: transitive0.NewFoo(),
}
}


func (p *Included) GetMyIntField() int64 {
  return p.MyIntField
}
var Included_MyTransitiveField_DEFAULT *transitive0.Foo = &transitive0.Foo{
  A: 2,
}
func (p *Included) GetMyTransitiveField() *transitive0.Foo {
  if !p.IsSetMyTransitiveField() {
    return Included_MyTransitiveField_DEFAULT
  }
return p.MyTransitiveField
}
func (p *Included) IsSetMyTransitiveField() bool {
  return p.MyTransitiveField != nil
}

func (p *Included) Read(iprot thrift.Protocol) error {
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

func (p *Included)  ReadField1(iprot thrift.Protocol) error {
  if v, err := iprot.ReadI64(); err != nil {
  return thrift.PrependError("error reading field 1: ", err)
} else {
  p.MyIntField = v
}
  return nil
}

func (p *Included)  ReadField2(iprot thrift.Protocol) error {
  p.MyTransitiveField = transitive0.NewFoo()
  if err := p.MyTransitiveField.Read(iprot); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T error reading struct: ", p.MyTransitiveField), err)
  }
  return nil
}

func (p *Included) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("Included"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := p.writeField2(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *Included) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("MyIntField", thrift.I64, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:MyIntField: ", p), err) }
  if err := oprot.WriteI64(int64(p.MyIntField)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.MyIntField (1) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:MyIntField: ", p), err) }
  return err
}

func (p *Included) writeField2(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("MyTransitiveField", thrift.STRUCT, 2); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 2:MyTransitiveField: ", p), err) }
  if err := p.MyTransitiveField.Write(oprot); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T error writing struct: ", p.MyTransitiveField), err)
  }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 2:MyTransitiveField: ", p), err) }
  return err
}

func (p *Included) String() string {
  if p == nil {
    return "<nil>"
  }

  myIntFieldVal := fmt.Sprintf("%v", p.MyIntField)
  var myTransitiveFieldVal string
  if p.MyTransitiveField == nil {
    myTransitiveFieldVal = "<nil>"
  } else {
    myTransitiveFieldVal = fmt.Sprintf("%v", p.MyTransitiveField)
  }
  return fmt.Sprintf("Included({MyIntField:%s MyTransitiveField:%s})", myIntFieldVal, myTransitiveFieldVal)
}

