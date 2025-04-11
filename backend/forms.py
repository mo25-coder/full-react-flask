from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp

class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=50)])
    email_or_phone = StringField("Email or Phone", validators=[
        DataRequired(),
        Regexp(r"^\+?\d{10,15}$|^[\w\.-]+@[\w\.-]+\.\w+$", message="Enter a valid email or phone number")
    ])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
