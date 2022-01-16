"""Python API for docker interface in maple"""

import os

def commit():
    """
    Commit changes from local container to local image
    """
    os.system('docker commit $maple_container $maple_container')

def pour():
    """
    Pour local image in a container, opposite of maple rinse
    """
    if(os.getenv('maple_source') and os.getenv('maple_target')):
        result = os.system('docker run -p $maple_port:$maple_port -dit \
                                                --name $maple_container \
                                                --mount type=bind,source=$maple_source,target=$maple_target \
                                                $maple_container bash')
    else:
        result = os.system('docker run -p $maple_port:$maple_port -dit \
                                                --name $maple_container \
                                                $maple_container bash')

    if result != 0: raise Exception("[maple] Error inside container")

def rinse(container=None):
    """
    Stop and remove the local container, opposite of maple pour
    """
    if container: os.environ['maple_container'] = str(container)
    os.system('docker stop $maple_container')
    os.system('docker rm $maple_container')

def shell():
    """
    Get shell access to the local container
    """
    os.system('docker exec -it $maple_container bash')

def execute(command):
    """
    Run local image in a container
    """
    pour()

    command='"{0}"'.format(command)
    result = os.system('docker exec $maple_container bash -c {0}'.format(str(command)))

    rinse()

    if result != 0: raise Exception("[maple] Error inside container")

def notebook():
    """
    Launch ipython notebook inside the container
    """
    execute('jupyter notebook --port=$maple_port --no-browser --ip=0.0.0.0')

def list():
    """
    List all containers on system
    """
    os.system('docker container ls -a')
