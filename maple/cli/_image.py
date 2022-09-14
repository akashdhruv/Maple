"""
Command Line Interface (CLI) for image management.
"""

import os
import click
import toml

from ..backend import Backend
from . import maple


# CLI group
#
@maple.group(name="image")
def image():
    """
    Image management, type maple image --help for more info
    """
    pass


# Build a local image using a base image
# The modulermation supplied from Maplefile
@image.command(name="build")
@click.argument("image", default="None")
@click.option("--base", "-B", default="None", help="base image name")
@click.option("--options", "-o", default="", help="run options")
@click.option("--as-root", is_flag=True, help="flag to build image as root")
@click.option("--create-tar", is_flag=True, help="flag to save image in tar ball")
def build(image, base, options, as_root, create_tar):
    """
    Builds a local image from a base image
    """
    if base != "None":
        os.environ["maple_base"] = str(base)
    if image != "None":
        os.environ["maple_image"] = str(image)

    Maplefile = os.path.exists("Maplefile")

    cmd_list = []
    env_list = []
    if Maplefile:
        if "build" in toml.load("Maplefile"):
            cmd_list = toml.load("Maplefile")["build"]
        if "environ" in toml.load("Maplefile"):
            env_list = toml.load("Maplefile")["environ"]

    Backend().image.build(as_root, options, cmd_list, env_list, create_tar)


# Pull base image from a remote registry
@maple.command(name="pull")
@click.argument("target", required=True)
@click.argument("base", required=True)
def pull(target, base):
    """
    Pull image from remote registry
    """
    Backend().image.pull(target, base)


# Push image to remote registry
# Note will require 'maple login' if credentials are required
#
@maple.command(name="push")
@click.argument("base", required=True)
@click.argument("target", required=True)
def push(base, target):
    """
    Push image to remote registry
    """
    Backend().image.push(base, target)


# Tag an image from base
@maple.command(name="tag")
@click.argument("base", required=True)
@click.argument("target", required=True)
def tag(base, target):
    """
    Tag a target image from base image
    """
    Backend().image.tag(base, target)


# List all images
#
@image.command("list")
def list():
    """
    List all images on system
    """
    Backend().image.list()


# Squash and prune layers
#
@image.command("squash")
@click.argument("image", default="None")
def squash(image):
    """
    Squash and remove layers from local image, reduces size of the image
    """
    if image != "None":
        os.environ["maple_image"] = str(image)
    Backend().image.squash()


# Scan all the images
@maple.command("scan")
@click.argument("image", required=True)
def scan(image):
    """
    Scan local images, accepts multiple arguments
    """
    Backend().image.scan(image)


# Clean all local images and containers
#
@image.command("delete")
@click.argument("images", nargs=-1)
def delete(images):
    """
    Delete local images, accepts multiple arguments
    """
    if not images:
        images = ["None"]

    for img in images:
        if img != "None":
            os.environ["maple_image"] = str(img)
        Backend().image.delete()
