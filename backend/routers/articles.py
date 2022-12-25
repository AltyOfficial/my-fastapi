from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.crud_article import create_article, read_article
from db.schemas import ArticleSchema, ArticleDisplaySchema, UserSchema
from utils.oauth2 import oauth2_schema, get_current_user


router = APIRouter(
    prefix='/articles',
    tags=['articles']
)


@router.post('/', response_model=ArticleDisplaySchema)
def article_create(request: ArticleSchema, db: Session = Depends(get_db)):
    return create_article(request, db)


@router.get('/{id}/')#, response_model=ArticleDisplaySchema)
def article_detail(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)
    ):
    # return read_article(id, db)
    return {
        'data': read_article(id, db),
        'current_user': current_user
    }
