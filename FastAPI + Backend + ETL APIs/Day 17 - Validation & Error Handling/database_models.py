from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship

Base=declarative_base()

class User(Base):
    __tablename__="users"
    u_id=Column(Integer,primary_key=True,index=True)
    u_name=Column(String(100),nullable=False)
    email=Column(String(100),unique=True,nullable=False)

    products=relationship("Product",back_populates="owner")


class Product(Base):
    __tablename__="products"
    p_id=Column(Integer,primary_key=True,index=True)
    p_name=Column(String(100),nullable=False)
    price=Column(Float,nullable=False)

    owner_id=Column(Integer,ForeignKey("users.u_id"))

    owner=relationship("User",back_populates="products")


