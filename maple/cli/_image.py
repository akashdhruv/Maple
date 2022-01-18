"""Python CLI for maple"""

import click
import os

from .. import api
from .  import maple

# CLI group
#
@maple.group(name='image')
def image():
    """
    Image management, type maple image --help for more info
    """
    pass

# Build a container using the information supplied from Maplefile
# Currently this uses a docker build, but we intend this interface to be more general depending
# on the type of backend use for containerization
#
@image.command(name='build')
@click.option('--base', default=None, help='value for the base image')
@click.option('--as-root/--not-as-root', default=False, help='flag to build image as root')
def build(base,as_root):
    """
    Builds a local image from remote image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.build(base,as_root)

# Pull image from remote registry
# Currently pulls maple_base for a remote registry
#
@image.command(name='pull')
@click.option('--base', default=None, help='value for the base image')
def pull(base):
    """
    Pull remote image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.pull(base)

# Push image to remote registry
# Tag and push changes to local container to remote registry
# Note will require 'maple login' if credentials are required
#
@image.command(name='push')
@click.option('--base', default=None, help='value for the base image')
def push(base):
    """
    Push local image to remote tag/image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.push(base)

# Create a new tag for the base image
@image.command(name='tag')
@click.argument('base')
@click.option('--set/--not-set', default=False, help='tag a new base image from local image')
@click.option('--get/--not-get', default=False, help='tag local image from base image')
def tag(base,set,get):
    """
    Create a tag for a new image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.tag(base,set,get)

# List all images
#
@image.command('list')
@click.argument('backend', default='None')
def list(backend):
    """
    List all images on system
    """
    if backend != 'None': os.environ['maple_backend'] = str(backend)
    api.Maple.backend[os.getenv('maple_backend')].image.list()

# Squash and prune layers
#
@image.command('squash')
def squash():
    """
    Squash and prune layers from local container and save it to local image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.squash()

# Delete a remote image
#
@image.command('remove')
@click.argument('base', default='None')
def remove(base):
    """
    Remove a remote image from local cache
    """
    api.Maple.backend[os.getenv('maple_backend')].image.remove(base)
