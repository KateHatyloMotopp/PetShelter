from sqlalchemy import select
from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser


def create_user(db: Session, request: UserBase):
  new_user = DbUser(
    e_mail = request.e_mail,
    first_name = request.first_name,
    second_name = request.second_name,
    username = request.username,
    password = Hash.bcrypt(request.password),
    accept_General_Condition = request.accept_General_Condition
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def get_user_by_username(db: Session, username: str):
    return db.query(DbUser).filter(DbUser.username == username).first()

def get_user_by_email(db: Session, e_mail: str):
    return db.query(DbUser).filter(DbUser.e_mail == e_mail).first()

def get_info_by_username(db: Session, username: str):
    return db.query(DbUser).filter(DbUser.username == username).first()

def update_user(db: Session, id: int, request: UserBase): # Need to update all fields
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.e_mail: request.e_mail,
        DbUser.first_name: request.first_name,
        DbUser.second_name: request.second_name,
        DbUser.username: request.username,
        DbUser.password: Hash.bcrypt(request.password),
        DbUser.accept_General_Condition: request.accept_General_Condition
    })
    db.commit()
    return f"Updated!"

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return "User is deleted successfully!"


def get_signed_in_users(db: Session):
    return db.query(DbUser).filter(DbUser.accept_General_Condition == True).all()

