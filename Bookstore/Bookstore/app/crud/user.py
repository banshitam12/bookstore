from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate
from app.utils.hashing import get_password_hash

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password_hash=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
