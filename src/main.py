from fastapi import FastAPI
from pydantic import BaseModel, Field
import enum
from datetime import datetime
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# from src.skins.router import router as router_skins

app = FastAPI(
    title="Skins"
)

#app.include_router(router_skins)


# @app.exception_handler(ResponseValidationError)
# async def validation_exception_handler(request, exc: ResponseValidationError):
#     return JSONResponse(
#         status_code=422,
#         content=jsonable_encoder({"detail": exc.errors()})
#     )
#
#
# class DegreeType(enum.Enum):
#     newbie = "newbie"
#     expert = "expert"
#
#
# class Degree(BaseModel):
#     id: int
#     dttm: datetime
#     degree_type: DegreeType
#
#
# class GameItem(BaseModel):
#     id: int = Field(ge=0)
#     name: str = Field(max_length=100)
#     type: str
#     degree: list[Degree] = []
#
#
# fake_items = [
#     {"id": 1, "name": "M4A4", "type": 123}
# ]
#
#
# @app.get("/")
# def hello():
#     return "Hello, world!"
#
#
# @app.get("/game_items/{item_id}")
# def get_game_item(item_id: int):
#     return [item for item in fake_items if item.get("id") == item_id]
#
#
# @app.get("/game_items/", response_model=list[GameItem])
# def get_items(limit: int = 10, offset: int = 10):
#     return fake_items[offset:][:limit]
#
#
# @app.patch("/game_items/{item_id}")
# def update_game_item(item_id: int, new_name: str):
#     items = filter(lambda x: x.get("id") == item_id, fake_items)
#     item = next(items)
#     item["name"] = new_name
#     return {"status_code": 200,
#             "message": "successfully updated"}
#
#
# @app.post("/game_items/")
# def add_game_item(game_items: list[GameItem]):
#     fake_items.extend(game_items)
#     return {"status_code": 200,
#             "content": fake_items}
#
#
# # def create_tables():
# #     models.Base.metadata.drop_all(sync_engine)
# #     models.Base.metadata.create_all(sync_engine)
