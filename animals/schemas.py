from pydantic import BaseModel
from fastapi import Body


class AnimalCreate(BaseModel):
    kind: str
    name: str
    breed: str
    age: int
    description: str
    color: str
    chipped: bool


class UserBase(BaseModel):
    e_mail: str
    first_name: str
    second_name: str 
    username: str 
    password: str 
    accept_General_Condition: bool 

class UserDisplaySingUp(BaseModel): # Define the data which is obtained from data base and provided to user
    id: int
    e_mail: str
    first_name: str
    second_name: str
    username: str
    password: str
    accept_General_Condition: bool
# not all field are obligatory to display

    class Config():
        from_attributes = True # Allows the system to return database data in format provided in class UserDisplaySignIn


class UserDisplayLogIn(BaseModel): # Define the data which is obtained from data base and provided to user
    message: str

    class Config():
        from_attributes = True # Allows the system to return database data in format provided in class UserDisplayLogIn

