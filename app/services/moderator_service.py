import json

from sqlalchemy.orm import Session
from app.repositories import moderator_repository
from app.schemas.moderator_schema import AcknowledgeEventRequest, ClaimEventRequest


def login_moderator(db: Session, moderator_id: int):
    return moderator_repository.get_moderator(db, moderator_id)


def get_available_events(db: Session, moderator_id: int):
    result = []
    events = moderator_repository.get_events_for_region(db, moderator_id)
    for event in events:
        payload_data = json.loads(event.payload)

        result.append({
            "event_id": event.event_id,
            "category": payload_data.get("category"),
            "title": payload_data.get("title"),
            "description": payload_data.get("description")
        })

    return result


def claim_event(db: Session, request: ClaimEventRequest):
    return moderator_repository.claim_event(db, request)


def acknowledge_event(db: Session,request: AcknowledgeEventRequest):
    return moderator_repository.acknowledge_event(db, request)

def expire_event(db: Session, event_id: int):
    return moderator_repository.expire_event(db, event_id)