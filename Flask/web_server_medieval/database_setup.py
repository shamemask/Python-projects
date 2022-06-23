# -*- coding: utf-8 -*-
# для настройки баз данных
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()


class Citizen(Base):
   __tablename__ = "citizens"
   id = Column(Integer, primary_key=True)
   name = Column(String(250), nullable=False)
   estate = Column(String(250), nullable=False)
   estate_level = Column(Integer)
   subjection = Column(Integer)
   salary = Column(Integer, nullable=False)
   def __repr__(self):
       return f'{self.id}-{self.name}-{self.estate}-{self.estate_level}-{self.subjection}-{self.salary}'

