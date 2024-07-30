from fastapi import FastAPI
from pydantic import BaseModel, Field
import enum
from datetime import datetime
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn

from src.skins.routers.skin_router import skin_router
from src.skins.routers.store_skin_router import store_skin_router

app = FastAPI(
    title="Skins"
)

app.include_router(skin_router)
app.include_router(store_skin_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
