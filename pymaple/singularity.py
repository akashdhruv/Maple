"""Python API for singularity interface in maple"""

import os
import warnings

from . import docker

def build(image=None,root=False):
    """
    Builds a local image from remote image
    """
    os.system('singularity build $maple_container.sif docker://$maple_image')

def commit():
    """
    Commit changes from local container to local image
    """
    print("[maple] command not available for singularity backend")

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

def login():
    """
    Login to container account
    """
    print("[maple] command not available for singularity backend")

def rinse(container=None):
    """
    Stop and remove the local container, opposite of maple pour
    """
    print("[maple] command not available for singularity backend")

def shell():
    """
    Get shell access to the local container
    """
    if(os.getenv('maple_source') and os.getenv('maple_target')):
        os.system('singularity shell --containall --cleanenv \
                                                  --bind $maple_source:$maple_target \
                                                  --pwd $maple_target $maple_container.sif')
    else:
        os.system('singularity shell --containall --cleanenv \
                                                  --pwd $maple_target $maple_container.sif')

def execute(command):
    """
    Run local image in a container
    """
    command='"{0}"'.format(command)
    if(os.getenv('maple_source') and os.getenv('maple_target')):
        result = os.system('singularity exec --containall --cleanenv \
                                             --bind $maple_source:$maple_target \
                                             --pwd $maple_target \
                                             $maple_container.sif bash -c {0}'.format(str(command)))
    else:
        result = os.system('singularity exec --containall --cleanenv \
                                             --pwd $maple_target \
                                             $maple_container.sif bash -c {0}'.format(str(command)))

    if result != 0: raise Exception("[maple] Error inside container")

def notebook():
    """
    Launch ipython notebook inside the container
    """
    execute('jupyter notebook --port=$maple_port --no-browser --ip=0.0.0.0')

def images():
    """
    List all images on system
    """
    os.system('ls *.sif 2> /dev/null')

def containers():
    """
    List all containers on system
    """
    print("[maple] command not available for singularity backend")

def squash(container=None):
    """
    Squash an image and remove layers
    """
    if container: os.environ['maple_container'] = str(container)
    print("[maple] command not available for singularity backend")

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
    print("[maple] command not available for singularity backend")

def prune():
    """
    Prune system
    """
    os.system('singularity cache clean')
