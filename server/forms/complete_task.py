from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class CompleteTaskForm(FlaskForm):
    task_id = SelectField('Select Task That Is Complete: ', coerce=int)
    submit = SubmitField("Mark Task Complete")
