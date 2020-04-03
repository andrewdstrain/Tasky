from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    """
    A Flask form for adding a task to the Flasky databaase
    """
    task_text = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')
