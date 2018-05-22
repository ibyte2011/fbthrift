// Autogenerated by Thrift Compiler (facebook)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
// @generated

package transitive

import (
	"bytes"
	"sync"
	"fmt"
	"github.com/facebook/fbthrift-go"
)

// (needed to ensure safety because of naive import list construction.)
var _ = thrift.ZERO
var _ = fmt.Printf
var _ = sync.Mutex{}
var _ = bytes.Equal

var GoUnusedProtection__ int;

// Attributes:
//  - A
type Foo struct {
  A int64 `thrift:"a,1" db:"a" json:"a"`
}

func NewFoo() *Foo {
  return &Foo{
A: 2,
}
}


func (p *Foo) GetA() int64 {
  return p.A
}
func (p *Foo) Read(iprot thrift.Protocol) error {
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

func (p *Foo)  ReadField1(iprot thrift.Protocol) error {
  if v, err := iprot.ReadI64(); err != nil {
  return thrift.PrependError("error reading field 1: ", err)
} else {
  p.A = v
}
  return nil
}

func (p *Foo) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("Foo"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *Foo) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("a", thrift.I64, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:a: ", p), err) }
  if err := oprot.WriteI64(int64(p.A)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.a (1) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:a: ", p), err) }
  return err
}

func (p *Foo) String() string {
  if p == nil {
    return "<nil>"
  }
  return fmt.Sprintf("Foo(%+v)", *p)
}

