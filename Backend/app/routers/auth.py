from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth_services import AuthService
from app.schemas.auth import UserLogin, UserRegister,Token
from app.dependencies.auth import get_current_user
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user:UserRegister, db:Session=Depends(get_db)):
    auth_service=AuthService(db)
    return auth_service.register_user(user)

@router.post("/login",response_model=Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    auth_service=AuthService(db)
    user=UserLogin(email=form_data.username,password=form_data.password)
    return auth_service.login_user(user)

@router.get("/me")
def get_me(current_user:User=Depends(get_current_user)):
    return current_user
