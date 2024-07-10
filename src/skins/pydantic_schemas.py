from datetime import datetime

import pydantic


class BaseORMModel(pydantic.BaseModel):
    class Config:
        orm_mode = True


class RarityModel(BaseORMModel):
    name: str
    hex_color: str
    id: int
    add_dttm: datetime
    update_dttm: datetime


class GameItemTypeModel(BaseORMModel):
    id: int
    name_rus: str
    name_eng: str
    add_dttm: datetime
    update_dttm: datetime


class GameItemModel(BaseORMModel):
    id: int
    name_rus: str
    name_eng: str
    add_dttm: datetime
    update_dttm: datetime


class SkinModel(BaseORMModel):
    id: int
    name_rus: str
    name_eng: str
    add_dttm: datetime
    update_dttm: datetime
