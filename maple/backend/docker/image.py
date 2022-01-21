"""Python API for docker interface in maple"""

import os

from . import container

def build(target,base,as_root=False):
    """
    Builds a local image from remote image
 
    Arguments
    ---------
    target     : Name of the local image to be built
    base       : Name of the base image
    as_root    : Build image as root (True/False)
    """
    # Check if Dockerfile is present else use default
    if os.path.exists('Dockerfile'):
        dockerfile = 'Dockerfile'
    elif as_root:
        dockerfile = os.getenv('maple_dir')+'/resources/Dockerfile.root'
    else:
        dockerfile = os.getenv('maple_dir')+'/resources/Dockerfile.user'

    # execute docker build
    os.system('docker build -t {0} --no-cache \
                                   --build-arg maple_base={1} \
                                   --build-arg maple_user=$maple_user \
                                   --build-arg maple_group=$maple_group \
                                   --file={2} $maple_home/context'.format(target,base,dockerfile))

def pull(target,base):
    """
    Pull remote image

    Arguments
    ---------
    target : target image to pull into
    base   : base image in remote registry
    """
    os.system('docker pull {0}'.format(base))
    os.system('docker tag {0} {1}'.format(base,target))

def push(base,target):
    """
    Push local image to remote tag/image
    
    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    os.system('docker tag {0} {1}'.format(base,target))
    os.system('docker push {0}'.format(target))

def tag(base,target):
    """
    Tag a target image from base image

    Arguments
    ---------
    base   : base image
    target : target image to push
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
