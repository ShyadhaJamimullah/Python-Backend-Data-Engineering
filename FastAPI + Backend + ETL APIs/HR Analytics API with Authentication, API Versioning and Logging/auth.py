from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

security=HTTPBearer()

def verify_token(
    credentials: HTTPAuthorizationCredentials=Depends(security)
):
    token=credentials.credentials

    if token!=os.getenv("API_TOKEN"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token"
        )

    return "authorized"