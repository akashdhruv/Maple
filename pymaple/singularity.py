"""Python API for singularity interface in maple"""

import os
import warnings

def build(image=None,root=False):
    """
    Builds a local image from remote image
    """
    if(image): os.environ['maple_image'] = str(image)
    os.system('singularity build $maple_container.sif docker://$maple_image')

def commit():
    """
    Commit changes from local container to local image
    """
    raise NotImplementedError('[maple] command not implemented for singularity backend')

def pull(image=None):
    """
    Pull remote image
    """
    if image: os.environ['maple_image'] = str(image)
    os.system('singularity pull docker://$maple_image')

def push(tag):
    """
    Push local image to remote tag/image
    """
    os.environ['maple_pushtag'] = str(tag)
    raise NotImplementedError('[maple] command not implemented for singularity backend')

def login():
    """
    Login to docker account
    """
    raise NotImplementedError('[maple] command not implemented for singularity backend')

def run(command):
    """
    Run local image in a container
    """
    pour()
    execute(command)
    rinse()

def pour():
    """
    Pour local image in a container, opposite of maple rinse
    """
    print("[maple] command is a stub for singularity backend")

def bash():
    """
    Get shell access to the local container
    """
    os.system('singularity shell $maple_container.sif')

def execute(command):
    """
    Run local image in a container
    """
    result = os.system('singularity exec $maple_container.sif {0}'.format(str(command)))

    if result != 0: raise Exception("[maple] Error inside container")

def notebook():
    """
    Launch ipython notebook inside the container
    """
    execute('jupyter notebook --port=$maple_port --no-browser --ip=0.0.0.0')

def rinse(container=None):
    """
    Stop and remove the local container, opposite of maple pour
    """
    if container: os.environ['maple_container'] = str(container)
    print("[maple] command is a stub for singularity backend")

def images():
    """
    List all images on system
    """
    os.system('docker images -a')
    os.system('ls *.sif 2> /dev/null')

def containers():
    """
    List all containers on system
    """
    os.system('docker container ls -a')

def squash(container=None):
    """
    Squash an image and remove layers
    """
    if container: os.environ['maple_container'] = str(container)
    raise NotImplementedError('[maple] command not implemented for singularity backend')

def clean(container=None):
    """
    clean local container environment
    """
    if container: os.environ['maple_container'] = str(container)
    os.system('rm -f -v $maple_container.sif')

def remove(image=None):
    """
    Remove a remote image
    """
    if image: os.environ['maple_image']=str(image)
    os.system('rm -f -v $maple_image.sif')

def prune():
    """
    Prune system
    """
    os.system('singularity cache clean')
