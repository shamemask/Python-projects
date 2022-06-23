from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class Form(FlaskForm):
    name = StringField("Name: ")
    age  = IntegerField("age: ")
    submit = SubmitField("submit")