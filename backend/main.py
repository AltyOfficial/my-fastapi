import time

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocket

from db import models, database
from routers import articles, auth, blogs, users, products, file, templates
from utils.exceptions import HelloException
from routers.client import html


app = FastAPI()

models.Base.metadata.create_all(database.engine)


@app.exception_handler(HelloException)
def hello_exception_handler(request: Request, exc: HelloException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={'detail': exc.title}
    )

# 3 next lines - websockets examples
@app.get('/')
async def get():
    return HTMLResponse(html)


clients = []


@app.websocket('/chat/')
async def websocket(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]


# Adding Custom Middleware
@app.middleware('http')
async def add_custom_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time()- start_time
    response.headers['duration'] = str(duration)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.mount('/media/', StaticFiles(directory='media/'), name='media')


app.include_router(auth.router)
app.include_router(articles.router)
app.include_router(blogs.router)
app.include_router(file.router)
app.include_router(products.router)
app.include_router(templates.router)
app.include_router(users.router)
