from fastapi import APIRouter, Depends
from db.database import get_db
from db.models import Animal
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from schemas import AnimalCreate
from db.db_animals import insert_animal

router = APIRouter(
        tags=["Animal List"]

    )


@router.post("/")
def create_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    created_animal = insert_animal(
        db=db,
        kind=animal.kind,
        name=animal.name,
        breed=animal.breed,
        age=animal.age,
        description=animal.description,
        color=animal.color,
        chipped=animal.chipped
    )
    return created_animal