from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from init_db import Base, engine, SessionLocal
from models import Payment, Service, Flat, JsonField
from pydantic import BaseModel, condecimal
from datetime import date
from typing import List

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return "Welcome"

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




# Create
@app.post("/flat/", response_model=FlatResponse)
def create_flat(flat: FlatCreate, db: Session = Depends(get_db)):
    db_flat = Flat(**flat.dict())
    db.add(db_flat)
    db.commit()
    db.refresh(db_flat)
    return db_flat


@app.post("/payment/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


@app.post("/service/", response_model=ServiceResponse)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    db_service = Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service



# Read
@app.get("/flat/{flat_id}", response_model=FlatResponse)
def read_flat(flat_id: int, db: Session = Depends(get_db)):
    flat = db.query(Flat).filter(Flat.id == flat_id).first()
    if flat is None:
        raise HTTPException(status_code=404, detail='Flat not found')
    return flat

@app.get("/payment/{payment_id}", response_model=PaymentResponse)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail='Payment not found')
    return payment


@app.get("/service/{service_id}", response_model=ServiceResponse)
def read_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service is None:
        raise HTTPException(status_code=404, detail='Service not found')
    return service



# Update
@app.put("/flat/{flat_id}", response_model=FlatResponse)
def update_flat(flat_id: int, updated: FlatCreate, db: Session = Depends(get_db)):
    flat = db.query(Flat).filter(Flat.id == flat_id).first()
    if flat is None:
        raise HTTPException(status_code=404, detail='Flat type not found')

    for key, value in updated.dict().items():
        setattr(flat, key, value)

    db.commit()
    db.refresh(flat)
    return flat


@app.put("/payment/{payment_id}", response_model=PaymentResponse)
def update_payment(payment_id: int, updated: PaymentCreate, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail='Payment not found')

    for key, value in updated.dict().items():
        setattr(payment, key, value)

    db.commit()
    db.refresh(payment)
    return payment


@app.put("/service/{service_id}", response_model=ServiceResponse)
def update_service(service_id: int, updated: ServiceCreate, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service is None:
        raise HTTPException(status_code=404, detail='Service not found')

    for key, value in updated.dict().items():
        setattr(service, key, value)

    db.commit()
    db.refresh(service)
    return service


# Delete
@app.delete("/flat/{flat_id}", response_model=FlatDelete)
def delete_flat(flat_id: int, db: Session = Depends(get_db)):
    flat = db.query(Flat).filter(Flat.id == flat_id).first()
    if flat is None:
        raise HTTPException(status_code=404, detail="Flat not found")

    db.delete(flat)
    db.commit()
    return {"message": "Flat deleted"}

@app.delete("/payment/{payment_id}", response_model=PaymentDelete)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    db.delete(payment)
    db.commit()
    return {"message": "Payment deleted"}

@app.delete("/service/{service_id}", response_model=ServiceDelete)
def delete_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")

    db.delete(service)
    db.commit()
    return {"message": "Service deleted"}


@app.post("/json_field/", response_model=JsonResponse)
def create_json_data(json_data: JsonCreate, db: Session = Depends(get_db)):
    db_json_data = JsonField(**json_data.dict())
    db.add(db_json_data)
    db.commit()
    db.refresh(db_json_data)
    return db_json_data



# pagination for read
@app.get("/flats/", response_model=List[FlatResponse])
def read_flats(page: int = 0, per_page: int = 10, db: Session = Depends(get_db)):
    flat = db.query(Flat).offset(page).limit(per_page).all()
    if flat is None:
        raise HTTPException(status_code=404, detail='Flats not found')
    return flat


@app.get("/payments/", response_model=List[PaymentResponse])
def read_payments(page: int = 0, per_page: int = 10, db: Session = Depends(get_db)):
    payment = db.query(Payment).offset(page).limit(per_page).all()
    if payment is None:
        raise HTTPException(status_code=404, detail='Payments not found')
    return payment


@app.get("/services/", response_model=List[ServiceResponse])
def read_services(page: int = 0, per_page: int = 10, db: Session = Depends(get_db)):
    service = db.query(Service).offset(page).limit(per_page).all()
    if service is None:
        raise HTTPException(status_code=404, detail='Services not found')
    return service