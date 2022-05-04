
from flask import render_template, request, Response, stream_with_context
from app import app
from dbAlch import DBalchemy
from app.forms import SearchName
import json
import random
import time
from datetime import datetime

# import threading
d = DBalchemy()

currentTickers = []

    

@app.route('/', methods=['GET','POST'])
def index1():
    sform = SearchName(request.form)
    
    if request.method == 'POST':
        name = sform.name.data
        data = d.get_one(name)
        return render_template (
            'find.html',
            table_name=name,
            tlist=data,
            titles=d.titles,
            form=sform,
            title='Bitcoin Monthly Price in USD'
        )
    return render_template (
        'find.html',
        table_name='ALL Tickers',
        tlist=d.get_all(),
        titles=d.titles,
        form=sform,
            title='Bitcoin Monthly Price in USD'
    )



@app.route('/get', methods=['GET','POST'])
def getNames():
    global currentTickers
    tickers = request.args.get('tickers')
    # print(tickers)
    if tickers:
        array = tickers.split(",")
        for i in range(len(array)):
            array[i] = "ticker_" + array[i]
        currentTickers = array
        # print(array)
        return json.dumps(d.get_tickers(array))
    return





@app.route('/chart-data')
def chart_data():
    def generate_data():
        global currentTickers
        while True:
            
            # json_data = json.dumps(d.get_tickers(currentTickers))
            json_data = json.dumps(d.get_20_times_tickers(currentTickers))
            # print(currentTickers)
            # print(json_data)
            yield f"data:{json_data}\n\n"
            time.sleep(2)
        
    response = Response(stream_with_context(generate_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response