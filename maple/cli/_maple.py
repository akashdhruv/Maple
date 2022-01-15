"""Python CLI for maple"""

import click
import os

from .. import api

# CLI group
#
@click.group(name='maple')
def maple():
    """
    Simple CLI for using docker/singularity containers for HPC applications
    """
    # Check if required environment variables are defined in the Maplefile
    # If not then assign default values

    # VARIABLE                                             DESCRIPTION
    # ----------------------------------------------------------------
    # maple_user                Name of the user - usually current user
    # maple_group               Name of the users group
    # maple_image               Name of the image in remote registry    
    # maple_container           Name of the local container
    # maple_target              Name of the target dir to mount source dir
    # maple_source              Name of the source dir - usually $PWD
    # maple_port                Port ID for the container (used when running jupyter notebooks)
    # maple_docker              Container backend (docker/singularity)

    if not os.getenv('maple_backend'): os.environ['maple_backend'] = 'docker'
    if not os.getenv('maple_user'): os.environ['maple_user'] = os.popen('id -u').read().split()[0]
    if not os.getenv('maple_group'): os.environ['maple_group'] = os.popen('id -g').read().split()[0]
    if not os.getenv('maple_port'): os.environ['maple_port'] = '8888'

    # Condition to check if target and source directories are defined in the Maplefile
    # assign default if they are not, and deal with execptions
    if not os.getenv('maple_target'):
        os.environ['maple_target'] = '/home'
        if os.getenv('maple_source'): del os.environ['maple_source']
    else:
        if not os.getenv('maple_source'): os.environ['maple_source'] = os.getenv('PWD')

# Build a container using the information supplied from Maplefile
# Currently this uses a docker build, but we intend this interface to be more general depending
# on the type of backend use for containerization
#
@maple.command(name='build')
@click.option('--image',default=os.getenv('maple_image'),help='overwrite current remote image')
@click.option('--as-root/--no-as-root', default=False)
def build(image,as_root):
    """
    Builds a local image from remote image
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].build(image,as_root)

# Commit changes to a container
# Saves changes to local container as an image, currently uses docker
#
@maple.command(name='commit')
def commit():
    """
    Commit changes from local container to local image
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].commit()

# Pull image from remote registry
# Currently pulls maple_image for a remote registry
#
@maple.command(name='pull')
@click.option('--image',default=os.getenv('maple_image'),help='overwrite current remote image')
def pull(image):
    """
    Pull remote image
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].pull(image)

# Push image to remote registry
# Tag and push changes to local container to remote registry
# Note will require 'maple login' if credentials are required
#
@maple.command(name='push')
@click.argument('tag')
def push(tag):
    """
    Push local image to remote tag/image
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].push(tag)

# Login to remote registry
#
@maple.command(name='login')
def login():
    """
    Login to container backend
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].login()

# Enter the shell environment of a container
#
@maple.command('shell')
def shell():
    """
    Get shell access to the local container
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].shell()

# Launch a notebook inside the container
#
@maple.command('notebook')
def notebook():
    """
    Launch ipython notebook inside the container
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].notebook()

# Execute a command in a container
@maple.command('execute')
@click.argument('command',default='echo Hello World!')
def execute(command):
    """
    Execute command in a container
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].execute(command)

# Pour an image in a local container to access interactive shell
# If maple_source or maple_traget are present then they will be mounted inside the containter.
# This is useful for mounting maple_source for development
#
@maple.command('pour')
def pour():
    """
    Pour local image in a container
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].pour()

# Rinse a local container
# Do this if the local container is not needed
#
@maple.command('rinse')
@click.argument('container',default=os.getenv('maple_container'))
def rinse(container):
    """
    Remove the local container
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].rinse(container)

# List all images
#
@maple.command('images')
@click.argument('backend',default=os.getenv('maple_backend'))
def images(backend):
    """
    List all images on system
    """
    os.environ['maple_backend'] = str(backend)
    api.Maple.dict_backend[os.getenv('maple_backend')].images()

# List all container
#
@maple.command('containers')
@click.argument('backend',default=os.getenv('maple_backend'))
def containers(backend):
    """
    List all containers on system
    """
    os.environ['maple_backend'] = str(backend)
    api.Maple.dict_backend[os.getenv('maple_backend')].containers()

# Squash and prune layers
#
@maple.command('squash')
@click.argument('container',default=os.getenv('maple_container'))
def squash(container):
    """
    Squash and prune layers from local container and save it to local image
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].squash(container)

# Clean all local images and containers
#
@maple.command('clean')
@click.argument('container',default=os.getenv('maple_container'))
def clean(container):
    """
    Clean local image/container environment
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].clean(container)

# Delete a remote image
#
@maple.command('remove')
@click.argument('image',default=os.getenv('maple_image'))
def remove(image):
    """
    Remove a remote image from local cache
    """
    api.Maple.dict_backend[os.getenv('maple_backend')].remove(image)

# Prune system
#
@maple.command('prune')
@click.argument('backend',default=os.getenv('maple_backend'))
def prune(backend):
    """
    Prune system
    """
    os.environ['maple_backend'] = str(backend)
    api.Maple.dict_backend[os.getenv('maple_backend')].prune()
