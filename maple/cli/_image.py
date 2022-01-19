"""Python CLI for maple"""

import click
import os

from .. import backend
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
# The modulermation supplied from Maplefile
@image.command(name='build')
@click.argument('image')
@click.option('--base', default=None, help='value for the base image')
@click.option('--as-root', is_flag=True, help='flag to build image as root')
def build(image,base,as_root):
    """
    Builds a local image from a base image
    """
    backend.dict[os.getenv('maple_backend')].image.build(image,base,as_root)

# Pull base image from a remote registry
@maple.command(name='pull')
@click.argument('image')
def pull(image):
    """
    Pull an image from remote registry
    """
    backend.dict[os.getenv('maple_backend')].image.pull(image)

# Push image to remote registry
# Note will require 'maple login' if credentials are required
#
@maple.command(name='push')
@click.argument('image')
def push(image):
    """
    Push an image to remote registry
    """
    backend.dict[os.getenv('maple_backend')].image.push(image)

# Tag an image from base
@image.command(name='tag')
@click.argument('base')
@click.argument('image')
def tag(base,image):
    """
    Tag an image from base image
    """
    backend.dict[os.getenv('maple_backend')].image.tag(base,image)

# List all images
#
@image.command('list')
def list():
    """
    List all images on system
    """
    backend.dict[os.getenv('maple_backend')].image.list()

# Squash and prune layers
#
@image.command('squash')
@click.argument('image')
def squash(image):
    """
    Squash and prune layers from local image
    """
    backend.dict[os.getenv('maple_backend')].image.squash(image)

# Clean all local images and containers
#
@image.command('delete')
@click.argument('image')
def delete(image):
    """
    Delete a local image
    """
    backend.dict[os.getenv('maple_backend')].image.delete(image)
