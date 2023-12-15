from fastapi import FastAPI
from router import animal_get, animal_post, animal_put, animal_delete,signup_post, update_user,delete_user, userlist_get
from db import models 
from db.database import engine
from pydantic import BaseModel

app = FastAPI()

app.include_router(animal_get.router)
app.include_router(animal_post.router)
app.include_router(animal_put.router)
app.include_router(animal_delete.router)
app.include_router(signup_post.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)
app.include_router(userlist_get.router)


models.Base.metadata.create_all(engine)