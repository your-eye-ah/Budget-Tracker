from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
from datetime import date

class EntryForm(FlaskForm):
    type = SelectField('Type', choices=[('Expense', 'Expense'), ('Income', 'Income')], validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    category = StringField('Category', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[Length(max=200)])
    date = DateField('Date', default=date.today, validators=[DataRequired()])
    submit = SubmitField('Add Entry')
