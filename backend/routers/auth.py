from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import UserModel
from utils.hashing import Hash
from utils.oauth2 import create_access_token


router = APIRouter(tags=['auth'])


@router.post('/token/')
def get_token(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    user = db.query(UserModel).filter(UserModel.username==request.username)
    user = user.first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Invalid Username'
        )
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid Password'
        )
    access_token = create_access_token(
        data={'sub': user.username}
    )

    return {
        'access_token': access_token,
        'type': 'Bearer'
    }
