"""Python API for docker interface in maple"""

import os

def build(image=None,root=False):
    """
    Builds a local image from remote image
    """
    if(image): os.environ['maple_image'] = str(image)

    if root:
        dockerfile = 'resources/dockerfile.root'
    else:
        dockerfile = 'resources/dockerfile.user'

    os.system('docker build -t $maple_container --no-cache \
                                                --build-arg maple_image=$maple_image \
                                                --build-arg maple_target=$maple_target \
                                                --build-arg maple_user=$maple_user \
                                                --build-arg maple_group=$maple_group \
                                                --file=$maple_dir/pymaple/{0} .'.format(dockerfile))
def commit():
    """
    Commit changes from local container to local image
    """
    os.system('docker commit $maple_container $maple_container')

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
    os.system('docker tag $maple_container $maple_pushtag')
    os.system('docker push $maple_pushtag')

def login():
    """
    Login to docker account
    """
    os.system('docker login')

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
    pour()
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

def squash(container=None):
    """
    Squash an image and remove layers
    """
    if container: os.environ['maple_container'] = str(container)
    os.system('docker export $maple_container > $maple_container.tar')
    os.system('cat $maple_container.tar | docker import - $maple_container')
    os.system('rm $maple_container.tar')

def clean(container=None):
    """
    clean local container environment
    """
    if container: os.environ['maple_container'] = str(container)
    os.system('docker rmi $maple_container $(docker images --filter dangling=true -q --no-trunc)')

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
