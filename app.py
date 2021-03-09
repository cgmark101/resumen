import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, date
from deta import Deta 
from fastapi.responses import HTMLResponse
import starlette.status as status

today = date.today()
now = datetime.now()

current_date = today.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")


key = 'b08z8w5z_svn4Ez3GNhn7DpZkSumBYjjNborFy4Yb'
deta = Deta(key)
db = deta.Base("contact")

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse, name='index')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

"""
@app.get('/styles', response_class=HTMLResponse, name='styles')
async def style(request: Request):
    return templates.TemplateResponse("styles.html", {"request": request})


@app.post('/form')
async def email(
    request: Request,
    contactName: str = Form(...), 
    contactEmail: str = Form(...), 
    contactSubject: str = Form(...), 
    contactMessage: str = Form(...)):
    db.insert({
        'nombre':contactName, 
        'email':contactEmail, 
        'sujeto':contactSubject, 
        'mensaje':contactMessage,
        'fecha':current_date,
        'hora':current_time
        })
    #return RedirectResponse('/ok', status_code=status.HTTP_302_FOUND)
    return 'ok'

 @app.get('/ok', response_class=HTMLResponse, name='styles')
async def ok(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})  """