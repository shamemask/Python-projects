from enum import unique
from app import db

class Tickers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tickername = db.Column(db.String(10), index = True, unique = True)
    cost = db.Column(db.Integer, index = True)

    def __repr__(self):
        return '<{} = {}>'.format(self.trickername,self.cost)