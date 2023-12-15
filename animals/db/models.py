from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column

class Animal(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True, index=True)
    kind = Column(String)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    description = Column(String)
    color = Column(String)
    chipped = Column(Boolean, nullable=False)


class DbUser(Base): # Created structure for database
	__tablename__ = 'users' 
	id = Column(Integer, primary_key=True, index=True)
	e_mail = Column(String)
	first_name = Column(String)
	second_name = Column(String)
	username = Column(String)
	password = Column(String)
	accept_General_Condition = Column(Boolean)


