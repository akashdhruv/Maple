"""Python API for singularity interface in maple"""

import os

def build(image=None,root=False):
    """
    Builds a local image from remote image
    """
    os.system('singularity build $maple_container.sif docker://$maple_image')

def pull(image=None):
    """
    Pull remote image
    """
    print("[maple] command not available for singularity backend")

def push(tag):
    """
    Push local image to remote tag/image
    """
    print("[maple] command not available for singularity backend")

def list():
    """
    List all images on system
    """
    os.system('ls *.sif 2> /dev/null')

def squash(image=None):
    """
    Squash an image and remove layers
    """
    if image: os.environ['maple_container'] = str(image)
    print("[maple] command not available for singularity backend")

def clean(image=None):
    """
    clean local container environment
    """
    if image: os.environ['maple_container'] = str(image)
    os.system('rm -f -v $maple_container.sif')

def remove(image=None):
    """
    Remove a remote image
    """
    print("[maple] command not available for singularity backend")
