from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokeForm(FlaskForm):
    pokemon1input = StringField('Choose your Pokemon', validators=[DataRequired()])
    pokemon2input = StringField('Opponents Pokemon', validators=[DataRequired()])
    submit = SubmitField()

    

