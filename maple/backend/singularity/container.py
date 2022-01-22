"""Python API for singularity interface in maple"""

import os
import random

def commit(image):
    """
    Commit changes from local container to local image

    Arguments
    ---------
    image : image name
    """
    print("[maple.container.commit] not available for singularity backend")

def pour(image,options='--no-home'):
    """
    Pour local image in a container, opposite of maple rinse


    Arguments
    ---------
    image : image name
    options : string of options
    """
    result = os.system('singularity instance start {0} \
                                                   --bind $maple_source:$maple_target \
                                                   $maple_home/images/{1}.sif \
                                                   $maple_container'.format(options,image))

    if result != 0: raise Exception("[maple] Error inside container")

def rinse(container='None',rinse_all=False):
    """
    Stop and remove the local container, opposite of maple pour

    Arguments
    ---------
    container : name of the container to rinse
    rinse_all : (True/Flase) flag to rinse all container
    """
    if container == 'None': container = os.getenv('maple_container')

    if rinse_all:
        os.system('singularity instance stop --all')
    else:
        os.system('singularity instance stop {0}'.format(container))

def shell():
    """
    Get shell access to the local container
    """
    os.system('singularity shell --pwd $maple_target instance://$maple_container')

def run(image,command):
    """
    Run and rinse the local container

    Arguments
    ---------
    image : image name
    command : command string
    """
    os.environ['maple_container'] = os.getenv('maple_container')+'_'+str(random.randint(1111,9999))

    command = '"{0}"'.format(command)
    result = os.system('singularity exec --no-home \
                                         --bind $maple_source:$maple_target \
                                         --pwd  $maple_target \
                                         $maple_home/images/{0}.sif bash -c {1}'.format(image,str(command)))

    if result != 0: raise Exception("[maple] Error inside container")

def execute(command):
    """
    Run local image in a container

    Arguments
    ---------
    command : command string
    """
    command = '"{0}"'.format(command)
    result = os.system('singularity exec --pwd $maple_target \
                                         instance://$maple_container bash -c {0}'.format(str(command)))

    return result

def notebook(image,port='8888'):
    """
    Launch ipython notebook inside the container

    Arguments
    ---------
    image : image name
    port  : port id ('8888')
    """
    os.environ['maple_container'] = os.getenv('maple_container')+'_'+str(random.randint(1111,9999))

    pour(image,options='--cleanenv')
    result = execute('jupyter notebook --port={0} --no-browser --ip=0.0.0.0'.format(port))
    rinse()

    if result != 0: raise Exception("[maple] Error inside container")

def list():
    """
    List all containers on system
    """
    os.system('singularity instance list')
