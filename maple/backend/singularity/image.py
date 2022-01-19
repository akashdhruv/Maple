"""Python API for singularity interface in maple"""

import os

def build(base=None,as_root=False):
    """
    Builds a local image from remote image
    """
    if(base): os.environ['maple_base'] = str(base)
    os.system('singularity build $maple_container.sif $maple_base')
    os.system('mv $maple_container.sif $maple_home/$maple_container.sif')

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

def get(base):
    """
    Get tag from a base image
    """
    os.environ['maple_base'] = str(base)
    os.system('cp $maple_home/$maple_base.sif $maple_home/$maple_container.sif')

def set(base):
    """
    Set tag for a base image
    """
    os.environ['maple_base'] = str(base)
    os.system('cp $maple_home/$maple_container.sif $maple_home/$maple_base.sif')

def list():
    """
    List all images on system
    """
    os.system('ls $maple_home/*.sif 2> /dev/null')

def squash():
    """
    Squash an image and remove layers
    """
    if image: os.environ['maple_container'] = str(image)
    print("[maple] command not available for singularity backend")

def clean(local='None'):
    """
    clean local container environment
    """
    if local != 'None': os.environ['maple_container'] = str(local)
    os.system('rm -f -v $maple_home/$maple_container.sif')

def remove(base='None'):
    """
    Remove a remote image
    """
    if base != 'None': os.environ['maple_base'] = str(base)
    print("[maple] command not available for singularity backend")
