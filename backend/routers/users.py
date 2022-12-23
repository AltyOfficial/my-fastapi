from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.crud_user import (create_user, list_user, read_user, 
                          update_user, delete_user)
from db.schemas import UserDisplaySchema, UserSchema, ShortUserDisplaySchema


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/', response_model=List[ShortUserDisplaySchema])
def user_list(db: Session = Depends(get_db)):
    return list_user(db)


@router.post('/', response_model=UserDisplaySchema)
def user_create(request: UserSchema, db: Session = Depends(get_db)):
    return create_user(request, db)


@router.get('/{id}/', response_model=UserDisplaySchema)
def user_detail(id: int, db: Session = Depends(get_db)):
    return read_user(id, db)


@router.put('/{id}/', response_model=UserDisplaySchema)
def user_update(id: int, request: UserSchema, db: Session = Depends(get_db)):
    return update_user(id, request, db)


@router.delete('/{id}/')
def user_delete(id: int, db: Session = Depends(get_db)):
    return delete_user(id, db)
