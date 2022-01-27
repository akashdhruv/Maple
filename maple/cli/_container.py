"""
Command Line Interface (CLI) for container management.
"""

import click
import toml
import os

from ..backend import Backend
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
@click.option('--image', default='None', help='image to commit changes')
def commit(image):
    """
    Commit changes from a poured container to an image
    """
    if image != 'None': os.environ['maple_image'] = str(image)
    Backend().container.commit()

# Enter the shell environment of a container
#
@container.command('shell')
def shell():
    """
    Get shell access inside a poured container
    """
    Backend().container.shell()

# Launch a notebook inside the container
#
@container.command('notebook')
@click.option('--image', default='None', help='image to launch notebook')
@click.option('--port', default='8888', help='port for notebook server')
def notebook(image,port):
    """
    Launch ipython notebook inside a container using an image
    """
    if image != 'None': os.environ['maple_image'] = str(image)
    Backend().container.notebook(port)

# Publish a container to an image
#
@container.command('publish')
@click.option('--image', default='None', help='image to pour and publish')
def publish(image):
    """
    Publish a container to an image using default execute statements
    """
    if image != 'None': os.environ['maple_image'] = str(image)

    Backend().container.pour()

    cmd_list = ['None']

    Maplefile = os.path.exists('Maplefile')
    if Maplefile and 'execute' in toml.load('Maplefile'): cmd_list = toml.load('Maplefile')['execute']

    result = Backend().container.execute(cmd_list)

    Backend().container.commit()
    Backend().container.rinse()

    if result != 0: raise Exception("[maple] Error inside container")

# Run a command inside a container and commit changes
@container.command('run')
@click.option('--image', default='None', help='image to run')
@click.option('--options', default='', help='run options')
@click.argument('command', default='None')
def run(image,options,command):
    """
    Pour a container to a run a command and then rinse it
    """
    if image != 'None': os.environ['maple_image'] = str(image)

    Maplefile = os.path.exists('Maplefile')
    if Maplefile and command == 'None':
        if 'run' in toml.load('Maplefile'): command = toml.load('Maplefile')['run']

    Backend().container.run(command,options)

# Execute a command in a container
@container.command('execute')
@click.argument('command', default='None')
def execute(command):
    """
    Execute command in a poured container
    """
    cmd_list = [command]

    Maplefile = os.path.exists('Maplefile')
    if Maplefile and command == 'None':
        if 'execute' in toml.load('Maplefile'): cmd_list = toml.load('Maplefile')['execute']

    result = Backend().container.execute(cmd_list)
    if result != 0: raise Exception("[maple] Error inside container")

# Pour an image in a local container to access interactive shell
# If maple_source or maple_traget are present then they will be mounted inside the containter.
# This is useful for mounting maple_source for development
#
@container.command('pour')
@click.option('--image', default='None', help='image to pour inside container')
def pour(image):
    """
    Pour an image into a container
    """
    if image != 'None': os.environ['maple_image'] = str(image)
    Backend().container.pour()

# Rinse a local container
# Do this if the local container is not needed
#
@container.command('rinse')
@click.argument('containers', nargs=-1)
@click.option('--all', is_flag=True, help='rinse all containers')
def rinse(containers,all):
    """
    Stop and remove containers, accepts multiple arguments
    """
    if not containers: containers = ['None']
   
    for ctr in containers:
        if ctr != 'None': os.environ['maple_container'] = str(ctr)
        Backend().container.rinse(all)

# List all container
#
@container.command('list')
def list():
    """
    List all containers on system
    """
    Backend().container.list()
