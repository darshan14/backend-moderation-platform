from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services import moderator_service
from app.schemas.moderator_schema import AcknowledgeEventRequest, ClaimEventRequest

router = APIRouter(prefix="/moderator", tags=["Moderator"])

# 1 Login Moderator
@router.post("/login/{moderator_id}")
def login_moderator(moderator_id: int, db: Session = Depends(get_db)):
    return moderator_service.login_moderator(db, moderator_id)


# 2 Get Available Events
@router.get("/events/{moderator_id}")
def get_available_events(moderator_id: int, db: Session = Depends(get_db)):
    return moderator_service.get_available_events(db, moderator_id)


# 3 Claim Events
@router.post("/claim")
def claim_event(request: ClaimEventRequest, db: Session = Depends(get_db)):
    return moderator_service.claim_event(db, request)


# 4 Acknowledge Event
@router.post("/acknowledge")
def acknowledge_event(request: AcknowledgeEventRequest, db: Session = Depends(get_db)):
    return moderator_service.acknowledge_event(db, request)

@router.post("/expire/{event_id}")
def expire_event(event_id: int, db: Session = Depends(get_db)):
    return moderator_service.expire_event(db, event_id)