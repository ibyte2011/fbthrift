// Autogenerated by Thrift Compiler (facebook)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
// @generated

package module

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

type Banal struct {
}

func NewBanal() *Banal {
  return &Banal{}
}

func (p *Banal) Read(iprot thrift.Protocol) error {
  if _, err := iprot.ReadStructBegin(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read error: ", p), err)
  }


  for {
    _, fieldTypeId, fieldId, err := iprot.ReadFieldBegin()
    if err != nil {
      return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", p, fieldId), err)
    }
    if fieldTypeId == thrift.STOP { break; }
    if err := iprot.Skip(fieldTypeId); err != nil {
      return err
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

func (p *Banal) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("Banal"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *Banal) String() string {
  if p == nil {
    return "<nil>"
  }
  return fmt.Sprintf("Banal(%+v)", *p)
}

func (p *Banal) Error() string {
  return p.String()
}

// Attributes:
//  - Message
type Fiery struct {
  Message string `thrift:"message,1,required" db:"message" json:"message"`
}

func NewFiery() *Fiery {
  return &Fiery{}
}


func (p *Fiery) GetMessage() string {
  return p.Message
}
func (p *Fiery) Read(iprot thrift.Protocol) error {
  if _, err := iprot.ReadStructBegin(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T read error: ", p), err)
  }

  var issetMessage bool = false;

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
      issetMessage = true
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
  if !issetMessage{
    return thrift.NewProtocolExceptionWithType(thrift.INVALID_DATA, fmt.Errorf("Required field Message is not set"));
  }
  return nil
}

func (p *Fiery)  ReadField1(iprot thrift.Protocol) error {
  if v, err := iprot.ReadString(); err != nil {
  return thrift.PrependError("error reading field 1: ", err)
} else {
  p.Message = v
}
  return nil
}

func (p *Fiery) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("Fiery"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *Fiery) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("message", thrift.STRING, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:message: ", p), err) }
  if err := oprot.WriteString(string(p.Message)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.message (1) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:message: ", p), err) }
  return err
}

func (p *Fiery) String() string {
  if p == nil {
    return "<nil>"
  }
  return fmt.Sprintf("Fiery(%+v)", *p)
}

func (p *Fiery) Error() string {
  return p.String()
}

