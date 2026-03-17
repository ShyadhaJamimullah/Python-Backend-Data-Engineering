#db connection imports
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session

#pydantic model imports
from pydantic import BaseModel
from typing import Optional

#database model imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String


from fastapi import FastAPI,Depends,HTTPException
app=FastAPI()


#database connection
load_dotenv()

db_user=os.getenv("db_user")
db_password=os.getenv("db_password")
db_host=os.getenv("db_host")
db_port=os.getenv("db_port")
db_name=os.getenv("db_name")

if not all([db_user,db_password,db_host,db_port,db_name]):
    raise ValueError("Database environment variables are not set properly")

db_url=f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine=create_engine(db_url)
session=sessionmaker(bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


#pydantic models
class CreateUser(BaseModel):
    name:str
    age:int

class RetrieveUser(BaseModel):
    id:int
    name:str
    age:int
    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None


#database models
Base=declarative_base()

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    age=Column(Integer,nullable=False)

#http methods
Base.metadata.create_all(bind=engine) 

@app.post("/users")
def add_user(user:CreateUser,db:Session=Depends(get_db)):
    db_user=User(name=user.name,age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user=db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{id}")
def update_user(id: int, user: CreateUser, db: Session = Depends(get_db)):
    db_user=db.query(User).filter(User.id==id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name=user.name
    db_user.age=user.age

    db.commit()
    db.refresh(db_user)

    return db_user

@app.patch("/users/{id}")
def partial_update(id:int,user:UpdateUser,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.id==id).first()

    if not db_user:
        raise HTTPException(status_code=404,detail="User not found")
    
    update_data={
        key:val
        for key, val in user.model_dump(exclude_unset=True).items()
        if val is not None and val!=""
    }

    for key, val in update_data.items():
        setattr(db_user, key, val)

    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}




        
