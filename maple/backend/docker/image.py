"""Python API for docker interface in maple"""

import os

from . import container

def build(as_root=False,cmd_list=[]):
    """
    Builds a local image from remote image
 
    Arguments
    ---------
    as_root    : Build image as root (True/False)
    cmd_list   : Command list for build
    """
    # Set Dockerfile for the build
    dockerfile_build = os.getenv('maple_home')+'/context/Dockerfile.'+os.getenv('maple_image')

    # Select the base and user Dockerfile
    dockerfile_base  = os.getenv('maple_dir')+'/resources/Dockerfile.base'

    if as_root:
        dockerfile_user = os.getenv('maple_dir')+'/resources/Dockerfile.root'
    else:
        dockerfile_user = os.getenv('maple_dir')+'/resources/Dockerfile.user'


    # Populate Dockerfile for the build
    os.system('cat {0} > {1}'.format(dockerfile_base,dockerfile_build))

    dockerfile = open('{0}'.format(dockerfile_build), 'a')  # append mode

    if cmd_list:
        for command in cmd_list: dockerfile.write('\n RUN {0} \n'.format(command))

    dockerfile.close()

    os.system('cat {0} >> {1}'.format(dockerfile_user,dockerfile_build))

    # execute docker build
    os.system('docker build -t $maple_image --no-cache \
                                   --build-arg maple_base=$maple_base \
                                   --build-arg maple_user=$maple_user \
                                   --build-arg maple_group=$maple_group \
                                   --file={0} \
                                   $maple_home/context'.format(dockerfile_build))

    #os.system('rm $maple_home/context/Dockerfile.build')

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

def squash():
    """
    Squash an image and remove layers
    """
    os.environ['maple_container'] = os.environ['maple_image']+'_container'

    container.pour()
    os.system('docker export $maple_container > $maple_image.tar')
    os.system('cat $maple_image.tar | docker import - $maple_image')
    os.system('rm $maple_image.tar')
    container.rinse()

def scan(image):
    """
    Scan an image

    Arguments
    ---------
    image : image name

    """
    os.system('docker scan {0}'.format(image))

def delete():
    """
    Delete an image
    """
    os.system('docker rmi $maple_image $(docker images --filter dangling=true -q --no-trunc)')
