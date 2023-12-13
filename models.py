from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, Boolean
from sqlalchemy.orm import relationship
from init_db import Base, engine
from sqlalchemy.dialects.postgresql import JSONB



class Payment(Base):

    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    sum = Column(Numeric(precision=10, scale=2))
    date_of_payment = Column(Date)
    for_date = Column(String(50))

    # Many-to-One relation with Service
    service_id = Column(Integer, ForeignKey('service.id'))
    service = relationship('Service', back_populates='payments')

    # Many-to-One with Flat
    flat_id = Column(Integer, ForeignKey('flat.id'))
    flat = relationship('Flat', back_populates='payments')


class Flat(Base):

    __tablename__ = 'flat'

    id = Column(Integer, primary_key=True)
    owner = Column(String(50))
    street = Column(String(50))
    flat_num = Column(Integer)
    building_num = Column(Integer)

    # One-to-Many relation with Payment
    payments = relationship('Payment', back_populates='flat')


class Service(Base):

    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    price_per_month = Column(Numeric(precision=10, scale=2))
    name = Column(String(50))
    counter = Column(Boolean)

    # One-to-Many with Payment
    payments = relationship('Payment', back_populates='service')


class JsonField(Base):

    __tablename__ = 'json_data'

    id = Column(Integer, primary_key=True)
    json_field = Column(JSONB)




Base.metadata.create_all(engine)
