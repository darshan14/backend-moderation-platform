from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.database.models import Moderator, Event, Assignment
from app.schemas.moderator_schema import AcknowledgeEventRequest, ClaimEventRequest


def get_moderator(db: Session, moderator_id: int):
    return db.query(Moderator).filter(Moderator.id == moderator_id).first()


def get_events_for_region(db: Session, moderator_id: int):

    moderator = db.query(Moderator).filter(Moderator.id == moderator_id).first()

    return db.query(Event.event_id, Event.payload).filter(
        Event.region == moderator.region,
        Event.is_claim == False
    ).all()


def claim_event(db: Session, request: ClaimEventRequest):

    try:
        # Lock the event row
        event = (db.query(Event).filter(
                Event.event_id == request.event_id,
                Event.is_claim == False
            )
            .with_for_update()
            .first()
        )

        # If event is already claimed by another moderator, return errorv message
        if not event:
            return {"message": "Event already claimed by another moderator"}

        # Mark event as claimed
        event.is_claim = True

        assignment = Assignment(
            event_id=request.event_id,
            moderator_id=request.moderator_id,
            dt_tm_claim=datetime.now(),
            dt_tm_expire=datetime.now() + timedelta(minutes=15),
            is_acknowledge=False
        )

        db.add(assignment)
        db.commit()

        return {
                "message": "Event claimed",
                "event_id": request.event_id,
                "event_expires_at": assignment.dt_tm_expire.isoformat()
            }

    except Exception as e:
        db.rollback()
        raise e

def acknowledge_event(db: Session, request: AcknowledgeEventRequest):

    assignment = db.query(Assignment).filter(
        Assignment.event_id == request.event_id,
        Assignment.moderator_id == request.moderator_id
    ).first()

    assignment.is_acknowledge = True
    assignment.dt_tm_expire = datetime.now()  # Mark as expired immediately after acknowledgment

    db.commit()

    return {
            "message": "Event acknowledged",
            "event_id": request.event_id
            }

def expire_event(db: Session, event_id: int):

    event = db.query(Event).filter(Event.event_id == event_id).first()

    if event:

        # Mark the event as not claimed so it can be claimed by other moderators
        event.is_claim = False

        db.commit()

        return {
                "message": "Event expired",
                "event_id": event_id
            }
    else:
        return {
                "message": "No active Event found",
                "event_id": event_id
            }