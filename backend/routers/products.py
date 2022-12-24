from fastapi import APIRouter, Depends, Header, Cookie
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from sqlalchemy.orm import Session
from typing import Optional, List

from db.database import get_db
from db.crud_article import create_article, read_article
from db.schemas import ArticleSchema, ArticleDisplaySchema


router = APIRouter(
    prefix='/products',
    tags=['products']
)


product_list = ['watch', 'camera', 'pc', 'console', 'phone']


# Cookie Example
@router.get('/')
def product_list_f():
    data = ' '.join(product_list)
    response = Response(content=data, media_type='text/plain')
    response.set_cookie(key='test_cookie', value='test_cookie_value')
    response.set_cookie(key='test_cookie_two', value='test_cookie_value_two')
    return response


# Adding Header Example
@router.get('/header_test/')
def get_product(response: Response,
    custom_header: Optional[List[str]] = Header(None),
    test_cookie_two: Optional[str] = Cookie(None)):
    if custom_header:
        response.headers['test-header'] = ', '.join(custom_header)
    return {
        'data': product_list,
        'custom-header': custom_header,
        'my_cookie': test_cookie_two
    }


# Different Responses Example
@router.get('/{id}/', responses={
    200: {
        'content': {
            'text/html': {
                'example': '<div>Product name</div>'
            }
        },
        'description': 'HTML response'
    },
    404: {
        'content': {
            'text/plain': {
                'example': 'product not found'
            }
        }
    }
})
def product_detail(id: int):
    if id > len(product_list) - 1:
        output = 'Product not available'
        return PlainTextResponse(content=output,
                                 media_type='text/plain',
                                 status_code=404)
    product = product_list[id]
    output = f"""
    <head>
      <div>{product}</div>
    </head>
    """
    return HTMLResponse(content=output, media_type='text/html')
