from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User   
from app.repositories.user_repositories import UserRepository
from app.schemas.auth import UserLogin, UserRegister
from app.core.security import hash_password,verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def register_user(self, user_register: UserRegister):
        existing_user = self.user_repository.get_user_by_email(user_register.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        hashed_password = hash_password(user_register.password)
        new_user = self.user_repository.create_user(User(email=user_register.email, password_hash=hashed_password))
        print("New account created successfully")
        return new_user

    def login_user(self, user_login: UserLogin):
        user = self.user_repository.get_user_by_email(user_login.email)
        if not user or not verify_password(user_login.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        access_token = create_access_token(user.id)
        return {"access_token": access_token, "token_type": "bearer"}
