from fastapi import FastAPI
from app.api.v1 import api


app = FastAPI(title="Mock API")


app.include_router(api.router, prefix="/api/v1", tags=["Mock API"])
