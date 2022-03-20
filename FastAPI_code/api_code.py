# give this in your terminal: uvicorn api_code:app --reload
# this is our server: 127.0.0.1:8000/docs

import imp
import fastapi 
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

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

# GET, POST, PUT(update information), DELETE 

#@app.get("/")
#def home():
#    return {"Data": "Testing"}

#@app.get("/about")
#def about():
#    return{"Data": "About"}


shipments = {}                ## later we want to change "shipments={} against an actual database!!"       

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


#if you reloud the server all the information will be automatically deleted and refreshed!