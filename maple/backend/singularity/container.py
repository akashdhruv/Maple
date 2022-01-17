"""Python API for singularity interface in maple"""

import os

def commit():
    """
    Commit changes from local container to local image
    """
    print("[maple] command not available for singularity backend")

def pour():
    """
    Pour local image in a container, opposite of maple rinse
    """
    print("[maple] command not available for singularity backend")

def rinse(container='None'):
    """
    Stop and remove the local container, opposite of maple pour
    """
    if container != 'None': os.environ['maple_container'] = str(container)
    print("[maple] command not available for singularity backend")

def clean(container='None'):
    """
    clean local container environment
    """
    if container != 'None': os.environ['maple_container'] = str(container)
    os.system('rm -f -v $maple_container.sif')

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

def execute(command,commit_flag=False):
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

    if commit_flag: print("[maple] Cannot commit to local image")

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
    print("[maple] command not available for singularity backend")
