from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from src.skins import pydantic_schemas

from src.database import get_async_session

from src.skins import models


rarity_router = APIRouter(
    prefix="/rarities",
    tags=["Rarity"]  # Это что
)

# skin_router = APIRouter(
#     prefix="/skins",
#     tags=["Skin"]
# )


@rarity_router.get("/", response_model=list[pydantic_schemas.RarityModel])
async def get_rarities(session: AsyncSession = Depends(get_async_session)):
    query = select(models.RarityORM)
    data = await session.execute(query)
    return data.scalars().all()


# @skin_router.get("/")
# async def get_skins(session: AsyncSession = Depends(get_async_session)):
#     query = select(models.SkinORM)
#     data = await session.execute(query)
#     return data.scalars().all()

