"""Config"""

from os import environ
from os.path import dirname, basename, isfile
import glob

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY', 'abc012def345ghi678jkl9AB')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///../tasky.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
