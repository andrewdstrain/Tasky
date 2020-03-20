from flask import render_template, flash, redirect, url_for
from server import app
from server.forms import LoginForm


@app.route('/')
def index():
    return redirect(url_for('main_menu'))

@app.route('/main_menu')
def main_menu():
    return redirect(url_for('list_tasks'))

@app.route('/list_tasks')
def list_tasks():
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
    return render_template('list_tasks.html', title='Home', tasks=tasks)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('main_menu'))
    return render_template('login.html', title='Sign In', form=form)


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')


@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
