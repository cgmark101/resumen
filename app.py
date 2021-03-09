import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import starlette.status as status

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse, name='index')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/ok', response_class=HTMLResponse, name='styles')
async def ok(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})