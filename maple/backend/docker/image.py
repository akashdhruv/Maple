"""Python API for docker interface in maple"""

import os

from . import container

def build(image,base=None,as_root=False):
    """
    Builds a local image from remote image
    """
    if base: os.environ['maple_base'] = str(base)

    if as_root:
        dockerfile = 'resources/Dockerfile.root'
    else:
        dockerfile = 'resources/Dockerfile.user'

    os.system('docker build -t {0} --no-cache \
                                   --build-arg maple_base=$maple_base \
                                   --build-arg maple_user=$maple_user \
                                   --build-arg maple_group=$maple_group \
                                   --file=$maple_dir/{1} .'.format(image,dockerfile))

def pull(image):
    """
    Pull remote image
    """
    os.system('docker pull {0}'.format(image))

def push(image):
    """
    Push local image to remote tag/image
    """
    os.system('docker push {0}'.format(image))

def tag(base,target):
    """
    Tag an image from base
    """
    os.system('docker tag {0} {1}'.format(base,target))

def list():
    """
    List all images on system
    """
    os.system('docker images')

def squash(image):
    """
    Squash an image and remove layers
    """
    os.environ['maple_container'] = str(image+'_container')
    container.pour(image)
    os.system('docker export $maple_container > {0}.tar'.format(image))
    os.system('cat {0}.tar | docker import - {0}'.format(image))
    os.system('rm {0}.tar'.format(image))
    container.rinse()

def scan(image):
    """
    Scan an image
    """
    os.system('docker scan {0}'.format(image))

def delete(image):
    """
    Delete an image
    """
    os.system('docker rmi {0} $(docker images --filter dangling=true -q --no-trunc)'.format(image))
