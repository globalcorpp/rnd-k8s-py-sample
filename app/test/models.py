########################################################################################################
#                                           Library
########################################################################################################
from sqlalchemy import Column, Integer, String
from .database import DeclarativeBase

# Base_declarative = Base()


########################################################################################################
#                                           Functions
########################################################################################################
class Test(DeclarativeBase):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
