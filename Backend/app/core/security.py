from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from jose import jwt,JWTError
from passlib.context import CryptContext
from app.core.config import settings
from uuid import UUID

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str)->bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user_id:UUID)->str:
    expire= datetime.now(timezone.utc)+timedelta(days=30)
    to_encode={"exp": expire, "sub": str(user_id)}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_access_token(token:str)->UUID:
    try:
        payload=jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id=payload.get("sub")
        if user_id is None:
            raise ValueError("Invalid token")
        return UUID(user_id)
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e
    
