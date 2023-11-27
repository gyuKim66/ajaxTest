from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField
from wtforms.validators import DataRequired

class IdeaForm(FlaskForm):
	idea = TextAreaField('idea', validators=[DataRequired()])