from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#creating a database URL for SQLAlechemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"      #here we are "connecting" to a SQLite database (opening a file with the SQLite database) - the file will be located in the file "sql_app.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()    #this returns a class 



