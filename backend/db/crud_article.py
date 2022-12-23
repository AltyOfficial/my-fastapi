from sqlalchemy.orm import Session

from db.models import ArticleModel
from db.schemas import ArticleSchema


def create_article(request: ArticleSchema, db: Session):
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
    return article
