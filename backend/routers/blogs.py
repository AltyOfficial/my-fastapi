from fastapi import APIRouter, Body

from db import schemas


router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)


@router.get('/')
def index():
    return {'detail': 'hello world!'}


# @router.post('/bands/')
# def band_create(request: schemas.Band, instrument: str = Body(...)):
#     return {
#         'band': request,
#         'instrument': instrument
#     }


def required_functionality():
    return {'message': 'learning fastAPI'}
