from fastapi import FastAPI
from app.database.connection import engine, Base
import app.database.models 

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Moderation API running"}
