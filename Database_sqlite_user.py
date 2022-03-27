import sqlite3
from user import User

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE users (
            first text,
            last text,
            email text
            adress text
            )""")


def insert_user(user):                #insert new user into database 
    with conn:  
        c.execute("INSERT INTO users VALUES (:first, :last, :email)", {'first': user.first, 'last': user.last, 'email': user.email, 'adress': user.adress})

def get_users_by_name(lastname):      #search user by their name 
    c.execute("SELECT * FROM users WHERE last=:last", {'last': lastname}) 
    return c.fetchall()

def update_email(user, email):        #update users email 
    with conn:
        c.execute("""UPDATE users SET email = :email
                    WHERE first = :first AND last = :last""",
                  {'first': user.first, 'last': user.last, 'email': email})

def update_adress(user, adress):        #update users adress 
    with conn:
        c.execute("""UPDATE users SET adress = :adress
                    WHERE first = :first AND last = :last""",
                  {'first': user.first, 'last': user.last, 'email': user.email, 'adress': adress})

def remove_user(user):                #delete user 
    with conn:
        c.execute("DELETE from users WHERE first = :first AND last = :last",
                  {'first': user.first, 'last': user.last})




user_1 = User('Mike', 'Ray', 'mikeray@gmail.com', 'Simplestreet 8') 
user_2 = User('Jane', 'Ray', 'janeray@gmail.com', 'Simplestreet 8') 
user_3 = User('John', 'Blake', 'john.blake@gmail.com', 'Sunstreet 12')

insert_user(user_1)
insert_user(user_2)
insert_user(user_3)


update_email(user_2, 'jane.ray@gmail.com')

update_adress(user_2, 'Highstreet 3')

remove_user(user_1)

users = get_users_by_name('Ray') + get_users_by_name('Blake')  

print(users)   ##Mike Ray was removed and Jane Ray email has been updated (code lines: 53-57)






conn.close()