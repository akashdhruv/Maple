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

# Build a local image using a base image 
# The information supplied from Maplefile
@image.command(name='build')
@click.option('--base', default=None, help='value for the base image')
@click.option('--as-root/--not-as-root', default=False, help='flag to build image as root')
def build(base,as_root):
    """
    Builds a local image from a base image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.build(base,as_root)

# Pull base image from a remote registry
@image.command(name='pull')
@click.option('--base', default=None, help='value for the base image')
def pull(base):
    """
    Pull a base image from remote registry
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
    Push local image to a base image in remote registry
    """
    api.Maple.backend[os.getenv('maple_backend')].image.push(base)

# Get tag from a base image
@image.command(name='get')
@click.argument('base')
def get(base):
    """
    Tag local image from a base image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.get(base)

# Set tag from a base image
@image.command(name='set')
@click.argument('base')
def set(base):
    """
    Set local image for a base image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.set(base)

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

# Clean all local images and containers
#
@image.command('clean')
@click.argument('local',default='None')
def clean(local):
    """
    Clean local image
    """
    api.Maple.backend[os.getenv('maple_backend')].image.clean(local)

# Delete a remote image
#
@image.command('remove')
@click.argument('base', default='None')
def remove(base):
    """
    Remove a base image from local cache
    """
    api.Maple.backend[os.getenv('maple_backend')].image.remove(base)
