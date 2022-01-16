"""Initialize Maple"""
import os

os.environ['maple_dir'] = os.path.dirname(os.path.realpath(__file__))

from . import backend
from . import api
from . import cli
