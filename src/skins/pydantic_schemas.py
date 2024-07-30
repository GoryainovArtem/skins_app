from datetime import datetime

import pydantic


class BaseORMModel(pydantic.BaseModel):
    class Config:
        orm_mode = True


class RarityModel(BaseORMModel):
    name: str
    hex_color: str


class GameItemTypeModel(BaseORMModel):
    id: int
    name_rus: str
    name_eng: str


class GameItemModel(BaseORMModel):
    id: int
    name: str
    game_item_type: GameItemTypeModel


class CaseTypeModel(BaseORMModel):
    id: int
    name_rus: str
    name_eng: str
    image_url: str


class SkinModel(BaseORMModel):
    name_rus: str
    name_eng: str
    rarity: RarityModel
    image_url: str
    game_item: GameItemModel
    case_type: CaseTypeModel
    # hyperlink_url: str
    # slug: str


class WearConditionModel(BaseORMModel):
    name_rus: str
    name_eng: str


class StoreItemModel(BaseORMModel):
    id_owner: int
    assert_id: int
    #store_skin_item: St


class StoreSkinItemModel(BaseORMModel):
    pattern: int
    skin_float: float
    is_stattrack: bool
    wear_condition: WearConditionModel
    skin: SkinModel
