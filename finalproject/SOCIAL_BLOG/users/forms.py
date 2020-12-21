from operator import sub
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from SOCIAL_BLOG.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Log In')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm',messages='Password must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit= SubmitField('Register!')
    
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exists')
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('user already exists')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(),])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg','png'])])
    submit= SubmitField('Update')
    
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exists')
        
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('user already exists')
    