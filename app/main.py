from fastapi import FastAPI
from app.database.init_db import init_db
from app.routes import moderator_routes

app = FastAPI()

init_db()

app.include_router(moderator_routes.router)

@app.get("/")
def home():
    return {"message": "Moderation API running"}