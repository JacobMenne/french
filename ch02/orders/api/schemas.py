from enum import Enum
from typing import List, Optional, Annotated
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, conlist, conint, field_validator

class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'

class Status(Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'

class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[Annotated[int, Field(ge=1, strict=True)]] = 1

    @field_validator('quantity')
    def quantity_non_nullable(cls, value):
        assert value is not None, 'quantity may not be None'
        return value

class CreateOrderSchema(BaseModel):
    order: list[OrderItemSchema] = Field(..., min_length=1)
    
class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status

class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]

    