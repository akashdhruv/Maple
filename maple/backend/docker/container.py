"""Python API for docker interface in maple"""

import os
import random

def commit(image):
    """
    Commit changes from local container to local image

    Arguments
    ---------
    image : image name
    """
    os.system('docker commit $maple_container {0}'.format(image))

def pour(image,options=''):
    """
    Pour local image in a container, opposite of maple rinse

    Arguments
    ---------
    image   : image name
    options : string of options

    """
    result = os.system('docker run {0} -dit --name $maple_container \
                                   --mount type=bind,source=$maple_source,target=$maple_target \
                                   {1} bash'.format(options,image))

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
        os.system('docker stop $(docker ps -aq)')
        os.system('docker rm $(docker ps -aq)')
    else:
        os.system('docker stop {0}'.format(container))
        os.system('docker rm {0}'.format(container))

def shell():
    """
    Get shell access to the local container
    """
    os.system('docker exec -it --workdir $maple_target $maple_container bash')

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
    result = os.system('docker run --name $maple_container \
                                   --mount type=bind,source=$maple_source,target=$maple_target \
                                   --workdir $maple_target \
                                   {0} bash -c {1}'.format(image,str(command)))

    rinse()

    if result != 0: raise Exception("[maple] Error inside container")

def execute(command):
    """
    Run local image in a container

    Arguments
    ---------
    command : command string
    """
    command = '"{0}"'.format(command)
    result = os.system('docker exec --workdir $maple_target $maple_container bash -c {0}'.format(str(command)))

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

    pour(image,options='-p {0}:{0}'.format(port))
    result = execute('jupyter notebook --port={0} --no-browser --ip=0.0.0.0'.format(port))
    rinse()

    if result != 0: raise Exception("[maple] Error inside container")

def list():
    """
    List all containers on system
    """
    os.system('docker container ls -a')
