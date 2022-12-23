from pydantic import BaseModel
from typing import List


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserArticleSchema(BaseModel):
    title: str
    text: str
    published: bool

    class Config():
        orm_mode = True


class UserDisplaySchema(BaseModel):
    username: str
    email: str
    articles: List[UserArticleSchema] = []

    class Config():
        orm_mode = True


class ArticleSchema(BaseModel):
    title: str
    text: str
    published: bool
    owner_id: int


class ShortUserDisplaySchema(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True


class ArticleDisplaySchema(BaseModel):
    title: str
    text: str
    published: bool
    owner: ShortUserDisplaySchema

    class Config():
        orm_mode = True

