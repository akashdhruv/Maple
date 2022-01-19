"""Python API for singularity interface in maple"""

import os

def build(image,base=None,as_root=False):
    """
    Builds a local image from remote image
    """
    if base: os.environ['maple_base'] = str(base)
    os.system('singularity build {0}.sif $maple_base'.format(image))
    os.system('mv ${0}.sif $maple_home/${0}.sif'.format(image))

def pull(image):
    """
    Pull remote image
    """
    print("[maple] command not available for singularity backend")

def push(image):
    """
    Push local image to remote tag/image
    """
    print("[maple] command not available for singularity backend")

def tag(base,image):
    """
    Tag an image from base
    """
    os.system('cp $maple_home/{0}.sif $maple_home/{1}.sif'.format(base,image))

def list():
    """
    List all images on system
    """
    os.system('ls $maple_home/*.sif 2> /dev/null')

def squash(image):
    """
    Squash an image and remove layers
    """
    print("[maple] command not available for singularity backend")

def delete(image):
    """
    Delete an image
    """
    os.system('rm -f -v $maple_home/{0}.sif'.format(image))
