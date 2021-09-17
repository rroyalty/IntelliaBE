from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
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

#Template Routes

#Route for viewing the list of all lesson plans.
@app.get('/list')
def show_list(request: Request):
    data = requests.get(request.url_for('read_lessons')).json()
    return templates.TemplateResponse("list.html", {"request": request, "data": data})

#Route for viewing a single lesson plan.
@app.get('/view/{id_param}')
def show_lesson(request: Request, id_param: int):
    data = requests.get(request.url_for('read_lesson', id=id_param)).json()
    return templates.TemplateResponse("view.html", {"request": request, "data": data})

#Route for deleteing a lesson plan.
@app.get('/delete/{id_param}')
def show_lesson(request: Request, id_param: int):
    requests.delete(request.url_for('delete_lesson', id=id_param))
    return RedirectResponse(url="/list")

#Route for deleteing a lesson plan.
@app.get('/new')
def show_lesson(request: Request, id_param: int):
    requests.delete(request.url_for('delete_lesson', id=id_param))
    return RedirectResponse(url="/list")
