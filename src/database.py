from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema
from src.skins.models import Base

from src.config import settings


sync_engine = create_engine(
    url=settings.database_url_psycopg2,
    echo=True,
    pool_size=5,
    max_overflow=10
)

async_engine = create_async_engine(url=settings.database_url_asyncpg,
                                   echo=True,
                                   pool_size=5,
                                   max_overflow=10
                                   )

sync_session_factory = sessionmaker(bind=sync_engine)
async_session_factory = async_sessionmaker(bind=async_engine)


async def get_async_session():
    async with async_session_factory() as session:
        yield session


def create_schemas():
    with sync_engine.connect() as conn:
        if not sync_engine.dialect.has_schema(conn, "skins"):
            conn.execute(CreateSchema("skins"))
            conn.commit()


create_schemas()
