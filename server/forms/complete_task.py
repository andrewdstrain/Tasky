from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class CompleteTaskForm(FlaskForm):
    """
    A Flask form for completing a task
    """
    task_id = SelectField('Select Task That Is Complete: ', coerce=int)
    submit = SubmitField("Mark Task Complete")
