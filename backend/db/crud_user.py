from sqlalchemy.orm import Session

from db.models import UserModel
from db.schemas import UserSchema
from utils.hashing import Hash


def list_user(db: Session):
    users = db.query(UserModel).all()
    return users


def create_user(request: UserSchema, db: Session):
    new_user = UserModel(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def read_user(id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id==id).first()
    return user


def update_user(id: int, request: UserSchema, db: Session):
    user = db.query(UserModel).filter(UserModel.id==id)
    user.update(dict(request))
    db.commit()
    return user.first()


def delete_user(id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id==id)
    user.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'deleted'}
