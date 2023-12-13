from init_db import SessionLocal
from fastapi import FastAPI
from init_db import Base, engine
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models import Flat, Payment, Service, JsonField
from pydantic import BaseModel, condecimal
from datetime import date

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class JsonCreate(BaseModel):
    json_field: dict


class JsonResponse(BaseModel):
    id: int
    json_field: dict


class FlatCreate(BaseModel):
    owner: str
    street: str
    flat_num: int
    building_num: int


class FlatDelete(BaseModel):
    message: str


class FlatResponse(BaseModel):
    id: int
    owner: str
    street: str
    flat_num: int
    building_num: int


class PaymentCreate(BaseModel):
    sum: condecimal(max_digits=10, decimal_places=2)
    date_of_payment: date
    for_date: str

class PaymentDelete(BaseModel):
    message: str


class PaymentResponse(BaseModel):
    id: int
    sum: condecimal(max_digits=10, decimal_places=2)
    date_of_payment: date
    for_date: str

class ServiceCreate(BaseModel):
    price_per_month: condecimal(max_digits=10, decimal_places=2)
    name: str
    counter: bool


class ServiceDelete(BaseModel):
    message: str


class ServiceResponse(BaseModel):
    id: int
    price_per_month: condecimal(max_digits=10, decimal_places=2)
    name: str
    counter: bool


Base.metadata.create_all(engine)
