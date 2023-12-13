import requests
import random
from faker import Faker
from init_db import Base, engine
from sqlalchemy.orm import sessionmaker


BASE_URL = 'http://127.0.0.1:8000'
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()




def populate_payment():
    random_date = fake.date_between(start_date='-30y', end_date='today').strftime("%Y-%m-%d")
    url = f"{BASE_URL}/payment/"
    data = {
        'sum': round(fake.pyfloat(min_value=0, max_value=1e8), 2),
        'date_of_payment': random_date,
        'for_date': str(fake.date())
    }
    response = requests.post(url, json=data)
    return response.json()


def populate_flat():
    url = f"{BASE_URL}/flat/"
    data = {
        'owner': fake.name(),
        'street': fake.street_name(),
        'flat_num': abs(fake.pyint()),
        'building_num': abs(fake.pyint())
    }
    response = requests.post(url, json=data)
    return response.json()


def populate_service():
    url = f"{BASE_URL}/service/"
    data = {
        'price_per_month': round(fake.pyfloat(min_value=0, max_value=1e8), 2),
        'name': fake.name(),
        'counter': random.choice([True, False])
    }
    response = requests.post(url, json=data)
    return response.json()


def populate_json_data():
    url = f"{BASE_URL}/json_field/"
    data = {
        "json_field": {
            "address": fake.address().replace('\n', ', '),
            "street": fake.street_name(),
            "city": fake.city(),
        }
    }
    response = requests.post(url, json=data)
    return response.json()


for _ in range(100):
    populate_flat()

for _ in range(100):
    populate_payment()

for _ in range(100):
    populate_service()

for _ in range(100):
    populate_json_data()

session.commit()

print("Data Base population completed")  # Message to know that populating DB completed successfully


