from random import choices
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from dbAlch import DBalchemy


class SearchName(FlaskForm):
    name = StringField('Ticker:')
    # name = SelectField('Choice Ticher: ', choices=DBalchemy().show_all())
    submit = SubmitField('Search')
    