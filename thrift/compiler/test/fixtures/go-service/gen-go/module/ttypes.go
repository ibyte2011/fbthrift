// Autogenerated by Thrift Compiler (facebook)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
// @generated

package module

import (
	"bytes"
	"context"
	"sync"
	"fmt"
	thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift"
)

// (needed to ensure safety because of naive import list construction.)
var _ = thrift.ZERO
var _ = fmt.Printf
var _ = sync.Mutex{}
var _ = bytes.Equal
var _ = context.Background

var GoUnusedProtection__ int;

// Attributes:
//  - Id
type GetEntityRequest struct {
  Id string `thrift:"id,1" db:"id" json:"id"`
}

func NewGetEntityRequest() *GetEntityRequest {
  return &GetEntityRequest{}
}


func (p *GetEntityRequest) GetId() string {
  return p.Id
}
func (p *GetEntityRequest) Read(iprot thrift.Protocol) error {
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

func (p *GetEntityRequest)  ReadField1(iprot thrift.Protocol) error {
  if v, err := iprot.ReadString(); err != nil {
  return thrift.PrependError("error reading field 1: ", err)
} else {
  p.Id = v
}
  return nil
}

func (p *GetEntityRequest) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("GetEntityRequest"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *GetEntityRequest) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("id", thrift.STRING, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:id: ", p), err) }
  if err := oprot.WriteString(string(p.Id)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.id (1) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:id: ", p), err) }
  return err
}

func (p *GetEntityRequest) String() string {
  if p == nil {
    return "<nil>"
  }

  idVal := fmt.Sprintf("%v", p.Id)
  return fmt.Sprintf("GetEntityRequest({Id:%s})", idVal)
}

// Attributes:
//  - Entity
type GetEntityResponse struct {
  Entity string `thrift:"entity,1" db:"entity" json:"entity"`
}

func NewGetEntityResponse() *GetEntityResponse {
  return &GetEntityResponse{}
}


func (p *GetEntityResponse) GetEntity() string {
  return p.Entity
}
func (p *GetEntityResponse) Read(iprot thrift.Protocol) error {
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

func (p *GetEntityResponse)  ReadField1(iprot thrift.Protocol) error {
  if v, err := iprot.ReadString(); err != nil {
  return thrift.PrependError("error reading field 1: ", err)
} else {
  p.Entity = v
}
  return nil
}

func (p *GetEntityResponse) Write(oprot thrift.Protocol) error {
  if err := oprot.WriteStructBegin("GetEntityResponse"); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", p), err) }
  if err := p.writeField1(oprot); err != nil { return err }
  if err := oprot.WriteFieldStop(); err != nil {
    return thrift.PrependError("write field stop error: ", err) }
  if err := oprot.WriteStructEnd(); err != nil {
    return thrift.PrependError("write struct stop error: ", err) }
  return nil
}

func (p *GetEntityResponse) writeField1(oprot thrift.Protocol) (err error) {
  if err := oprot.WriteFieldBegin("entity", thrift.STRING, 1); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field begin error 1:entity: ", p), err) }
  if err := oprot.WriteString(string(p.Entity)); err != nil {
  return thrift.PrependError(fmt.Sprintf("%T.entity (1) field write error: ", p), err) }
  if err := oprot.WriteFieldEnd(); err != nil {
    return thrift.PrependError(fmt.Sprintf("%T write field end error 1:entity: ", p), err) }
  return err
}

func (p *GetEntityResponse) String() string {
  if p == nil {
    return "<nil>"
  }

  entityVal := fmt.Sprintf("%v", p.Entity)
  return fmt.Sprintf("GetEntityResponse({Entity:%s})", entityVal)
}

