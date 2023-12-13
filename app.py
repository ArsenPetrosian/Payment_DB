from init_db import Base, engine, SessionLocal
from fastapi import FastAPI



app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
