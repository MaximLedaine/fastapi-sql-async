import sqlalchemy
from fastapi import Depends, FastAPI, APIRouter
from .database import database, DATABASE_URL, metadata
from .routers import notes

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

router = APIRouter()

@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()

router.include_router(notes.router)

