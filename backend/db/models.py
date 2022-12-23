from sqlalchemy import Column, Integer, String
from typing import List, Optional

from db.database import Base


class User(Base):
    """Model For User."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

