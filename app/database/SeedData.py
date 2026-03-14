import json
from app.database.connection import SessionLocal
from app.database.models import Moderator, Event

def seed_data():
    db = SessionLocal()

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
    # Event Categories
    # -------------------------

    categories = [
        "equipment_safety",
        "storage_safety",
        "worker_safety",
        "management_safety",
        "transport_safety"
    ]

    titles = {
        "equipment_safety": [
            "Forklift Brake Failure",
            "Conveyor Belt Overload",
            "Damaged Pallet Jack",
            "Crane Sensor Malfunction"
        ],
        "storage_safety": [
            "Unstable Pallet Stack",
            "Blocked Emergency Exit",
            "Overloaded Storage Rack",
            "Improper Hazard Storage"
        ],
        "worker_safety": [
            "Worker Without Helmet",
            "Unsafe Ladder Usage",
            "Worker in Restricted Zone",
            "Lack of Safety Vest"
        ],
        "management_safety": [
            "Missing Safety Inspection",
            "Expired Safety Certification",
            "Incomplete Incident Report",
            "Ignored Safety Protocol"
        ],
        "transport_safety": [
            "Unsecured Cargo",
            "Truck Dock Misalignment",
            "Driver Fatigue Alert",
            "Improper Trailer Lock"
        ]
    }

    descriptions = {
        "equipment_safety": [
            "Forklift brake system reported malfunction during warehouse operation.",
            "Automated conveyor belt exceeded recommended load capacity.",
            "Pallet jack wheel damaged while transporting goods.",
            "Warehouse crane safety sensor not responding properly."
        ],
        "storage_safety": [
            "Pallets stacked above recommended height limit.",
            "Emergency exit obstructed by stored inventory boxes.",
            "Heavy inventory stored beyond rack capacity.",
            "Hazardous materials placed outside designated storage."
        ],
        "worker_safety": [
            "Worker observed without helmet in active loading zone.",
            "Employee using ladder without proper stabilization.",
            "Worker entered forklift movement zone without authorization.",
            "Safety vest missing in high traffic warehouse area."
        ],
        "management_safety": [
            "Scheduled safety inspection not recorded in system.",
            "Safety training certification expired for warehouse staff.",
            "Incident report missing key safety details.",
            "Warehouse safety checklist not completed by supervisor."
        ],
        "transport_safety": [
            "Cargo inside truck not secured before transport.",
            "Delivery truck improperly aligned with dock station.",
            "Driver fatigue warning triggered during long haul.",
            "Trailer lock not properly engaged before departure."
        ]
    }

    # -------------------------
    # Insert Warehouse Events
    # -------------------------

    events = []
    event_id = 1

    regions = ["asia", "europe", "us"]

    for category in categories:
        for i in range(4):

            payload = {
                "category": category,
                "title": titles[category][i],
                "description": descriptions[category][i]
            }

            event = Event(
                event_id=event_id,
                region=regions[event_id % 3],
                payload=json.dumps(payload),
                is_claim=False
            )

            events.append(event)
            event_id += 1


    # -------------------------
    # Insert Records
    # -------------------------

    db.add_all(moderators)
    db.add_all(events)

    db.commit()
    db.close()

    print("20 warehouse safety events inserted successfully!")


