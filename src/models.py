import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    favorite_planet = Column(String)
    favorite_character = Column(String)

class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    favorite_planet = Column(String, ForeignKey('user.id'))
    number_of_moons = Column(Integer)
    galaxy = Column(String(50))
    user = relationship(User)

class Favorite_Character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    favorite_character = Column(String, ForeignKey('user.id'))
    galaxy = Column(String(50))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')