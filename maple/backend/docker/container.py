"""Python API for docker interface in maple"""

import os
import toml
import random
import subprocess


def commit():
    """
    Commit changes from local container to local image
    """
    subprocess.run("docker commit $maple_container $maple_image", shell=True)


def pour(options=""):
    """
    Pour local image in a container, opposite of maple rinse

    Arguments
    ---------
    options : string of options
    """
    process = subprocess.run(
        "docker run {0} -dit --name $maple_container \
                             --mount type=bind,source=$maple_source,target=$maple_target \
                            $maple_image bash".format(
            options
        ),
        shell=True,
    )

    if process.returncode != 0:
        raise Exception("[maple] Error inside container")


def rinse(rinse_all=False):
    """
    Stop and remove the local container, opposite of maple pour

    Arguments
    ---------
    rinse_all : (True/False) flag to rinse all container
    """
    if rinse_all:
        subprocess.run("docker stop $(docker ps -aq)", shell=True)
        subprocess.run("docker rm $(docker ps -aq)", shell=True)
    else:
        subprocess.run("docker stop $maple_container", shell=True)
        subprocess.run("docker rm $maple_container", shell=True)


def shell():
    """
    Get shell access to the local container
    """
    subprocess.run(
        "docker exec -it --workdir $maple_target $maple_container bash", shell=True
    )


def run(command, options=""):
    """
    Run and rinse the local container

    Arguments
    ---------
    command : command string
    options : run options
    """
    os.environ["maple_container"] = (
        os.getenv("maple_container") + "_" + str(random.randint(1111, 9999))
    )

    command = '"{0}"'.format(command)
    process = subprocess.run(
        "docker run {0} --name $maple_container \
                                       --mount type=bind,source=$maple_source,target=$maple_target \
                                       --workdir $maple_target \
                                       $maple_image bash -c {1}".format(
            options, str(command)
        ),
        shell=True,
    )

    rinse()

    if process.returncode != 0:
        raise Exception("[maple] Error inside container")


def execute(command):
    """
    Run local image in a container

    Arguments
    ---------
    command: string of command to execute
    """
    command = '"{0}"'.format(command)
    process = subprocess.run(
        "docker exec --workdir $maple_target $maple_container bash -c {0}".format(
            str(command)
        ),
        shell=True,
    )

    return process.returncode


def publish(cmd_list=[]):
    """
    Publish container to an image

    Arguments
    ---------
    cmd_list: list of commands to publish
    """
    pour()

    result_list = []

    if cmd_list:
        for command in cmd_list:
            result_list.append(execute(command))

    commit()
    rinse()

    if not all(result == 0 for result in result_list):
        raise Exception("[maple] Error inside container")


def notebook(port="4321"):
    """
    Launch ipython notebook inside the container

    Arguments
    ---------
    image : image name
    port  : port id ('4321')

    """
    os.environ["maple_container"] = (
        os.getenv("maple_container") + "_" + str(random.randint(1111, 9999))
    )

    pour(options="-p {0}:{0}".format(port))
    result = execute(
        "jupyter notebook --port={0} --no-browser --ip=0.0.0.0".format(port)
    )
    rinse()

    if result != 0:
        raise Exception("[maple] Error inside container")


def list():
    """
    List all containers on system
    """
    subprocess.run("docker container ls -a", shell=True)
