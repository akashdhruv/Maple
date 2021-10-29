"""Python API for docker interface in maple"""

import os


def _set_env(maple):
    """
    set environment variable
    """
    pass

def build(image=None):
    """
    Builds a local image from remote image
    """
    if(image): os.environ['maple_image'] = str(image)

    os.system('docker build -t ${maple_container}_image --build-arg maple_image=$maple_image \
                                                        --build-arg maple_target=$maple_target \
                                                        --build-arg maple_source=$maple_source \
                                                        --build-arg maple_user=$maple_user \
                                                        --build-arg maple_group=$maple_group \
                                                        --build-arg maple_parfile=$maple_parfile .')

def commit():
    """
    Commit changes from local container to local image
    """
    os.system('docker commit $maple_container ${maple_container}_image')

def pull(image=None):
    """
    Pull remote image
    """
    if image: os.environ['maple_image'] = str(image)
    os.system('docker pull ${maple_image}')

def push(tag):
    """
    Push local image to remote tag/image
    """
    os.environ['maple_pushtag'] = str(tag)
    os.system('docker tag ${maple_container}_image $maple_pushtag')
    os.system('docker push $maple_pushtag')

def login():
    """
    Login to docker account
    """
    os.system('docker login')

def run(nprocs):
    """
    Run local image in a container
    """
    os.environ['maple_procs'] = str(nprocs)

    if(os.getenv('maple_source') and os.getenv('maple_target')):
        os.system('docker run --name $maple_container \
                              --env maple_procs\
                              --mount type=bind,source=$maple_source,target=$maple_target \
                              ${maple_container}_image')
    else:
        os.system('docker run --name $maple_container \
                              --env maple_procs \
                              ${maple_container}_image')

    os.system('docker rm ${maple_container}')

def pour():
    """
    Pour local image in a container, opposite of maple rinse
    """
    if(os.getenv('maple_source') and os.getenv('maple_target')):
        os.system('docker run -dit --name $maple_container \
                                   --env maple_procs \
                                   --mount type=bind,source=$maple_source,target=$maple_target \
                                   ${maple_container}_image bash')
    else:
        os.system('docker run -dit --name $maple_container --env maple_procs ${maple_container}_image bash')

def bash():
    """
    Get shell access to the local container
    """
    os.system('docker exec -it $maple_container bash')

def execute(command):
    """
    Run local image in a container
    """
    print(command)
    os.system('docker exec $maple_container bash -c {0}'.format(command))

def rinse(container=None):
    """
    Stop and remove the local container, opposite of maple pour
    """
    if container: os.environ['maple_container'] = str(container)
    os.system('docker stop $maple_container')
    os.system('docker rm $maple_container')

def images():
    """
    List all images on system
    """
    os.system('docker images -a')

def containers():
    """
    List all containers on system
    """
    os.system('docker container ls -a')

def clean(container=None):
    """
    clean local container environment
    """
    if container: os.environ['maple_container'] = str(container)
    os.system('docker stop $maple_container')
    os.system('docker rm $maple_container')
    os.system('docker rmi ${maple_container}_image')

def remove(image=None):
    """
    Remove a remote image
    """
    if image: os.environ['maple_image']=str(image)
    os.system('docker rmi $maple_image')

def prune():
    """
    Prune system
    """
    os.system('docker system prune -a')
