from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base   ##


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    #first name 
    #last name 
    #phone no 

    is_active = Column(Boolean, default=True)

    shipments = relationship("Shipment", back_populates="owner")


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    name_recipient = Column(String, index=True)
    destination = Column(String, index=True)
    #weight = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="shipments")

