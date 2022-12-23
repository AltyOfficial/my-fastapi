import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import List, Optional

from db.database import Base


class UserModel(Base):
    """Model For User."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    articles = relationship('ArticleModel', back_populates='owner')


class ArticleModel(Base):
    """Model For Article."""

    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    published = Column(Boolean)
    owner_id = Column(Integer, ForeignKey('users.id'))
    pub_date = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship('UserModel', back_populates='articles')
