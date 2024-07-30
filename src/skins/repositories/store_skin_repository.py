from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from src.skins.repositories.repository import AbstractRepository
from src.skins.models import StoreSkinORM, SkinORM, GameItemORM
from src.database import async_session_factory


class StoreSkinRepository(AbstractRepository):
    model = StoreSkinORM

    async def get_all(self):
        async with async_session_factory() as session:
            query = select(self.model).options(joinedload(self.model.wear_condition),
                                               joinedload(self.model.skin).joinedload(SkinORM.rarity),
                                               joinedload(self.model.skin).joinedload(SkinORM.game_item).joinedload(GameItemORM.game_item_type),
                                               joinedload(self.model.skin).joinedload(SkinORM.case_type)
                                               )
            data = await session.execute(query)
            return data.scalars().all()

    async def get_object(self, skin_name: str):
        # Преобразовать из slug в название
        async with async_session_factory() as session:
            ...
            #query = select(self.model).where()
