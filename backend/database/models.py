from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    author = Column(String)

    available_copies = Column(Integer)

    shelf = Column(String)


class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)

    event_name = Column(String)

    event_date = Column(String)

    club = Column(String)

    location = Column(String)

    description = Column(String)


class CafeteriaMenu(Base):

    __tablename__ = "cafeteria_menu"

    id = Column(Integer, primary_key=True)

    day = Column(String)

    meal = Column(String)

    items = Column(String)