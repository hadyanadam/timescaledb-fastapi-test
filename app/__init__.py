from fastapi import FastAPI
from .config import DATABASE_URI
from . import routers

app = FastAPI()

app.include_router(routers.api)