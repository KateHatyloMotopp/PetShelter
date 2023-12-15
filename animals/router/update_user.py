from fastapi import FastAPI, APIRouter, Query, status, HTTPException, Depends
from typing import List, Optional
from schemas import UserDisplayLogIn 
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from db.hash import Hash
from schemas import UserBase

router = APIRouter(  
	prefix="/login",
	tags=["Login"]
)

@router.put("/update/{id}")
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
	return db_user.update_user(db, id, request)

