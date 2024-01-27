########################################################################################################
#                                           Library
########################################################################################################
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from .config import *
from sqlalchemy.orm import sessionmaker


########################################################################################################
#                                           Configuration
########################################################################################################
def db_connection():
    connection_url = URL.create(username=db_username, host=db_address, database=db_name, drivername=db_driver,
                                password=db_password, port=db_port)
    return create_engine(connection_url)

########################################################################################################
#                                                Function
########################################################################################################
DeclarativeBase = declarative_base()
def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)
# def Base():
#     return declarative_base(db_connection())


########################################################################################################
def loadSession():
    Session = sessionmaker(bind=db_connection())
    session = Session()
    return session

