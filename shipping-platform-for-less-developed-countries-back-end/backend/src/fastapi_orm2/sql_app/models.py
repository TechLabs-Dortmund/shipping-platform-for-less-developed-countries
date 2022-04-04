#creating SQLAlchemy models from the "Base" class

from http.client import TOO_MANY_REQUESTS
from operator import truediv
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base   


class User(Base):                            #SQLAlchemy model
    __tablename__ = "users"                  #this attribute  tells SQLAlchemy the name of the table to use in the database for each of these models

    id = Column(Integer, primary_key=True, index=True)
    
    firstName = Column(String, index=True) 
    lastName = Column(String, index=True) 
    phone = Column(String, index=True) 
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    shipments = relationship("Shipment", back_populates="owner")         #creating the relationship: that will contain the values from other tables related to this one 


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    name_recipient = Column(String, index=True)
    destination = Column(String, index=True)
    weight = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="shipments")
