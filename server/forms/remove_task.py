from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class RemoveTaskForm(FlaskForm):
    """
    A Flask form to remove a sing task from the Tasky database
    """
    task_id = SelectField('Select Task To Be Removed: ', coerce=int)
    submit = SubmitField("Remove Task")
