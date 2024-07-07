from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

from src.skins.models import RarityORM

router = APIRouter(
    prefix="/rarities",
    tags=["Skin"]  # Это что
)


@router.get("/")
async def get_rarities(session: AsyncSession = Depends(get_async_session)):
    query = select(RarityORM)
    print(1)
    data = await session.execute(query)
    print(2)
    return data.scalars().all()
