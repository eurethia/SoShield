from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    codes = StringField('Activation Code', validators=[DataRequired()])
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()], id = "password")
    show_password = BooleanField('Show password', id='check')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Confirm')

class Logout(FlaskForm):
    submit = SubmitField('Logout')
