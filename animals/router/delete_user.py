from fastapi import FastAPI, APIRouter, Query, status, HTTPException, Depends
from typing import List, Optional
from schemas import UserDisplayLogIn 
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from db.hash import Hash


router = APIRouter(  
	prefix="/login",
	tags=["Login"]
)


@router.delete("/delete/{id}")
def delete(id: int, db: Session = Depends(get_db)):
	return db_user.delete_user(db, id)