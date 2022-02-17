"""Initialize Maple"""
import os

os.environ["maple_dir"] = os.path.dirname(os.path.realpath(__file__))
os.environ["maple_home"] = os.environ["HOME"] + "/.local/maple"

from . import backend
from . import api
from . import cli
from . import resources
