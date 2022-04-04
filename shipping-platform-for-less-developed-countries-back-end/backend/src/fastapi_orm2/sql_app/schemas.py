#creating the Pydantic models 

from typing import List, Optional

from pydantic import BaseModel


class ShipmentBase(BaseModel):
    name: str
    name_recipient: str
    weight: int
    destination: str
    

class ShipmentCreate(ShipmentBase):
    pass


#creating Pydantic model (schemas) that will be used when reading data, when returning it from the API
class Shipment(ShipmentBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True          #Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes)


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    #firstName: str 
    #lastName: str 
    #phone: str
    


class User(UserBase):
    id: int
    is_active: bool
    shipments: List[Shipment] = []

    class Config:
        orm_mode = True

