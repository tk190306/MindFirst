from uuid import UUID
from sqlalchemy.orm import Session
from app.models.profiles import Profile

class ProfileRepository:
    def __init__(self,db:Session):
        self.db=db
    def get_profile_by_user_id(self,user_id:UUID)->Profile|None:
        return self.db.query(Profile).filter(Profile.user_id==user_id).first()
    def create_profile(self,profile:Profile)->Profile:
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile
    def update_profile(self,profile:Profile)->Profile:
        self.db.merge(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile
    