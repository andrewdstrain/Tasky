from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    task_text = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')
