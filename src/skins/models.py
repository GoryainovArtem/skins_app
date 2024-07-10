from typing import Annotated
import enum
from abc import ABC
from datetime import datetime

from sqlalchemy import ForeignKey, CheckConstraint, String, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True,
                                     nullable=False)]

str_256 = Annotated[str, 256]
str_7 = Annotated[str, 7]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256),
        str_7: String(7)
    }


class BaseMixin(Base):
    __abstract__ = True

    id: Mapped[intpk]
    add_dttm: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('UTC', now())"),
                                               nullable=False)
    update_dttm: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('UTC', now())"),
                                                  nullable=False)


class NameMixin(BaseMixin):
    __abstract__ = True

    name_rus: Mapped[str_256] = mapped_column(unique=True, nullable=False)
    name_eng: Mapped[str_256] = mapped_column(unique=True, nullable=False)


class ImageMixin(NameMixin):
    __abstract__ = True

    image_url: Mapped[str_256] = mapped_column(unique=True, nullable=False)


class WearConditionORM(NameMixin):
    __tablename__ = "skins_wear_conditions"
    __table_args__ = {"schema": "skins"}
    skins: Mapped[list["StoreSkinORM"]] = relationship(back_populates="wear_condition")


class GameItemTypeORM(NameMixin):
    """Модель категории игрового предмета."""
    __tablename__ = "skins_game_item_types"
    __table_args__ = {"schema": "skins"}
    game_items: Mapped[list["GameItemORM"]] = relationship(back_populates="game_item_type")


class GameItemORM(BaseMixin):
    """Модель игрового предмета."""
    __tablename__ = "skins_game_items"
    __table_args__ = {"schema": "skins"}
    name: Mapped[str_256] = mapped_column(unique=True, nullable=False)
    id_item_type: Mapped[int] = mapped_column(ForeignKey("skins.skins_game_item_types.id",
                                                         ondelete="RESTRICT"),
                                              nullable=False)
    game_item_type: Mapped["GameItemTypeORM"] = relationship(back_populates="game_items")
    skins: Mapped[list["SkinORM"]] = relationship(back_populates="game_item")


class CaseTypeORM(ImageMixin):
    __tablename__ = "skins_case_types"
    __table_args__ = (
        CheckConstraint("image_url LIKE 'http%' ",
                        name='url_validator'),
        {"schema": "skins"}
    )
    skins: Mapped[list["SkinORM"]] = relationship(back_populates="case_type")


class RarityORM(BaseMixin):
    __tablename__ = "skins_rarities"
    __table_args__ = (
        CheckConstraint("hex_color LIKE '#%'", name='hex_color_first_letter'),
        CheckConstraint("LENGTH(hex_color) = 7", name='hex_color_length'),
        {"schema": "skins"}
    )
    name: Mapped[str_256] = mapped_column(unique=True, nullable=False)
    hex_color: Mapped[str_7] = mapped_column()
    skins: Mapped[list["SkinORM"]] = relationship(back_populates="rarity")
    stickers: Mapped[list["StickerTypeORM"]] = relationship(back_populates="rarity")


class SkinORM(ImageMixin):
    __tablename__ = "skins_skins"
    __table_args__ = (
        CheckConstraint("image_url LIKE 'http%'",
                        name='url_validator'),
        {"schema": "skins"}
    )
    id_rarity: Mapped[int] = mapped_column(ForeignKey("skins.skins_rarities.id",
                                                      ondelete="RESTRICT")
                                           )
    rarity: Mapped["RarityORM"] = relationship(back_populates="skins")

    id_game_item_type: Mapped[int] = mapped_column(ForeignKey("skins.skins_game_items.id",
                                                              ondelete="RESTRICT")
                                                   )
    game_item: Mapped["GameItemORM"] = relationship(back_populates="skins")

    id_case_type: Mapped[int] = mapped_column(ForeignKey("skins.skins_case_types.id",
                                                         ondelete="RESTRICT")
                                              )
    case_type: Mapped["CaseTypeORM"] = relationship(back_populates="skins")


class StickerTypeORM(ImageMixin):
    __tablename__ = "skins_sticker_types"
    __table_args__ = {"schema": "skins"}
    id_rarity: Mapped[int] = mapped_column(ForeignKey("skins.skins_rarities.id",
                                                      ondelete="RESTRICT")
                                           )
    image_url: Mapped[str_256] = mapped_column(CheckConstraint("image_url LIKE 'http%' ",
                                                               name='url_validator'),
                                               unique=True, nullable=False)
    rarity: Mapped["RarityORM"] = relationship(back_populates="stickers")
    store_sticker_skins: Mapped[list["StoreSkinStickerORM"]] = relationship(back_populates="sticker")


class StoreItemORM(BaseMixin):
    __tablename__ = "skins_store_items"
    __table_args__ = {"schema": "skins"}
    id_owner: Mapped[int] = mapped_column()
    assert_id: Mapped[int] = mapped_column()
    store_skin_item: Mapped["StoreSkinORM"] = relationship(back_populates="store_item")


class StoreSkinORM(BaseMixin):
    __tablename__ = "skins_store_skins"
    __table_args__ = (
        CheckConstraint('pattern > 0 and pattern < 1000',
                        name='pattern_limits'),
        CheckConstraint('skin_float > 0.0 and skin_float < 1.0',
                        name='pattern_limits_2'),
        {"schema": "skins"}
    )
    id: Mapped[intpk]
    id_store_item: Mapped[int] = mapped_column(ForeignKey("skins.skins_store_items.id",
                                                          ondelete="RESTRICT"),
                                               nullable=False
                                               )
    store_item: Mapped[StoreItemORM] = relationship(back_populates="store_skin_item")
    id_wear_condition: Mapped[int] = mapped_column(ForeignKey("skins.skins_wear_conditions.id", ondelete="RESTRICT"),
                                                   nullable=False
                                                   )
    wear_condition: Mapped[WearConditionORM] = relationship(back_populates="skins")
    pattern: Mapped[int] = mapped_column(nullable=False)
    skin_float: Mapped[float] = mapped_column(nullable=False)
    is_stattrack: Mapped[bool] = mapped_column(nullable=False,
                                               server_default=text('false')
                                               )
    store_skin_stickers: Mapped[list["StoreSkinStickerORM"]] = relationship(back_populates="store_skin")


class StoreSkinStickerORM(BaseMixin):
    """
    Many to many таблица для хранения информации о нанесенных на
    скины стикерах.
    """
    __tablename__ = "skins_store_skins_stickers"
    __table_args__ = (
        CheckConstraint("position >= 1 AND position <= 4",
                        name="position_min_max"),
        {"schema": "skins"}
    )
    id_sticker: Mapped[int] = mapped_column(ForeignKey("skins.skins_sticker_types.id"),
                                            nullable=False)
    id_store_skin: Mapped[int] = mapped_column(ForeignKey("skins.skins_store_skins.id"),
                                               nullable=False)
    sticker: Mapped["StickerTypeORM"] = relationship(back_populates="store_sticker_skins")
    store_skin: Mapped["StoreSkinORM"] = relationship(back_populates="store_skin_stickers")
    position: Mapped[int] = mapped_column()
