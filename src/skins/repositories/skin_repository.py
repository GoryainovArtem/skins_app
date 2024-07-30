from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.skins.repositories.repository import SQLAlchemyRepository
from sqlalchemy.orm import aliased
from src.skins.models import SkinORM, GameItemORM, GameItemTypeORM, RarityORM
from src.database import async_session_factory
from src.skins.pydantic_schemas import SkinModel
from src.utils.utils import slugify


class SkinRepository(SQLAlchemyRepository):
    model = SkinORM

    async def get_all(self):
        async with async_session_factory() as session:
            # s = aliased(SkinORM)
            # r = aliased(RarityORM)
            # query = select(s).join(r, s.id_rarity == r.id)
            # subquery load

            query = select(SkinORM).options(joinedload(SkinORM.rarity),
                                            joinedload(SkinORM.game_item).joinedload(GameItemORM.game_item_type),
                                            joinedload(SkinORM.case_type)
                                            )
            data = await session.execute(query)
            return data.scalars().all()

    async def get_skin(self, skin_name: str):

        skin_name = slugify(skin_name)
        async with async_session_factory() as session:
            query = select(SkinORM).options(joinedload(SkinORM.rarity),
                                            joinedload(SkinORM.game_item).joinedload(GameItemORM.game_item_type),
                                            joinedload(SkinORM.case_type)
                                            ).where(self.model.name_eng == skin_name)
            data = await session.execute(query)
            obj = data.scalars().first()

            item_dict = obj.__dict__
            item_dict["hyperlink_url"] = "http:/12442"
            return SkinModel(**item_dict)