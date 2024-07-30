from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter

from src.skins.pydantic_schemas import SkinModel
from src.skins.services.skin_service import SkinService
from src.dependencies import skins_service
from src.skins.repositories.skin_repository import SkinRepository

skin_router = APIRouter(
    prefix="/skins",
    tags=["Skin"]
)


@skin_router.get("/",
                 description="Получить список всех скинов, которые были "
                             "внесены в сервис.",
                 response_model=list[SkinModel]
)
async def get_all_skins(skins_service: Annotated[SkinService, Depends(skins_service)]):
    return await skins_service.get_all_skins()


@skin_router.get("/{skin_name}")
async def get_skin(skin_name: str):
    response = await SkinService(SkinRepository).get_skin(skin_name)
    return response


@skin_router.post("/")
async def add_post():
    ...


@skin_router.put("/")
async def skin_full_update():
    ...
