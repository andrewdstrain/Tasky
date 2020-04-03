from server import db


class TaskyTask(db.Model):
    """
    The model for the actual task. The user_id field is the foreign key
    for the user who created the task.
    """
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(140), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('tasky_user.id'))

    def __repr__(self) -> str:
        """
        Method to display sane text for the TaskyTask.
        :return: a string showing the print() and repr() text
        """
        return '<TaskyTask {}>'.format(self.task)
