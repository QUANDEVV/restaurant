from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import Review

engine = create_engine('sqlite:///customers.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurants_visited = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return session.query(cls).all()

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        session.add(review)
        session.commit()

    def get_visited_restaurants(self):
        return list(set([review.restaurant for review in self.reviews]))

Base.metadata.create_all(engine)
