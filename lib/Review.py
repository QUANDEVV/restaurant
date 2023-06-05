from sqlalchemy import create_engine, Column, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///reviews.db')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Base class for declarative models
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Float)

    customer = relationship('Customer')
    restaurant = relationship('Restaurant')

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def get_rating(self):
        return self.rating


Base.metadata.create_all(engine)