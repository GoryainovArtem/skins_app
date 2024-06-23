import dataclasses
import os

from dotenv import load_dotenv

load_dotenv()


@dataclasses.dataclass
class Settings:
    DB_HOST: str
    DB_NAME: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str

    @property
    def database_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def database_url_psycopg2(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings(DB_HOST=os.getenv("DB_HOST"), DB_NAME=os.getenv("DB_NAME"),
                    DB_PORT=os.getenv("DB_PORT"), DB_USER=os.getenv("DB_USER"),
                    DB_PASS=os.getenv("DB_PASS"))
