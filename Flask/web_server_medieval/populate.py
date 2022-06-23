# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
# импортируем классы Citizen и Base из файла database_setup.py
from database_setup import Base, Citizen
from rand_citizen import citizen
from random import choice, randint as ri
from app import engine
# Свяжим engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляр DBSession
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()
# CREATE CITIZEN
higher_citizens = []
middle_citizens = []
lower_citizens = []
citizens_names = citizen(500)
# higher estate
for i in range(ri(10,15)):
    higher_citizen = Citizen(name = choice(citizens_names),
    estate = "Priest",
    estate_level = 1,
    subjection = 0,
    salary = 50000
    )
    session.add(higher_citizen)
    session.commit()
    higher_citizen.subjection = higher_citizen.id
    session.commit()
    higher_citizens.append(higher_citizen)
# middle estate
for i in range(ri(40,80)):
    middle_citizen = Citizen(name = choice(citizens_names),
    estate = "nobleman",
    estate_level = 2,
    subjection = choice(higher_citizens).id,
    salary = 30000
    )
    middle_citizens.append(middle_citizen)
session.add_all(middle_citizens)
session.commit()
# lower estate
for i in range(500 - len(higher_citizens) - len(middle_citizens)):
    lower_citizen = Citizen(name = choice(citizens_names),
    estate =choice(["крестьянин", "рабочий", "ремесленник", "буржуа"]),
    estate_level = 3,
    subjection = choice(middle_citizens).id,
    salary = ri(1000,10000)
    )
    lower_citizens.append(lower_citizen)
session.add_all(lower_citizens)
session.commit()


f = session.query(Citizen).all()
print(f)
