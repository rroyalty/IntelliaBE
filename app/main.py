from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes.lessons import *
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static/templates")

app.include_router(router)

@app.get('/list')
def show_list(request: Request):
    data = requests.get(request.url_for('read_lessons')).json()
    print(data)
    return templates.TemplateResponse("list.html", {"request": request, "data": data})
    