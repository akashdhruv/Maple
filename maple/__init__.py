"""Initialize PyMaple"""
import os

from . import backend
from . import cli
from .api import *

os.environ['maple_dir'] = os.path.dirname(os.path.realpath(__file__))
