import os
from flask import Flask, abort, session, request, redirect
from flask.json import jsonify
from server.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates", static_folder="../public", static_url_path='')
app.config.from_object(Config)
db = SQLAlchemy(app)

from server.routes import *
from server.models import *
from server.services import *

initServices(app)

if 'FLASK_LIVE_RELOAD' in os.environ and os.environ['FLASK_LIVE_RELOAD'] == 'true':
	import livereload
	app.debug = True
	server = livereload.Server(app.wsgi_app)
	server.serve(port=os.environ['port'], host=os.environ['host'])
