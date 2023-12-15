from sqlalchemy.orm import Session
from db.models import Animal

def insert_animal(db: Session, kind:str, name: str, breed: str, age: int, description: str, color: str, chipped: bool):
    new_animal = Animal(
        kind=kind,
        name=name,
        breed=breed,
        age=age,
        description=description,
        color=color,
        chipped=chipped
    )

    db.add(new_animal)
    db.commit()
    db.refresh(new_animal)
    return new_animal