"""Python API for docker interface in maple"""

import os

from . import container

def build(base=None,as_root=False):
    """
    Builds a local image from remote image
    """
    if base: os.environ['maple_base'] = str(base)

    if as_root:
        dockerfile = 'resources/Dockerfile.root'
    else:
        dockerfile = 'resources/Dockerfile.user'

    os.system('docker build -t $maple_container --no-cache \
                                                --build-arg maple_base=$maple_base \
                                                --build-arg maple_user=$maple_user \
                                                --build-arg maple_group=$maple_group \
                                                --file=$maple_dir/{0} .'.format(dockerfile))

def pull(base=None):
    """
    Pull remote image
    """
    if base: os.environ['maple_base'] = str(base)
    os.system('docker pull ${maple_base}')

def get(base):
    """
    Get tag from a base image
    """
    os.environ['maple_base'] = str(base)
    os.system('docker tag $maple_base $maple_container') 

def set(base):
    """
    Set tag for a base image
    """
    os.environ['maple_base'] = str(base)
    os.system('docker tag $maple_container $maple_base')

def push(base=None):
    """
    Push local image to remote tag/image
    """
    if base: os.environ['maple_base'] = str(base)
    os.system('docker tag $maple_container $maple_base')
    os.system('docker push $maple_base')

def list():
    """
    List all images on system
    """
    os.system('docker images')

def squash():
    """
    Squash local image and remove layers
    """
    container.pour()
    os.system('docker export $maple_container > $maple_container.tar')
    os.system('cat $maple_container.tar | docker import - $maple_container')
    os.system('rm $maple_container.tar')
    container.rinse()

def clean(local='None'):
    """
    clean local container environment
    """
    if local != 'None': os.environ['maple_container'] = str(local)
    os.system('docker rmi $maple_container $(docker images --filter dangling=true -q --no-trunc)')

def remove(base='None'):
    """
    Remove a remote image
    """
    if base != 'None': os.environ['maple_base'] = str(base)
    os.system('docker rmi $maple_base')
