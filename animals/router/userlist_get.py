from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import DbUser
from schemas import UserBase
from typing import List
from db import db_user


router = APIRouter(
    prefix="/users",
    tags=["Users List"]
)


@router.get("/signed-in")
def get_signed_in_users_list(db: Session = Depends(get_db)):
    signed_in_users = db_user.get_signed_in_users(db)
    return signed_in_users


# @router.get("/signed-in", response_model=List[UserBase])
# def get_signed_in_users_list(db: Session = Depends(get_db)):
#     signed_in_users = db_user.get_signed_in_users(db)
#     return signed_in_users