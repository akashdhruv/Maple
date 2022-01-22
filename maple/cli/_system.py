"""
Command Line Interface (CLI) for system configuration management.
"""

import click
import os

from ..backend import Backend
from .  import maple

# Login to remote registry
#
@maple.command(name='login')
def login():
    """
    Login to container backend
    """
    Backend().system.login()

# Prune system
#
@maple.command('prune')
def prune():
    """
    Clear backend cache
    """
    Backend().system.prune()
