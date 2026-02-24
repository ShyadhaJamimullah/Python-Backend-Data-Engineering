from fastapi import Depends, HTTPException,status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from jose import JWTError,jwt
import os
from datetime import datetime, timedelta
from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hashed_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hash_password:str)->bool:
    return pwd_context.verify(plain_password, hash_password)



security=HTTPBearer()

SECRET_KEY=os.getenv("jwt_secret_key", "supersecretkey")
ALGORITHM="HS256"
JWT_EXPIRE_MINUTES=30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt(
    credentials: HTTPAuthorizationCredentials= Depends(security)
):
    token=credentials.credentials

    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

      
        user_id=payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )

        return payload  

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
