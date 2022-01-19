"""Python API for docker interface in maple"""

import os

def commit(image):
    """
    Commit changes from local container to local image
    """
    os.system('docker commit $maple_container {0}'.format(image))

def pour(image):
    """
    Pour local image in a container, opposite of maple rinse
    """
    if(os.getenv('maple_source') and os.getenv('maple_target')):
        result = os.system('docker run -dit --name $maple_container \
                                       --mount type=bind,source=$maple_source,target=$maple_target \
                                       {0} bash'.format(image))
    else:
        result = os.system('docker run -dit --name $maple_container \
                                       {0} bash'.format(image))

    if result != 0: raise Exception("[maple] Error inside container")

def rinse(container='None'):
    """
    Stop and remove the local container, opposite of maple pour
    """
    if container == 'None': container = os.getenv('maple_container')
    os.system('docker stop {0}'.format(container))
    os.system('docker rm {0}'.format(container))

def shell():
    """
    Get shell access to the local container
    """
    os.system('docker exec -it --workdir $maple_target $maple_container bash')

def execute(command):
    """
    Run local image in a container
    """
    command = '"{0}"'.format(command)
    result = os.system('docker exec --workdir $maple_target $maple_container bash -c {0}'.format(str(command)))
  
    if result != 0: raise Exception("[maple] Error inside container")

def notebook(port='8888'):
    """
    Launch ipython notebook inside the container
    """
    execute('jupyter notebook --port={0} --no-browser --ip=0.0.0.0'.format(port))

def list():
    """
    List all containers on system
    """
    os.system('docker container ls -a')
