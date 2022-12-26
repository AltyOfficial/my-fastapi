import shutil

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse


router = APIRouter(
    prefix='/file',
    tags=['file']
)


# Simple File with a small size
@router.post('/')
def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}


# Upload Larger Files
@router.post('/upload/')
def get_upload_file(upload_file: UploadFile = File(...)):
    path = f'media/images/{upload_file.filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return {
        'filename': path,
        'type': upload_file.content_type
    }


#Returning a File
@router.get('/download/{name}/', response_class=FileResponse)
def download_file(name: str):
    path = f'media/images/{name}.png'
    return path
