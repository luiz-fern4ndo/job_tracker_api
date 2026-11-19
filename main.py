from fastapi import FastAPI

from database import engine
from models.base import table_registry
from routes.applications import router as application_router

app = FastAPI()

table_registry.metadata.create_all(engine)

app.include_router(application_router)
