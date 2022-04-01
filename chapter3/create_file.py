from fastapi import File, FastAPI

app = FastAPI()

# handles file uploads
# http --form POST localhost:8000/files file@cat.jpg
@app.post('/files')
async def create_file(file: bytes = File(...)):
    #return {'message': 'test'}
    return {'file size': len(file)}


# reading from an uploaded file that deals with it under a different format
# http --form POST localhost:8000/files/upload file@cat.jpg
from fastapi import UploadFile

@app.post('/files/upload')
async def upload_file(file:UploadFile = File(...)):
    return {'file_name': file.filename,
            'content_type': file.content_type}

# uploading multiple files
# http --form POST localhost:8000/files/upload/multiple files@cat.jpg files@cat.jpg
from typing import List 

@app.post('/files/upload/multiple')
async def upload_multiple_files(files:List[UploadFile] = File(...)):
    return [{'file_name': file.filename,
            'content_type': file.content_type}
            for file in files]