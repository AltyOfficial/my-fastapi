from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.models import ArticleModel
from db.schemas import ArticleSchema
from utils.exceptions import HelloException


def create_article(request: ArticleSchema, db: Session):

    if request.text.startswith('Hello'):
        raise HelloException('please dont say hello')

    article = ArticleModel(
        title=request.title,
        text=request.text,
        published=request.published,
        owner_id=request.owner_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def read_article(id: int, db: Session):
    article = db.query(ArticleModel).filter(ArticleModel.id==id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='article not found'
        )
    return article
