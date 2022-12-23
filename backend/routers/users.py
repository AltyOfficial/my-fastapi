from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.crud import create_user
from db.schemas import UserDisplaySchema, UserSchema


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', response_model=UserDisplaySchema)
def user_create(request: UserSchema, db: Session = Depends(get_db)):
    return create_user(request, db)
