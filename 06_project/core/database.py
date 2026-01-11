from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker , declarative_base

db_url = "sqlite:///./inventory.db"

import os
print("DB FILE PATH =", os.path.abspath("inventory.db"))

engine = create_engine(
    db_url ,
    connect_args={"check_same_thread" : False}
)
SessionLocal = sessionmaker(
    autoflush = False ,
    autocommit = False,
    bind = engine
)
Base = declarative_base()

#
# def get_db() :
#     db =  SessionLocal()
#     try :
#         yield db
#     finally:
#         db.close()

