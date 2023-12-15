from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from db.models import Animal
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from schemas import AnimalCreate

router = APIRouter(
        tags=["Animal List"]

    )

@router.put('/')
def update_animal(animal_id: int, animal: AnimalCreate, db: Session = Depends(get_db)):
    db_animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    update_data = animal.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_animal, field, value)
    
    db.commit()
    db.refresh(db_animal)
    return db_animal