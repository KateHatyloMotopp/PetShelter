from fastapi import FastAPI, APIRouter, Query, Body, Response, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from schemas import UserBase, UserDisplaySingUp 
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from db.models import DbUser

router = APIRouter(
	prefix="/signup",
	tags=["Sign Up"]
)


@router.post("/", response_model=UserDisplaySingUp)
def sign_up(
    user_data: UserBase,
    db: Session = Depends(get_db)
):
    new_user = db_user.create_user(db=db, request=user_data)
    return new_user
