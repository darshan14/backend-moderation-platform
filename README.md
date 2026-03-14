##Tech Stack:
- *Programming Language:* Python 3.13.12
- *Libraries:* FastAPI, sqlalchemy
- *Database:* PostgreSQL

##Database URL:
postgresql://postgres:postgres@localhost:5432/moderation_db

##Database Tables:
*tbmoderator*
---------
id
region

*tbevent*
---------
event_id
region
payload
is_claim

*tbassignment*
---------
id
event_id
moderator_id
dt_tm_claim
dt_tm_expire
is_acknowledge

##Endpoint
- Connection Test: http://127.0.0.1:8000
- Post Login User: http://127.0.0.1:8000/moderator/login/{moderator_id}
- Get Available Events: http://127.0.0.1:8000/moderator/events/{moderator_id}
- Post Claim Event: http://127.0.0.1:8000/moderator/claim
    Response Body: {
    "event_id": 3,
    "moderator_id": 1
    }

- Post Acknowledge Event: http://127.0.0.1:8000/moderator/acknowledge
    Response Body: {
    "event_id": 3,
    "moderator_id": 1
    }

- Post Expiry Event: http://127.0.0.1:8000/moderator/expire/{event_id}