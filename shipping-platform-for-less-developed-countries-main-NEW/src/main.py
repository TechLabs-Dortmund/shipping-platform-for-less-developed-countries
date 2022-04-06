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

app.mount("/static", StaticFiles(directory="src/static"), name="static")



# GET, POST, PUT(update information), DELETE 
@app.get("/")
def home():
   return {"Data": "Testing"}

#@app.get("/about")
#def about():
#    return{"Data": "About"}


#shipments = {}  ## later we want to change "shipments={} against an actual database!!"

# users dictionary 
users = {
    "username@gmail.com":schemas.UserModel(
        email = "username@gmail.com",
        password = "password1",
        firstName = "Bob",
        lastName = "Franklin",
        phone = "888343", 
        country = "any",
        city = "any"
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




# Auth management
@app.post("/login")
def login(login_data : schemas.LoginRequestModel) -> schemas.LoginResponseModel:
    print(login_data)
    
    if login_data.email in users and login_data.password == users[login_data.email].password:
        response = schemas.LoginResponseModel(successful=True, user=users[login_data.email])
    else:
        response = schemas.LoginResponseModel(successful=False)
    
    return response
    


@app.post("/register")
def register(register_data : schemas.RegisterRequestModel) -> schemas.UserModel:
    print(register_data)
    
    if register_data.email in users:
        raise HTTPException(status_code=400, detail="User already exists.")
    response = schemas.UserModel(
        email=register_data.email,
        password=register_data.password,
        firstName=register_data.firstName,
        lastName=register_data.lastName,
        phone=register_data.phone,
        country=register_data.country, 
        city=register_data.city 

    )
    users[register_data.email] = response

    return response


