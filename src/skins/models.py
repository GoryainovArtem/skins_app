from typing import Annotated
import enum

from sqlalchemy import ForeignKey, CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True,
                                     nullable=False)]

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }


class GameItemTypes(enum.Enum):
    rifle = "Винтовка"
    sniper_rifle = "Снайперская винтовка"
    pistol = "Пистолет"
    knife = "Нож"
    machine_pistol = "Пистолет-пулемет"
    machinegun = "Пулемет"
    shotgun = "Дробовик"
    gloves = "Перчатки"
    sticker = "Наклейка"
    case = "Кейс"


class WearConditions(enum.Enum):
    fn = "Прямо с завода"
    mw = "Немного поношенный"
    ft = "После полевых испытаний"
    ww = "Поношенный"
    bs = "Закаленный в боях"


class GameItemORM(Base):
    __tablename__ = "skins_game_items"
    __table_args__ = {"schema": "skins"}
    id: Mapped[intpk]
    name_rus: Mapped[str] = mapped_column(unique=True)
    name_eng: Mapped[str] = mapped_column(unique=True)
    type: Mapped[GameItemTypes]
    skins: Mapped[list["SkinORM"]] = relationship()


class CaseTypeORM(Base):
    __tablename__ = "skins_case_types"
    __table_args__ = {"schema": "skins"}
    id: Mapped[intpk]
    name_rus: Mapped[str] = mapped_column(unique=True)
    name_eng: Mapped[str] = mapped_column(unique=True)
    image_url: Mapped[str] = mapped_column(unique=True) # Нужна URL валидация
    skins: Mapped[list["SkinORM"]] = relationship()


class RarityORM(Base):
    __tablename__ = "skins_rarities"
    __table_args__ = {"schema": "skins"}
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(unique=True)
    hex_color: Mapped[str] = mapped_column() # Валидация на длину в 7 символов и 1 символ #
    skins: Mapped[list["SkinORM"]] = relationship()


class SkinORM(Base):
    __tablename__ = "skins_skins"
    __table_args__ = {"schema": "skins"}
    id: Mapped[intpk]
    id_rarity: Mapped[int] = mapped_column(ForeignKey("skins.skins_rarities.id",
                                                      ondelete="RESTRICT") #  + поле is_active
                                             # protected - по умолчанию
                                             )
    rarity: Mapped["RarityORM"] = relationship()

    id_game_item: Mapped[int] = mapped_column(ForeignKey("skins.skins_game_items.id",
                                                         ondelete="RESTRICT")
                                              )
    game_item: Mapped["GameItemORM"] = relationship()

    id_case_type: Mapped[int] = mapped_column(ForeignKey("skins.skins_case_types.id",
                                                         ondelete="RESTRICT")
                                              )
    case_type: Mapped["CaseTypeORM"] = relationship()

    name_rus: Mapped[str] = mapped_column()
    name_eng: Mapped[str] = mapped_column()
    image_url: Mapped[str] = mapped_column()


# class StoreSkinORM(Base):
#     __tablename__ = "store_skins"
#
#     id_store_skin = ...
#     id_skin = ...
#     id_wear_condition = ...


# class Customer(Base):
#     ...
