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
@click.option('--remote',default=os.getenv('maple_image'),help='overwrite current remote image')
@click.option('--as-root', is_flag=False)
def build(remote,as_root):
    """
    Builds a local image from remote image
    """
    api.MapleEnv.backend[os.getenv('maple_backend')].image.build(remote,as_root)

# Pull image from remote registry
# Currently pulls maple_image for a remote registry
#
@image.command(name='pull')
@click.option('--remote',default=os.getenv('maple_image'),help='overwrite current remote image')
def pull(remote):
    """
    Pull remote image
    """
    api.MapleEnv.backend[os.getenv('maple_backend')].image.pull(remote)

# Push image to remote registry
# Tag and push changes to local container to remote registry
# Note will require 'maple login' if credentials are required
#
@image.command(name='push')
@click.argument('tag')
def push(tag):
    """
    Push local image to remote tag/image
    """
    api.MapleEnv.backend[os.getenv('maple_backend')].image.push(tag)

# List all images
#
@image.command('list')
def list():
    """
    List all images on system
    """
    api.MapleEnv.backend[os.getenv('maple_backend')].image.list()

# Squash and prune layers
#
@image.command('squash')
@click.argument('image',default=os.getenv('maple_container'))
def squash(image):
    """
    Squash and prune layers from local container and save it to local image
    """
    api.MapleEnv.backend[os.getenv('maple_backend')].image.squash(image)

# Clean all local images and containers
#
@image.command('clean')
@click.argument('image',default=os.getenv('maple_container'))
def clean(image):
    """
    Clean local image/container environment
    """
    api.MapleEnv.backend[os.getenv('maple_backend')].image.clean(image)

# Delete a remote image
#
@image.command('remove')
@click.argument('image',default=os.getenv('maple_image'))
def remove(image):
    """
    Remove a remote image from local cache
    """
    api.MapleEnv.backend[os.getenv('maple_backend')].image.remove(image)
