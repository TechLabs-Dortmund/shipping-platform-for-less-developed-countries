#in this file we will have reusable functions to interact with the data in the database (CRUD = Create, Read, Update, Delete)

from sqlalchemy.orm import Session

from backend.src.fastapi_orm2.sql_app.main import Shipment

from . import models, schemas

#read a single user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#read a single user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#read multiple users 
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#create user
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#read multiple shipments
def get_shipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shipment).offset(skip).limit(limit).all()

#create shipment for user
def create_user_shipment(db: Session, shipment: schemas.ShipmentCreate, user_id: int):
    db_shipment = models.Shipment(**Shipment.dict(), owner_id=user_id)
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment


