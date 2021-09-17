from fastapi import FastAPI, Request
from pydantic.networks import HttpUrl
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

app.include_router(router)

@app.get('/list')
def show_list(request: Request):
    data = requests.get(request.url_for('read_lessons'))
    print(data)