# from urllib import request
import time
import requests
from bs4 import BeautifulSoup
from flask import render_template, request
from app import app, turbo, excel
from dbAlch import DBalchemy
from app.forms import SearchName
import threading
d = DBalchemy()

# @app.route('/')
# @app.route('/index')
# def index():
    
#     user = {'username': 'miguel'}
#     posts = [
#         {
#             'author': {'username':'John'},
#             'body': 'Beauteful day in Portland'
#         },
#         {
#             'author': {'username':'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         },
#         {
#             'author': {'username':'Ипполит'},
#             'body': 'Какая гадость эта ваша заливная рыба!!'
#         }
#     ]
#     return render_template("index.html",
#                     title = 'Home',
#                     user = user,
#                     posts = posts)
    

@app.route('/', methods=['GET','POST'])
def index():
    sform = SearchName(request.form)
    
    if request.method == 'POST':
        name = sform.name.data
        data = d.get_one(name)
        return render_template (
            'find.html',
            table_name=name,
            tlist=data,
            titles=d.titles,
            form=sform
        )
    return render_template (
        'find.html',
        table_name='ALL Tickers',
        tlist=d.get_all(),
        titles=d.titles,
        form=sform
    )

# @app.route('/selected_room/<int:room_id>')
# def selected_room(room_id):
#     room = Room.query.filter_by(id=room_id).first_or_404()

#     return room

@app.route('/get', methods=['GET','POST'])
def getNames():
    tickers = request.args.get('tickers')
    print(tickers)
    if tickers:
        tickers = tickers.split(",")
        for ticker in tickers:
            tickers[tickers.index[ticker]] = "ticker_" + ticker
        return str(d.get_tickers(tickers))

# @app.context_processor
# def inject_load():
#     d.life()

# @app.before_first_request
# def before_first_request():
#     threading.Thread(target=update_load).start()

# def update_load():
#     with app.app_context():
#         while True:
#             time.sleep(5)
#             turbo.push(turbo.replace(render_template('find.html'), '#dtAccess'))

