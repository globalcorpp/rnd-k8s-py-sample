########################################################################################################
#                                           Library
########################################################################################################
from fastapi import APIRouter, HTTPException, Depends, Request, Query
from .crud import db_get_message
from .schemas import TestInfoSchema
from .database import loadSession, db_connection, create_deals_table
from .config import api_path_prefix


########################################################################################################
#                                               Main
########################################################################################################
router = APIRouter(prefix="/{}/test".format(api_path_prefix),
                   tags=["Test"],
                   responses={404: {"description": "This URL is not corrected"}}, )

# Base().metadata.create_all(bind=db_connection())
create_deals_table(db_connection())

########################################################################################################
########################################################################################################
@router.get("/", response_model=list[TestInfoSchema])
async def show_message():
    session = loadSession()
    result = db_get_message(session)
    return result
