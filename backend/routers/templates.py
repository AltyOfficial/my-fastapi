from fastapi import APIRouter
from fastapi.background import BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from db.schemas import ProductSchema
from routers.logger import log


router = APIRouter(
    prefix='/templates',
    tags=['templates']
)


templates = Jinja2Templates(directory='templates')


# Background Task Example
def log_template_call(message: str):
    log('my-fastapi', message)


@router.post('/product/{id}/', response_class=HTMLResponse)
def product_detail(id: int, request: Request,
    product: ProductSchema, bt: BackgroundTasks):

    bt.add_task(log_template_call('testing background task completed'))
    return templates.TemplateResponse(
        'product.html',
        {
            'request': request,
            'id': id,
            'title': product.title,
            'description': product.description,
            'price': product.price,
        }
    )
