"""Python API for docker interface in maple"""

import os

def build():
    """
    Builds a local image from remote image
    """
    os.system('docker build -t ${maple_container}_image --build-arg maple_image=${maple_image} \
                                                        --build-arg maple_target=${maple_target} \
                                                        --build-arg maple_source=${maple_source} \
                                                        --build-arg maple_user=${maple_user} \
                                                        --build-arg maple_group=${maple_group} \
                                                        --build-arg maple_parfile=${maple_parfile} .')

def commit():
    """
    Commit changes from local container to local image
    """
    os.system('docker commit ${maple_container} ${maple_container}_image')

def pull():
    """
    Pull remote image
    """
    os.system('docker pull ${maple_image}')

def push():
    """
    Push local image to remote tag/image
    """
    os.system('docker tag ${maple_container}_image ${maple_tag}')
    os.system('docker push ${maple_tag}')

def login():
    """
    Login to container service (currently docker)
    """
    os.system('docker login')

def run(nprocs):
    """
    Run local image in a container
    """
    os.environ['nprocs'] = str(nprocs)
    if(os.getenv('maple_source') and os.getenv('maple_target')):
        os.system('docker run --name ${maple_container} \
                              --env nprocs=$nprocs \
                              --mount type=bind,source=${maple_source},target=${maple_target} \
                              ${maple_container}_image')
    else:
        os.system('docker run --name ${maple_container} \
                              --env nprocs=$nprocs \
                              ${maple_container}_image')

def pour():
    """
    Pour local image in a container, opposite of maple rinse
    """
    if(os.getenv('maple_source') and os.getenv('maple_target')):
        os.system('docker run -dit --name ${maple_container} \
                                   --mount type=bind,source=${maple_source},target=${maple_target} \
                                   ${maple_container}_image bash')
    else:
        os.system('docker run -dit --name ${maple_container} ${maple_container}_image bash')

def bash():
    """
    Get shell access to the local container
    """
    os.system('docker exec -it ${maple_container} bash')

def rinse():
    """
    Stop and remove the local container, opposite of maple pour
    """
    os.system('docker stop ${maple_container}')
    os.system('docker rm ${maple_container}')

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

def clean():
    """
    clean local container environment
    """
    os.system('docker stop ${maple_container}')
    os.system('docker rm ${maple_container}')
    os.system('docker rmi ${maple_container}_image')

def remove():
    """
    Remove a remote image
    """
    os.system('docker rmi ${maple_image}')

def prune():
    """
    Prune system
    """
    os.system('docker system prune -a')
