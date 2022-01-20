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
@click.argument('images', nargs=-1)
def pull(images):
    """
    Pull images from remote registry, accepts multiple arguments
    """
    for img in images:
        backend.dict[os.getenv('maple_backend')].image.pull(img)

# Push image to remote registry
# Note will require 'maple login' if credentials are required
#
@maple.command(name='push')
@click.argument('images', nargs=-1)
def push(images):
    """
    Push images to remote registry, accepts multiple arguments
    """
    for img in images:
        backend.dict[os.getenv('maple_backend')].image.push(img)

# Tag an image from base
@image.command(name='tag')
@click.argument('base')
@click.argument('target')
def tag(base,target):
    """
    Tag a target image from base image
    """
    backend.dict[os.getenv('maple_backend')].image.tag(base,target)

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
    Squash and remove layers from local image, reduces size of the image
    """
    backend.dict[os.getenv('maple_backend')].image.squash(image)

# Scan all the images
@maple.command('scan')
@click.argument('images', nargs=-1)
def scan(images):
    """
    Scan local images, accepts multiple arguments
    """
    for img in images:
        backend.dict[os.getenv('maple_backend')].image.scan(img)

# Clean all local images and containers
#
@image.command('delete')
@click.argument('images', nargs=-1)
def delete(images):
    """
    Delete local images, accepts multiple arguments
    """
    for img in images:
        backend.dict[os.getenv('maple_backend')].image.delete(img)
