"""Python CLI for maple"""

import click
import os

from .. import api
from .  import maple

# CLI group
#
@maple.group(name='system')
def system():
    """
    Manage system configuration, type maple system --help for more info 
    """
    pass

# Login to remote registry
#
@system.command(name='login')
def login():
    """
    Login to container backend
    """
    api.Maple.backend[os.getenv('maple_backend')].system.login()

# Prune system
#
@system.command('prune')
@click.argument('backend',default='None')
def prune(backend):
    """
    Prune system
    """
    if backend != 'None': os.environ['maple_backend'] = str(backend)
    api.Maple.backend[os.getenv('maple_backend')].system.prune()
