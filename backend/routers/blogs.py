from fastapi import APIRouter


router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)


@router.get('/')
def index():
    return {'detail': 'hello world!'}
