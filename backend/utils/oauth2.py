from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from typing import Optional

from db.crud_user import read_user_by_username
from db.database import get_db
from db.models import UserModel


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

# SECRET_KEY GENERATION COMMAND - openssl rand -hex 32
SECRET_KEY = 'e81f6eede00c2a55065c23408c26d4fc0789976be493adf934481114bc28bc84'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt


def get_current_user(
    token: str = Depends(oauth2_schema),
    db: Session = Depends(get_db)
    ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not Validate Credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user = read_user_by_username(username, db)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # user = read_user_by_username(username, db)
    # if username is None:
    #         raise credentials_exception

    return user
