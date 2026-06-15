from fastapi import FastAPI
from sqlalchemy.orm import Session

from backend.database.db import SessionLocal
from backend.database.models import Event

app = FastAPI(
    title="Events MCP Server"
)

@app.get("/")
def root():
    return {
        "server": "Events MCP",
        "status": "running"
    }

@app.get("/upcoming")
def upcoming_events():

    db: Session = SessionLocal()

    events = db.query(Event).all()

    return [
        {
            "id": e.id,
            "event_name": e.event_name,
            "date": e.event_date,
            "club": e.club,
            "location": e.location
        }
        for e in events
    ]


@app.get("/search")
def search_event(query: str):

    db: Session = SessionLocal()

    events = db.query(Event).filter(
        Event.event_name.ilike(f"%{query}%")
    ).all()

    return [
        {
            "event_name": e.event_name,
            "date": e.event_date,
            "club": e.club
        }
        for e in events
    ]


@app.get("/club/{club_name}")
def club_events(club_name: str):

    db: Session = SessionLocal()

    events = db.query(Event).filter(
        Event.club.ilike(f"%{club_name}%")
    ).all()

    return [
        {
            "event_name": e.event_name,
            "date": e.event_date,
            "location": e.location
        }
        for e in events
    ]