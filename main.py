from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, APIRouter, Depends
from datetime import datetime
import uuid
import random
from typing import Final
from time import sleep
import logger.app_logger as app_logger
from logger.app_logger_formatter import CustomFormatter
from sqlalchemy.orm import Session
from database import SessionLocal, Base, alchemy_connection
from models import Message
from sqlalchemy.sql import text
from os import listdir
from os.path import isfile, join

formatter = CustomFormatter('%(asctime)s')
app = FastAPI()
prefix_router = APIRouter(prefix="/Stage")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create the tables in the database
Base.metadata.create_all(bind=alchemy_connection)


@prefix_router.get("/message")
async def get_all(db: Session = Depends(get_db)):
    cmd = "SELECT * FROM messages"
    result = db.execute(text(cmd))
    return result.all()

@prefix_router.post("/message")
async def add_item(message: dict, db: Session = Depends(get_db)):
    name_ = message['name']
    data_ = message['data']
    db.add(Message(message_name=name_, data=data_))
    db.commit()
    return {'id': uuid.uuid1(),
            'name': name_,
            'data': data_,
            'timestamp': datetime.now()}

@prefix_router.get("/files/{path}")
def files(path: str):
    return [f for f in listdir(path) if isfile(join(path, f))]

@prefix_router.get("/names/{name}")
def files(name: str):
    return name.title()


@prefix_router.get("/time")
def routes():
    return datetime.now()
app.include_router(prefix_router)
