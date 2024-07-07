from sqlalchemy import select, func, cast, Integer, and_
from sqlalchemy.orm import aliased

import models
from src.config import settings
from src.database import sync_session_factory


def get_with_lazy_relationship():
    with sync_session_factory() as session:
        query = select(models.RarityORM.rarity_name,
                       cast(func.avg(models.RarityORM.id_rarity), Integer).label("avg_data")
                       ).group_by(models.RarityORM.rarity_name)
        data = session.execute(query)
        return data.all()


def query_with_join():
    with sync_session_factory() as session:
        r = aliased(models.RarityORM)
        query = select(r)
        data = session.execute(query)
        return data.scalars().all()


def lazy_select():
    with sync_session_factory() as session:
        query = select(models.RarityORM)
        data = session.execute(query)
        rarity_1 = data.scalars().all()[1]
        return rarity_1.skins


if __name__ == "__main__":
    data = lazy_select()
    print(data)
