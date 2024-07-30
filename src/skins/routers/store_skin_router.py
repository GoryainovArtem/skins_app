from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.skins.services.store_skin_service import StoreSkinService
from src.skins.repositories.store_skin_repository import StoreSkinRepository
from src.skins.pydantic_schemas import StoreSkinItemModel

store_skin_router = APIRouter(
    prefix="/store_skins",
    tags=["Store_skin"]
)


@store_skin_router.get("/", description="Получить список всех скинов, "
                                        "которые были добавлены в сервис",
                       response_model=list[StoreSkinItemModel])
async def get_all_store_skins():
    return await StoreSkinService(StoreSkinRepository).get_all_store_skins()


@store_skin_router.get("/{id}", description="Получить конкретный скин, "
                                            "который был добавлен в сервис",
                       response_model=StoreSkinItemModel)
async def get_store_skin(assert_id: int):
    return await StoreSkinService(StoreSkinRepository).get_store_skin(assert_id)


