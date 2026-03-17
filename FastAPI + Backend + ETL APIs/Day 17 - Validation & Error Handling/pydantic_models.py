from pydantic import BaseModel
from typing import List,Optional

class UserCreate(BaseModel):
    u_name:str
    email:str


class UserBasic(BaseModel):
    u_id:int
    u_name:str
    email:str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    u_name:Optional[str]=None
    email:Optional[str]=None

class UserWithProducts(BaseModel):
    u_id:int
    u_name:str
    email:str
    products:List["ProductBasic"]

    class Config:
        from_attributes = True

    
class ProductCreate(BaseModel):
    p_name:str
    price:float
    owner_id:int


class ProductBasic(BaseModel):
    p_id:int
    p_name:str
    price:float

    class Config:
        from_attributes = True

class ProductWithOwner(BaseModel):
    p_id:int
    p_name:str
    price:float
    owner:UserBasic

    class Config:
        from_attributes = True


UserWithProducts.model_rebuild()