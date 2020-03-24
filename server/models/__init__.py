"""Models"""

from os.path import dirname, basename, isfile
from server import login
from server.models.user import User
import glob

modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


@login.user_loader
def load_user(id: str):
    return User.query.get(int(id))
