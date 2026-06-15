from fastapi import FastAPI
from sqlalchemy.orm import Session

from backend.database.db import SessionLocal
from backend.database.models import CafeteriaMenu

app = FastAPI(
    title="Cafeteria MCP Server"
)

@app.get("/")
def root():
    return {
        "server": "Cafeteria MCP",
        "status": "running"
    }


@app.get("/menu")
def weekly_menu():

    db: Session = SessionLocal()

    menu = db.query(CafeteriaMenu).all()

    return [
        {
            "day": m.day,
            "meal": m.meal,
            "items": m.items
        }
        for m in menu
    ]


@app.get("/day/{day}")
def menu_by_day(day: str):

    db: Session = SessionLocal()

    items = db.query(CafeteriaMenu).filter(
        CafeteriaMenu.day.ilike(day)
    ).all()

    return [
        {
            "meal": m.meal,
            "items": m.items
        }
        for m in items
    ]