"""Python API for singularity interface in maple"""

import os

def build(base=None,as_root=False):
    """
    Builds a local image from remote image
    """
    if(base): os.environ['maple_base'] = str(base)
    os.system('singularity build $maple_container.sif docker://$maple_base')

def pull(base=None):
    """
    Pull remote image
    """
    if(base): os.environ['maple_base'] = str(base)
    print("[maple] command not available for singularity backend")

def push(base=None):
    """
    Push local image to remote tag/image
    """
    if base: os.environ['maple_base'] = str(base)
    print("[maple] command not available for singularity backend")

def tag(base):
    """
    Retag an image
    """
    if base: os.environ['maple_base'] = str(base)
    os.system('cp $maple_container.sif $maple_base.sif')

def list():
    """
    List all images on system
    """
    os.system('ls *.sif 2> /dev/null')

def squash():
    """
    Squash an image and remove layers
    """
    if image: os.environ['maple_container'] = str(image)
    print("[maple] command not available for singularity backend")

def remove(base='None'):
    """
    Remove a remote image
    """
    if base != 'None': os.environ['maple_base'] = str(base)
    print("[maple] command not available for singularity backend")
