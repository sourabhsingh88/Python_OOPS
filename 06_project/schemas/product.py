from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str
    sku: str
    price: float
    is_active: bool = True
    manufacturer_id: int


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
