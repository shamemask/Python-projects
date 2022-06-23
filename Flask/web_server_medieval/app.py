# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Citizen
import os
from config import SQLALCHEMY_DATABASE_URI as SDU
SECRET_KEY = os.urandom(32)
app = Flask(__name__, static_folder='static')
app.config['CSRF_ENABLED'] = True
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = SECRET_KEY
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
# Подключаемся и создаем сессию базы данных
engine = create_engine(SDU, connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Главная страница
@app.route('/')
def index():
    citizens = session.query(Citizen).all()
    # titles = session.query("PRAGMA table_info('citizens')").all()
    titles = [ "id",
        "name",
        "estate",
        "estate_level",
        "subjection",
        "salary"]
    for i in range(len(citizens)):
        citizen = str(citizens[i]).split('-')
        subjection = session.query(Citizen).filter_by(id=citizen[4]).first()
        citizen[4] = ','.join(str(subjection).split('-')[:3])
        citizens[i] = '-'.join(citizen)
        # print(citizens[i])
    
    
    return render_template (
        'main.html',
        table_name='ALL Citizen',
        tlist=citizens,
        titles=titles,
            title='ALL Citizen'
    )


if __name__ == '__main__':
   app.debug = True
   app.run(port=4996)
