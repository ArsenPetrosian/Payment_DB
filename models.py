from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, Boolean
from sqlalchemy.orm import relationship
from init_db import Base, engine


class Payment(Base):

    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    sum = Column(Numeric(precision=10, scale=2))
    date_of_payment = Column(Date)
    for_date = Column(String(50))

    

    # Many-to-One relation with Service
    service_id = Column(Integer, ForeignKey('service.id'))
    service = relationship('Service', back_populates='payment')

    # Many-to-One with Flat
    flat_id = Column(Integer, ForeignKey('flat.id'))
    flat = relationship('Flat', back_populates='payment')


class Flat(Base):

    __tablename__ = 'flat'

    id = Column(Integer, primary_key=True)
    owner = Column(String(50))
    street = Column(String(50))
    flat_num = Column(Integer)
    building_num = Column(Integer)

    # One-to-Many relation with Payment
    payment = relationship('Payment', back_populates='flat')
    


class Service(Base):

    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    counter = Column(Boolean)

    # One-to-Many with Payment
    service = relationship('Payment', back_populates='service')


Base.metadata.create_all(engine)