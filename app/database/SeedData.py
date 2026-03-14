import json
from app.database.connection import SessionLocal
from app.database.models import Moderator, Event

db = SessionLocal()

# Prevent duplicate seeding
if db.query(Moderator).first():
    print("Seed data already exists. Skipping...")
    db.close()
    exit()

# -------------------------
# Insert Moderators
# -------------------------

moderators = [
    Moderator(id=1, region="asia"),
    Moderator(id=2, region="asia"),
    Moderator(id=3, region="europe"),
    Moderator(id=4, region="us")
]

# -------------------------
# Insert Warehouse Events
# -------------------------

events = [

    Event(
        event_id=1,
        region="asia",
        payload=json.dumps({
            "title": "Forklift Near Miss",
            "description": "Forklift operator nearly collided with a worker in the loading dock area."
        }),
        is_claim=False
    ),

    Event(
        event_id=2,
        region="asia",
        payload=json.dumps({
            "title": "Improper Pallet Stacking",
            "description": "Multiple pallets stacked beyond safe height limits creating a collapse risk."
        }),
        is_claim=False
    ),

    Event(
        event_id=3,
        region="asia",
        payload=json.dumps({
            "title": "Blocked Emergency Exit",
            "description": "Emergency exit door obstructed by stored inventory boxes."
        }),
        is_claim=False
    ),

    Event(
        event_id=4,
        region="europe",
        payload=json.dumps({
            "title": "Chemical Spill",
            "description": "Small chemical spill detected in hazardous material storage area."
        }),
        is_claim=False
    ),

    Event(
        event_id=5,
        region="europe",
        payload=json.dumps({
            "title": "Unsecured Cargo",
            "description": "Cargo inside transport truck not properly secured during loading operation."
        }),
        is_claim=False
    ),

    Event(
        event_id=6,
        region="europe",
        payload=json.dumps({
            "title": "Worker Without Safety Helmet",
            "description": "Worker observed operating in high-risk zone without required protective helmet."
        }),
        is_claim=False
    ),

    Event(
        event_id=7,
        region="us",
        payload=json.dumps({
            "title": "Overloaded Conveyor Belt",
            "description": "Automated conveyor belt exceeding recommended load capacity."
        }),
        is_claim=False
    ),

    Event(
        event_id=8,
        region="us",
        payload=json.dumps({
            "title": "Truck Dock Misalignment",
            "description": "Delivery truck incorrectly aligned with loading dock causing safety hazard."
        }),
        is_claim=False
    ),

    Event(
        event_id=9,
        region="us",
        payload=json.dumps({
            "title": "Oil Spill on Warehouse Floor",
            "description": "Hydraulic oil spill detected near forklift charging station."
        }),
        is_claim=False
    ),

    Event(
        event_id=10,
        region="us",
        payload=json.dumps({
            "title": "Damaged Storage Rack",
            "description": "Storage rack beam visibly bent after recent forklift impact."
        }),
        is_claim=False
    )
]

# -------------------------
# Insert Records
# -------------------------

db.add_all(moderators)
db.add_all(events)

db.commit()
db.close()

print("10 warehouse safety events inserted successfully!")