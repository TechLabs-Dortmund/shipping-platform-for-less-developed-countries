import sqlite3
from shipment import Shipment

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE shipments (
            name text,
            name_recipient text,
            destination text
            weight float
            )""")


def insert_shipments(shipments):                #insert new shipment into database 
    with conn:  
        c.execute("INSERT INTO shipments VALUES (:name, :name_recipient, :destination)", {'name': shipments.name, 'name_recipient': shipments.name_recipient, 'destination': shipments.destination, 'weight': shipments.weight})

def get_shipments_by_name(name):      #search shipment by their name 
    c.execute("SELECT * FROM shipments WHERE name=:name", {'name': name}) 
    return c.fetchall()

def update_destination(shipment, destination):        #update shipments destination 
    with conn:
        c.execute("""UPDATE shipments SET destination = :destination 
                    WHERE name = :name AND name_recipient = :name_recipient""",
                  {'name': shipment.name, 'name_recipient': shipment.name_recipient, 'destination': destination})

def update_weight(shipment, weight):        #update shipments weight 
    with conn:
        c.execute("""UPDATE shipments SET weight = :weight
                    WHERE name = :name AND name_recipient = :name_recipient""",
                  {'name': shipment.name, 'name_recipient': shipment.name_recipient, 'destination': shipment.destination, 'weight': weight})

def remove_shipment(shipment):                #delete shipment 
    with conn:
        c.execute("DELETE from shipments WHERE name = :name AND name_recipient = :name_recipient",
                  {'name': shipment.name, 'name_recipient': shipment.name_recipient})




shipment_1 = Shipment('John', 'Carlos', 'Mexico City', '12') 
shipment_2 = Shipment('Jane', 'Maria', 'Mexico City', '8') 
shipment_3 = Shipment('Tim', 'David', 'Mexico City', '14')

insert_shipments(shipment_1)
insert_shipments(shipment_2)
insert_shipments(shipment_3)


update_destination(shipment_2, 'Tijuana')

update_weight(shipment_2, '7')

remove_shipment(shipment_1)

shipments = get_shipments_by_name('John') + get_shipments_by_name('Jane')  

print(shipments)   ##John was removed and Jane destination and weight has been updated 






conn.close()