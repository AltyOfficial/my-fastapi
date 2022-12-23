from sqlalchemy.orm import Session

from db.database import SessionLocal
from db.models import User
from db.schemas import UserSchema
from utils.hashing import Hash


def create_user(request: UserSchema, db: Session):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
