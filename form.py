from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Mine(FlaskForm):
    company_name = StringField('company name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    medicine_name = StringField('medicine name',
                       validators=[DataRequired(), Length(min=2, max=20)])
    Manufacturing_Date = StringField('Manufacturing Date',
                                   validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Sign Up')


