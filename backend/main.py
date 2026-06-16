from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

from backend.api import router

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

app.include_router(router)