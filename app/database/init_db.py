from app.database.connection import engine, Base, SessionLocal
from app.database.models import Moderator, Event
from app.database.SeedData import seed_data


def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Prevent duplicate seeding
    if not db.query(Moderator).first() and not db.query(Event).first():
        print("Seeding data into tables...")
        seed_data()
        
    db.close()
