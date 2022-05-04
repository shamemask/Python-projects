from enum import unique
from app import db
from sqlalchemy.sql import func
# import logging

# logging.basicConfig(filename="log\db.models.log",
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG)
# logging.info("Running Urban Planning")

# logger = logging.getLogger('urbanGUI')


class Tickers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tickername = db.Column(db.String(10), index = True)
    cost = db.Column(db.Integer, index = True)
    dateCreated = db.Column(db.DateTime(timezone=True), server_default=func.now()) 
    def __repr__(self):
        # logger.info('<{} = {}>'.format(self.trickername,self.cost))
        return '<{} , {} , {}>'.format(self.tickername,self.cost,self.dateCreated)