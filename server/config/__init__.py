"""Config"""

from os import environ
from os.path import dirname, basename, isfile, join, abspath
import glob

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

basedir = abspath(dirname(__file__))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'your-key-goes-here'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:///' + join(basedir, 'tasky.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
