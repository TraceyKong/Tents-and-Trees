from flask_wtf import FlaskForm
from wtforms import IntegerField, validators

class LevelForm(FlaskForm):
    level = IntegerField('Level', validators=[validators.NumberRange(min=5, max=24), validators.InputRequired()])