from server import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(140))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Task {}>'.format(self.task)
