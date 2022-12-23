from fastapi import FastAPI

from db import models, database
from routers import blogs, users


app = FastAPI()

models.Base.metadata.create_all(database.engine)


app.include_router(blogs.router)
app.include_router(users.router)
