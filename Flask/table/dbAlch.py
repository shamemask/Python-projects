
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
        self.titles = [ 'ticker name', 'cost','dateCreated']
        
    
    def life(self):
        time.sleep(1)
        os.system('cls')
        self.update_cost()

    def max_cost(self):
        tickers = self.currentTickers()

    def add_next_tickers(self,tickers):
        col = 0
        for t in tickers:
            cost = t.cost + generate_movement()
            if cost < 0:
                cost = 0       
            ticker = Tickers(tickername = t.tickername,cost = cost)         
            db.session.add(ticker)
            # col += 1 
            # if col % 3 > 0:
            #     print(' [',t.tickername,t.cost,t.dateCreated.isoformat(' '),'] ',end='')
            # else:
            #     print(' [',t.tickername,t.cost,t.dateCreated.isoformat(' '),'] ')
            
        db.session.commit()

    def last_20_sec(self):
        last = Tickers.query.order_by(Tickers.dateCreated.desc()).limit(20).all()
        sec20 = [l.dateCreated.isoformat(' ') for l in last]
        # print(sec20)
        return sec20

    def currentSec(self):
        last = Tickers.query.order_by(Tickers.dateCreated.desc()).first()
        return last.dateCreated

    def currentTickers(self):
        tickers = []
        for i in range(100):
            if i < 10:
                num_text = '0{}'.format(i)
            else:
                num_text = '{}'.format(i)
            tickers.append(Tickers.query.filter(Tickers.tickername.like(f'%{num_text}%')).order_by(Tickers.dateCreated.desc()).first())
        return tickers

    def update_cost(self):
        # print(tickers)
        tickers = self.currentTickers()
        self.add_next_tickers(tickers)

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

    def get_everyone(self):
        return [[t.tickername,t.cost,t.dateCreated.isoformat(' ')] for t in Tickers.query.order_by(Tickers.id.desc()).all()]

    def get_20_times_tickers(self,names):
        # last = self.last_20_sec()
        tickers = self.get_everyone()
        # print(tickers)
        return [t for t in tickers if t[0] in names]
    
    def get_all(self):
        # print('Ticker table')
        tickers = self.currentTickers()
        return [[t.tickername,t.cost,t.dateCreated.isoformat(' ')] for t in tickers]
        

    def get_tickers(self,names):
        # print('Find tickers')
        tickers = self.currentTickers()
        result = [[t.tickername,t.cost,t.dateCreated.isoformat(' ')] for t in tickers if t.tickername in names]
        # print(result)
        return result

    def get_one(self, name):
        # print('Find ticker')
        tickers = self.currentTickers()
        return [[t.tickername,t.cost,t.dateCreated.isoformat(' ')] for t in tickers if name in t.tickername ]
       
    
    def del_all(self):
        tickers = Tickers.query.all()
        for t in tickers:
            # print(t.id,t.tickername,'delete')
            db.session.delete(t)
        db.session.commit()
        print('All tickers removed')
        


if __name__ == '__main__':
    db1 = DBalchemy()
    # print(db1.get_20_times_tickers())
    
    db1.del_all()
    db1.add_all()
    while True:
        db1.life()
        # print(db1.get_everyone())
        # print(db1.get_20_times_tickers(['ticker_12', 'ticker_13', 'ticker_14', 'ticker_15', 'ticker_16', 'ticker_17', 'ticker_18', 'ticker_19']))