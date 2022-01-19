"""Python CLI for maple"""

import click
import os

from .. import backend
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
@click.option('--image', required=True)
def commit(image):
    """
    Commit changes from local container to local image
    """
    backend.dict[os.getenv('maple_backend')].container.commit(image)

# Enter the shell environment of a container
#
@container.command('shell')
def shell():
    """
    Get shell access to the local container
    """
    backend.dict[os.getenv('maple_backend')].container.shell()

# Launch a notebook inside the container
#
@container.command('notebook')
@click.option('--image', required=True)
@click.option('--port', default='8888', help='port for notebook server')
def notebook(image,port):
    """
    Launch ipython notebook inside the container
    """
    backend.dict[os.getenv('maple_backend')].container.notebook(image,port)

# Execute a command in a container
@container.command('execute')
@click.argument('command',default='echo Hello World!')
def execute(command):
    """
    Execute command in a container
    """
    result = backend.dict[os.getenv('maple_backend')].container.execute(command)
    if result != 0: raise Exception("[maple] Error inside container")

# Run a command inside a container and commit changes
@container.command('run')
@click.option('--image', required=True)
@click.option('--commit', is_flag=True, help='flag to commit changes to the image')
@click.argument('command')
def run(image,command,commit):
    """
    Run a command inside container and commit changes
    """
    backend.dict[os.getenv('maple_backend')].container.run(image,command,commit)

# Pour an image in a local container to access interactive shell
# If maple_source or maple_traget are present then they will be mounted inside the containter.
# This is useful for mounting maple_source for development
#
@container.command('pour')
@click.option('--image', required=True)
def pour(image):
    """
    Pour local image in a container
    """
    backend.dict[os.getenv('maple_backend')].container.pour(image)

# Rinse a local container
# Do this if the local container is not needed
#
@container.command('rinse')
@click.argument('containers', nargs=-1)
def rinse(containers):
    """
    Stop local container
    """
    if not containers: containers = ['None']
  
    for ctr in containers:
        backend.dict[os.getenv('maple_backend')].container.rinse(ctr)

# List all container
#
@container.command('list')
def list():
    """
    List all containers on system
    """
    backend.dict[os.getenv('maple_backend')].container.list()
