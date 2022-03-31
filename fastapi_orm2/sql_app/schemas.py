from typing import List, Optional

from pydantic import BaseModel


class ShipmentBase(BaseModel):
    name: str
    name_recipient: str
    #weight: int
    destination: str
    

class ShipmentCreate(ShipmentBase):
    pass


class Shipment(ShipmentBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    #first name 
    #last name 
    #phone no
    


class User(UserBase):
    id: int
    is_active: bool
    shipments: List[Shipment] = []

    class Config:
        orm_mode = True

