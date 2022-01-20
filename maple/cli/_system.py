"""Python CLI for maple"""

import click
import os

from .. import backend
from .  import maple

# Login to remote registry
#
@maple.command(name='login')
def login():
    """
    Login to container backend
    """
    backend.dict[os.getenv('maple_backend')].system.login()

# Prune system
#
@maple.command('prune')
def prune():
    """
    Clear backend cache
    """
    backend.dict[os.getenv('maple_backend')].system.prune()
