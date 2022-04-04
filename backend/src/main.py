# give this in your terminal: uvicorn main:app --reload
# this is our server: 127.0.0.1:8000/docs
# from flask import Flask, render_template, url_for, request, session, redirect
from distutils import ccompiler
import imp
import fastapi 
from typing import List

from fastapi import FastAPI, Depends, Path, Query, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from typing import Optional, List, TypedDict
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)    #this creates a database table


app = FastAPI()

#creating a Dependency -- Our dependency will create a new SQLAlchemy SessionLocal that will be used in a single request, and then close it once the request is finished
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


class Shipment(BaseModel):
    name: str
    name_recipient: str
    destination: str
    weight: float

class UpdateShipment(BaseModel):
    name: Optional[str] = None 
    name_recipient: Optional[str] = None 
    destination: Optional[str] = None 
    weight: Optional[float] = None 

class UserModel(BaseModel):
    firstName: str
    lastName: str
    phone: str
    email : str
    password : str
    # add the register data here 

class LoginRequestModel(BaseModel):
    email : str
    password : str

class LoginResponseModel(BaseModel):
    successful : bool
    user: Optional[UserModel] = None

class RegisterRequestModel(UserModel):
    pass
    # register data here like phone


# GET, POST, PUT(update information), DELETE 
@app.get("/")
def home():
   return {"Data": "Testing"}
    #  return render_template ('index.html')

#@app.get("/about")
#def about():
#    return{"Data": "About"}


#shipments = {}  ## later we want to change "shipments={} against an actual database!!"

# users dictionary 
users = {
    "username@gmail.com":UserModel(
        email = "username@gmail.com",
        password = "password1",
        firstName = "Bob",
        lastName = "Franklin",
        phone = "888343" 
    )
} 


#from here line 104 to 137 we have the standard FastAPI path operations code:
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/shipments/", response_model=schemas.Shipment)
def create_shipment_for_user(
    user_id: int, shipment: schemas.ShipmentCreate, db: Session = Depends(get_db)
):
    return crud.create_user_shipment(db=db, shipment=shipment, user_id=user_id)


@app.get("/shipments/", response_model=List[schemas.Shipment])
def read_shipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shipments = crud.get_shipments(db, skip=skip, limit=limit)
    return shipments




'''
@app.get("/get-shipments")
def get_shipments() -> List[Shipment]:
    return shipments

@app.get("/get-shipment/{shipment_id}")     # "shipment_id can be change by any other name"
def get_shipment(shipment_id: int = Path(None, description="The ID of the shipment you'd like to view", gt=0)):     # gt: greater than, lt: less than -> this means that the ID must be > 0, otherwise it will not accepted  
    return shipments[shipment_id]


# query parameters:
@app.get("/get-by-name/{shipment_id}")    
def get_shipment(name: Optional[str] = None):
    for shipment_id in shipments:
        if shipments[shipment_id].name == name:
            return shipments[shipment_id]
    raise HTTPException(status_code=404, detail="Shipment name not found.")
# give: "127.0.0.1:8000/get-by-name/1?test=2&name=..."


# request bosy & POST method:
@app.post("/create-shipment/{shipment_id}")
def create_shipment(shipment_id: int, shipment: Shipment):
    if shipment_id in shipments:
        raise HTTPException(status_code=400, detail="Shipment ID already exists.")

    shipments[shipment_id] = shipment     #{"name": shipment.name, "name_recipient": shipment.name_recipient, "destination": shipment.destination, "weight": shipment.weight}
    return shipments[shipment_id]


# update, PUT method:
@app.put("/update-shipment/{shipment_id}")
def update_shipment(shipment_id: int, shipment: UpdateShipment):
    if shipment_id not in shipments:
        raise HTTPException(status_code=404, detail="Shipment ID does not exist.")

    if shipment.name != None:
        shipments[shipment_id].name = shipment.name 

    if shipment.name_recipient != None:
        shipments[shipment_id].name_recipient = shipment.name_recipient   

    if shipment.destination != None:
        shipments[shipment_id].destination = shipment.destination 

    
    if shipment.weight != None:
        shipments[shipment_id].weight = shipment.weight 

    return shipments[shipment_id]


# DELETE method 
@app.delete("/delete-shipment")
def delete_shipment(shipment_id: int = Query(..., description="The ID of the Shipment to delete")):
    if shipment_id not in shipments:
        raise HTTPException(status_code=404, detail="Shipment ID does not exist.")

    del shipments[shipment_id]
    return {"Success": "Shipment deleted!"}
'''

# Auth management
@app.post("/login")
def login(login_data : LoginRequestModel) -> LoginResponseModel:
    print(login_data)
    

    if login_data.email in users and login_data.password == users[login_data.email].password:
        response = LoginResponseModel(successful=True, user=users[login_data.email])
    else:
        response = LoginResponseModel(successful=False)
    
    return response
    


@app.post("/register")
def register(register_data : RegisterRequestModel) -> UserModel:
    print(register_data)
    
    if register_data.email in users:
        raise HTTPException(status_code=400, detail="User already exists.")
    response = UserModel(
        email=register_data.email,
        password=register_data.password,
        firstName=register_data.firstName,
        lastName=register_data.lastName,
        phone=register_data.phone
    )
    users[register_data.email] = response

    return response


