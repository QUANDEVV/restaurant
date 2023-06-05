from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from Review import Review

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Base class for declarative models
class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return self.customers

    def average_star_rating(self):
        ratings = [review.get_rating() for review in self.reviews]
        return sum(ratings) / len(ratings) if ratings else 0


with engine.connect() as connection:
    Base.metadata.create_all(connection)  # This allows the database to be created at the root folder
