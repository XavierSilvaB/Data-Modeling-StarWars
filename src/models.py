import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from eralchemy import render_er



Base = declarative_base()


#Table de usuarios
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    def verifyLogin(self):
        """verify login"""
    
    def addToFavorite(self):
        """Add to Favorite """

    def removeFavorite(self):
        """remove Favorite"""
#Table de favoritos
# relacionada con las tablas de : personajes , planeta y vehiculos
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    Vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

#Table de personajes
class Character(Base):
    __tablename__= 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    gender = Column(String(40), nullable=False)
    height = Column(Integer, nullable=False)
    species = Column(String(100), nullable=False)
    weapons = Column(String(100), nullable=False)
    affiliations = Column(String(100), nullable=False)


#Table de Vehiculos
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    crew = Column(String(80), nullable=False)
    passenger = Column(String(80), nullable=False)
    vehicle_class = Column(String(80), nullable=False)
    model = Column(String(80), nullable=False)

#Table de Planetas
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    climate = Column(String(80), nullable=False)
    gravity = Column(String (80), nullable=False) 
    diameter = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)  
    terrain = Column(String(80), nullable=False)
 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')