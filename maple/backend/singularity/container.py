"""Python API for singularity interface in maple"""

import os
import random
import subprocess


def commit():
    """
    Commit changes from local container to local image
    """
    print("[maple.container.commit] not available for singularity backend")


def pour(options="--no-home"):
    """
    Pour local image in a container, opposite of maple rinse

    Arguments
    ---------
    options : string of options
    """
    process = subprocess.run(
        "singularity instance start {0} \
                                                   --bind $maple_source:$maple_target \
                                                   $maple_home/images/$maple_image.sif \
                                                   $maple_container".format(
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
        subprocess.run("singularity instance stop --all", shell=True)
    else:
        subprocess.run("singularity instance stop $maple_container", shell=True)


def shell():
    """
    Get shell access to the local container
    """
    subprocess.run(
        "singularity shell --pwd $maple_target instance://$maple_container", shell=True
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
        "singularity exec {0} --no-home \
                                             --bind $maple_source:$maple_target \
                                             --pwd  $maple_target \
                               $maple_home/images/$maple_image.sif bash -c {1}".format(
            options, str(command)
        ),
        shell=True,
    )

    if process.returncode != 0:
        raise Exception("[maple] Error inside container")


def execute(command):
    """
    Run local image in a container

    Arguments
    ---------
    command : command string
    """
    command = '"{0}"'.format(command)
    process = subprocess.run(
        "singularity exec --pwd $maple_target \
                                         instance://$maple_container bash -c {0}".format(
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
    print("[maple.container.publish] not available for singularity backend")


def notebook(port="4321"):
    """
    Launch ipython notebook inside the container

    Arguments
    ---------
    port  : port id ('4321')
    """
    os.environ["maple_container"] = (
        os.getenv("maple_container") + "_" + str(random.randint(1111, 9999))
    )

    pour(options="--cleanenv")
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
    subprocess.run("singularity instance list", shell=True)
