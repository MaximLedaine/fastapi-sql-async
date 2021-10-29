import sqlalchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import metadata


notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
    Column('thee_id', ForeignKey('thee.id'))
)

thees = sqlalchemy.Table(
    "thee",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
)
