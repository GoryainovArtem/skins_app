from pydantic_sqlalchemy_2 import sqlalchemy_to_pydantic
import models


RaritySchema = sqlalchemy_to_pydantic(models.RarityORM)
