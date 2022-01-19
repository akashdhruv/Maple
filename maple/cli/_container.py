"""Python CLI for maple"""

import click
import os

from .. import api
from .  import maple

# CLI group
#
@maple.group(name='container')
def container():
    """
    Container management, type maple container --help for more info
    """
    pass

# Commit changes to a container
# Saves changes to local container as an image, currently uses docker
#
@container.command(name='commit')
def commit():
    """
    Commit changes from local container to local image
    """
    api.Maple.backend[os.getenv('maple_backend')].container.commit()

# Enter the shell environment of a container
#
@container.command('shell')
def shell():
    """
    Get shell access to the local container
    """
    api.Maple.backend[os.getenv('maple_backend')].container.shell()

# Launch a notebook inside the container
#
@container.command('notebook')
@click.option('--port', default='8888', help='port for notebook server')
def notebook(port):
    """
    Launch ipython notebook inside the container
    """
    api.Maple.backend[os.getenv('maple_backend')].container.notebook(port)

# Execute a command in a container
@container.command('execute')
@click.argument('command',default='echo Hello World!')
def execute(command):
    """
    Execute command in a container
    """
    api.Maple.backend[os.getenv('maple_backend')].container.execute(command)

# Pour an image in a local container to access interactive shell
# If maple_source or maple_traget are present then they will be mounted inside the containter.
# This is useful for mounting maple_source for development
#
@container.command('pour')
def pour():
    """
    Pour local image in a container
    """
    api.Maple.backend[os.getenv('maple_backend')].container.pour()

# Rinse a local container
# Do this if the local container is not needed
#
@container.command('rinse')
@click.argument('container',default='None')
def rinse(container):
    """
    Stop local container
    """
    api.Maple.backend[os.getenv('maple_backend')].container.rinse(container)

# List all container
#
@container.command('list')
@click.argument('backend',default='None')
def list(backend):
    """
    List all containers on system
    """
    if backend != 'None': os.environ['maple_backend'] = str(backend)
    api.Maple.backend[os.getenv('maple_backend')].container.list()
