from pydantic import BaseModel


class ClaimEventRequest(BaseModel):
    event_id: int
    moderator_id: int

class AcknowledgeEventRequest(BaseModel):
    event_id: int
    moderator_id: int