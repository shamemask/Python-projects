from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_bootstrap import Bootstrap
from turbo_flask import Turbo
import flask_excel as excel
from waitress import serve
from flask_cors import CORS

SECRET_KEY = os.urandom(32)

app = Flask(__name__)

app.config.from_object(Config)
app.config['CSRF_ENABLED'] = True
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = SECRET_KEY
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
excel.init_excel(app)


Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
turbo = Turbo(app)
CORS(app)


from app import routes, models
from dbAlch import DBalchemy

# if __name__ == "__main__":
#     app.run()