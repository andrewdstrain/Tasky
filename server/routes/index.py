from server import app
from flask import render_template


@app.route('/')
@app.route('/mainmenu')
def index():
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
    return render_template('index.html', title='Home', tasks=tasks)


@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')


@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
