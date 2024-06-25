from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from src.config import settings


sync_engine = create_engine(url=settings.database_url_psycopg2,
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
