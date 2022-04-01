from fastapi import FastAPI, Header

app = FastAPI()

# retrieves the header
@app.get('/header')
async def get_header(user_agent:str = Header(...)):
    return {'user_agent':user_agent}


from fastapi import Response

@app.get('/header/custom')
async def custom_header(response : Response):
    response.headers['Custom-Header'] = 'Custom value, anything you want'
    #return{'message':'hello'}

from fastapi import Cookie
from typing import Optional

# retrieves the cookie
@app.get('/cookie')
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {'hello':hello}