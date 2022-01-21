"""Python API for singularity interface in maple"""

import os
import random

def commit(image):
    """
    Commit changes from local container to local image
    """
    print("[maple.container.commit] not available for singularity backend")

def pour(image,options='--no-home'):
    """
    Pour local image in a container, opposite of maple rinse
    """
    result = os.system('singularity instance start {0} \
                                                   --bind $maple_source:$maple_target \
                                                   $maple_home/images/{1}.sif \
                                                   $maple_container'.format(options,image))

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

def run(image,command):
    """
    Run and rinse the local container
    """
    os.environ['maple_container'] = os.getenv('maple_container')+'_'+str(random.randint(1111,9999))

    command = '"{0}"'.format(command)

    pour(image)
    result = execute(command)
    rinse()

    if result != 0: raise Exception("[maple] Error inside container")

def execute(command):
    """
    Run local image in a container
    """
    command = '"{0}"'.format(command)
    result = os.system('singularity exec --pwd $maple_target \
                                         instance://$maple_container bash -c {0}'.format(str(command)))

    return result

def notebook(image,port='8888'):
    """
    Launch ipython notebook inside the container
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
