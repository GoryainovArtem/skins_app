from backend.app.database.database import sync_engine, async_engine, sync_session_factory
from sqlalchemy import select, text
from backend.app.database.models import RarityORM


def select_data(name):
    with sync_engine.connect() as conn:
        stmt = text("SELECT * FROM rarities WHERE rarity_name=:rarity")
        stmt = stmt.bindparams(rarity=name)
        data = conn.execute(stmt)
        print(data.all())


def select_data_orm():
    with sync_session_factory() as session:
        item = session.get(RarityORM, 1)
        print(item.rarity_name)


select_data_orm()
