from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from server import app
from server.forms import LoginForm
from server.models.taskyuser import TaskyUser


@app.route('/')
def index():
    return redirect(url_for('main_menu'))


@app.route('/main_menu')
def main_menu():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('main_menu.html', authenticated=True)


@app.route('/add_task')
def add_task():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('add_task.html', title='Add Task', authenticated=True)


@app.route('/remove_task')
def remove_task():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('remove_task.html', title='Remove Task', authenticated=True)


@app.route('/complete_task')
def complete_task():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('complete_task.html', title='Complete Task', authenticated=True)


@app.route('/list_tasks')
def list_tasks():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    tasks = [
        {
            'name': 'Do the dishes',
            'complete': True
        },
        {
            'name': 'Wash car',
            'complete': False
        }
    ]
    return render_template('list_tasks.html', title='List Tasks', tasks=tasks, authenticated=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_menu'))
    form = LoginForm()
    if form.validate_on_submit():
        user = TaskyUser.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main_menu'))
    return render_template('login.html', title='Log In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_menu'))


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')


@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
