from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'message':'hello world'}

@app.get('/users/{id}')
async def get_user(id:int):
    return {'id':id}


from enum import Enum

# validating the values that are permissible for type
class UserType(str, Enum):
    STANDARD = 'standard'
    ADMIN = 'admin'

@app.get('/users/{type}/{id}')
async def get_user(type: UserType, id:int = Path(..., ge=1)):
    return {'type':type, 'id':id}

@app.get('/license-plates/{license}')
async def get_licence_plate(license: str = Path(..., regex = r"^w{2}-\d{3}-\w{2}$")):
    return {'license_plate': license}

# Query parameters is something we can also do
@app.get('/book')
async def get_page(page:int=1,size:int=2):
    return {'page' : page , 'size': size}

from fastapi import Form

# handles data in form format
@app.post('/users/form')
async def create_user_form(name: str = Form(...), age:int = Form(...)):
    return {'name': name, 'age': age}


from fastapi import File

# handles file uploads
# not sure why but I keep encountering an error 404 not found when run from here
# the issue is resolved when this function is in another py file
@app.post('/files')
async def create_file(file: bytes = File(...)):
    return {'message': 'test'}
    #return {'file size': len(file)}


from pydantic import BaseModel
