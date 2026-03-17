from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from pydantic_models import*
from database_models import*
from database_connection import engine,get_db


app=FastAPI()


Base.metadata.create_all(bind=engine) #create tables in mysql 



#add user
@app.post("/users")
def add_user(user: UserCreate, db: Session=Depends(get_db)):
    db_user=User(u_name=user.u_name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#get single user
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.u_id==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#update user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.u_id==user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.u_name=user.u_name
    db_user.email=user.email

    db.commit()
    db.refresh(db_user)

    return db_user

#partial update
@app.patch("/users/{user_id}")
def partial_update(user_id:int,user:UserUpdate,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.u_id==user_id).first()

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

#delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.u_id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}


#add product
@app.post("/products")
def add_product(product: ProductCreate, db: Session=Depends(get_db)):
    owner = db.query(User).filter(User.u_id==product.owner_id).first()

    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    db_product=Product(
        p_name=product.p_name,
        price=product.price,
        owner_id=product.owner_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


#view product
@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session=Depends(get_db)):
    product=db.query(Product).filter(Product.p_id==product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

#delete product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session=Depends(get_db)):
    product=db.query(Product).filter(Product.p_id==product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}

#join product name and owner name
@app.get("/products-with-owner/{product_id}")
def get_product_with_owner(product_id: int, db: Session=Depends(get_db)):
    product=db.query(Product).filter(Product.p_id==product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "product_name": product.p_name,
        "owner_name": product.owner.u_name
    }







