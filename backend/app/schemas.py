from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from typing import List

class DashboardResponse(BaseModel):
    total_products: int
    total_customers: int
    total_orders: int
    low_stock_products: int
    
class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate]

class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str

class CustomerResponse(CustomerCreate):
    id: int
    class Config:
        from_attributes = True
class ProductUpdate(BaseModel):
    name: str
    sku: str
    price: float = Field(gt=0)
    stock_quantity: int = Field(ge=0)

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float = Field(gt=0)
    stock_quantity: int = Field(ge=0)

class ProductResponse(ProductCreate):
    id: int
    class Config:
        from_attributes = True

class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    
class CustomerResponse(CustomerCreate):
    id: int
    class Config:
        from_attributes = True

