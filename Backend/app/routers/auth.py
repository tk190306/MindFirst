from fastapi import APIRouter
from app.schemas.auth import UserLogin, UserRegister

router=APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user:UserRegister):
    return {"message":"User is registered","email":user.email}
