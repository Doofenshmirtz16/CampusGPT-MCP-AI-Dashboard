import pandas as pd

from database.db import SessionLocal
from database.models import Book
from database.models import Event
from database.models import CafeteriaMenu

db = SessionLocal()

# BOOKS
books_df = pd.read_csv("../data/books.csv")

for _, row in books_df.iterrows():

    book = Book(
        title=row["title"],
        author=row["author"],
        available_copies=row["available_copies"],
        shelf=row["shelf"]
    )

    db.add(book)

# EVENTS
events_df = pd.read_csv("../data/events.csv")

for _, row in events_df.iterrows():

    event = Event(
        event_name=row["event_name"],
        event_date=row["event_date"],
        club=row["club"],
        location=row["location"],
        description=row["description"]
    )

    db.add(event)

# MENU
menu_df = pd.read_csv("../data/menu.csv")

for _, row in menu_df.iterrows():

    item = CafeteriaMenu(
        day=row["day"],
        meal=row["meal"],
        items=row["items"]
    )

    db.add(item)

db.commit()

print("Data Loaded Successfully")