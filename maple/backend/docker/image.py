"""Python API for docker interface in maple"""

import os

from . import container

def build(image=None,root=False):
    """
    Builds a local image from remote image
    """
    if(image): os.environ['maple_image'] = str(image)

    if root:
        dockerfile = 'resources/Dockerfile.root'
    else:
        dockerfile = 'resources/Dockerfile.user'

    os.system('docker build -t $maple_container --no-cache \
                                                --build-arg maple_image=$maple_image \
                                                --build-arg maple_target=$maple_target \
                                                --build-arg maple_user=$maple_user \
                                                --build-arg maple_group=$maple_group \
                                                --file=$maple_dir/{0} .'.format(dockerfile))

def pull(image=None):
    """
    Pull remote image
    """
    if image: os.environ['maple_image'] = str(image)
    os.system('docker pull ${maple_image}')

def push(tag):
    """
    Push local image to remote tag/image
    """
    os.environ['maple_pushtag'] = str(tag)
    os.system('docker tag $maple_container $maple_pushtag')
    os.system('docker push $maple_pushtag')

def list():
    """
    List all images on system
    """
    os.system('docker images -a')

def squash(image=None):
    """
    Squash local image and remove layers
    """
    if image: os.environ['maple_container'] = str(image)
    container.pour()
    os.system('docker export $maple_container > $maple_container.tar')
    os.system('cat $maple_container.tar | docker import - $maple_container')
    os.system('rm $maple_container.tar')
    container.rinse()

def clean(image=None):
    """
    clean local container environment
    """
    if image: os.environ['maple_container'] = str(image)
    os.system('docker rmi $maple_container $(docker images --filter dangling=true -q --no-trunc)')

def remove(image=None):
    """
    Remove a remote image
    """
    if image: os.environ['maple_image']=str(image)
    os.system('docker rmi $maple_image')
