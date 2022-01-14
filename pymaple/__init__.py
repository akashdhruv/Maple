"""Initialize PyMaple"""
import os

from . import docker
from . import singularity
from .maple import Maple

os.environ['maple_dir'] = os.path.dirname(os.path.realpath(__file__)) + '/..'
