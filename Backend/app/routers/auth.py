from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth_services import AuthService
from app.schemas.auth import UserLogin, UserRegister,Token

router=APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user:UserRegister, db:Session=Depends(get_db)):
    auth_service=AuthService(db)
    return auth_service.register_user(user)

@router.post("/login",response_model=Token)
def login(user:UserLogin, db:Session=Depends(get_db)):
    auth_service=AuthService(db)
    return auth_service.login_user(user)
