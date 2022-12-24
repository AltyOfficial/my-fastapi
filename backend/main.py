from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from db import models, database
from routers import articles, blogs, users, products
from utils.exceptions import HelloException


app = FastAPI()

models.Base.metadata.create_all(database.engine)


@app.exception_handler(HelloException)
def hello_exception_handler(request: Request, exc: HelloException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={'detail': exc.title}
    )


origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(articles.router)
app.include_router(blogs.router)
app.include_router(products.router)
app.include_router(users.router)
