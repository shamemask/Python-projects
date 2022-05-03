
from app import  db
from app.models import Tickers
from random import random
import time
import os

def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement

class DBalchemy:
    def __init__(self):
        self.titles = ['id', 'ticker name', 'cost']
        
    
    def life(self):
        time.sleep(1)
        os.system('cls')
        self.update_cost()

    def update_cost(self):
        col = 0
        for t in Tickers.query.all():
            t.cost += generate_movement()
            if t.cost < 0:
                t.cost = 0                
            db.session.add(t)
            if col % 5 > 0:
                print(' [',t.id,t.tickername,t.cost,'] ',end='')
            else:
                print(' [',t.id,t.tickername,t.cost,'] ')
            col += 1 
        db.session.commit()

    def add_all(self):
        for i in range(100):
            if i < 10:
                num_text = '0{}'.format(i)
            else:
                num_text = '{}'.format(i)
            ticker = Tickers(tickername = 'ticker_{}'.format(num_text),cost = 0)
            db.session.add(ticker)
        db.session.commit()
        self.get_all()

    def get_all(self):
        print('Ticker table')
        return [[t.id,t.tickername,t.cost] for t in Tickers.query.all()]
        # tickers = Tickers.query.all()
        
        # tickers_table=[]
        # for t in tickers:
        #     tickers_table.append([t.id,t.tickername,t.cost])
        
        # return tickers_table

    def get_tickers(self,names):
        print('Find tickers')
        return [[t.id,t.tickername,t.cost] for t in Tickers.query.filter(Tickers.tickername.in_(names)).all()]

    def get_one(self, name):
        print('Find ticker')
        return [[t.id,t.tickername,t.cost] for t in Tickers.query.filter(Tickers.tickername.like(f'%{name}%')).all()]
        
        # req = []
        # for t in tickers:
        #     if name in t.tickername:
        #         # print(t.id,t.tickername,t.cost)
        #         req.append([t.id,t.tickername,t.cost])
        
        # return req
    
    def del_all(self):
        tickers = Tickers.query.all()
        for t in tickers:
            print(t.id,t.tickername,'delete')
            db.session.delete(t)
        db.session.commit()
        print('All tickers removed')
        


if __name__ == '__main__':
    db1 = DBalchemy()
    # db1.get_all()
    print(db1.get_tickers(['ticker_12', 'ticker_13', 'ticker_14', 'ticker_15', 'ticker_16', 'ticker_17', 'ticker_18', 'ticker_19']))
    # db1.del_all()
    # db1.add_all()
    # while True:
    #     db1.life()