"""Python API for singularity interface in maple"""

import os

def commit(image):
    """
    Commit changes from local container to local image
    """
    print("[maple] command not available for singularity backend")

def pour(image):
    """
    Pour local image in a container, opposite of maple rinse
    """
    result = os.system('singularity instance start --containall --cleanenv \
                                                   --bind $maple_source:$maple_target \
                                                   $maple_home/images/{0}.sif $maple_container'.format(image))

    if result != 0: raise Exception("[maple] Error inside container")

def rinse(container='None'):
    """
    Stop and remove the local container, opposite of maple pour
    """
    if container == 'None': container = os.getenv('maple_container')
    os.system('singularity instance stop {0}'.format(container))

def shell():
    """
    Get shell access to the local container
    """
    os.system('singularity shell --pwd $maple_target instance://$maple_container')

def run(image,command,with_commit=False):
    """
    Run and rinse the local container
    """
    command = '"{0}"'.format(command)
    result = os.system('singularity exec --bind $maple_source:$maple_target \
                                         --pwd $maple_target \
                                         $maple_home/images/{0}.sif bash -c {1}'.format(image,command))

    if with_commit: print("[maple] cannot commit to the image")

    if result != 0: raise Exception("[maple] Error inside container")

def notebook(image,port='8888'):
    """
    Launch ipython notebook inside the container
    """
    result = os.system('singularity exec --containall --cleanenv \
                                         --bind $maple_source:$maple_target \
                                         --pwd $maple_target \
                                         $maple_home/images/{0}.sif \
                                         jupyter notebook --port={1} --no-browser --ip=0.0.0.0'.format(image,port))

    if result != 0: raise Exception("[maple] Error inside container")

def list():
    """
    List all containers on system
    """
    os.system('singularity instance list')
