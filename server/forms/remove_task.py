from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class RemoveTaskForm(FlaskForm):
    task_id = SelectField('Select Task To Be Removed: ', coerce=int)
    submit = SubmitField("Remove Task")
