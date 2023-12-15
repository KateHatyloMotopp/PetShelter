from fastapi import APIRouter, Depends
from db.database import get_db
from db.models import Animal
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Animal List"]
    )

@router.get('/')                   
def see_animals_list(db: Session = Depends(get_db)):
    return db.query(Animal).all()