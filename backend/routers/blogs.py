from fastapi import APIRouter, Body

from db import schemas
from routers.logger import log


router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)


# Logging
@router.get('/')
def index():
    log('my-fastapi', 'successed')
    return {'detail': 'hello world!'}


# @router.post('/bands/')
# def band_create(request: schemas.Band, instrument: str = Body(...)):
#     return {
#         'band': request,
#         'instrument': instrument
#     }
