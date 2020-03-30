from server import db


class TaskyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(140), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('tasky_user.id'))

    def __repr__(self):
        return '<TaskyTask {}>'.format(self.task)
