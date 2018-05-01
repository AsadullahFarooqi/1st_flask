from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
	first_name = StringField("First name", validators=[DataRequired(" please enter please enter ")])
	last_name = StringField("Last name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired(), Email("please enter the damn email")])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=8, message="o shit no shorter then 8")])
	submit = SubmitField("Sign up")