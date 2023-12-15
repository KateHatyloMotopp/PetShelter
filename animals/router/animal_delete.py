from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from db.models import Animal
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Animal List"]
    )

@router.delete('/')
def delete_animal(animal_id: int, db: Session = Depends(get_db)): 
    animal = db.query(Animal).get(animal_id)
    if animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    db.delete(animal)
    db.commit()
    return {"message": "Animal deleted successfully"}