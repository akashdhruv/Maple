"""Python API for singularity interface in maple"""

import os
import random
import subprocess


def commit():
    """
    Commit changes from local container to local image
    """
    print("[MAPLE ERROR]: container commit not available for singularity backend")
    raise NotImplementedError()


def pour(options="--no-home"):
    """
    Pour local image in a container, opposite of maple rinse

    Arguments
    ---------
    options : string of options
    """
    if os.getenv("maple_mpi"):
        options = options + "--bind $maple_mpi:$maple_mpi"

    process = subprocess.run(
        f"singularity instance start {options} --bind $maple_source:$maple_target \
                                              $maple_home/images/$maple_image.sif \
                                              $maple_container",
        shell=True,
        check=True,
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
        subprocess.run("singularity instance stop --all", shell=True, check=True)
    else:
        subprocess.run(
            "singularity instance stop $maple_container", shell=True, check=True
        )


def shell():
    """
    Get shell access to the local container
    """
    subprocess.run(
        "singularity shell --pwd $maple_target instance://$maple_container",
        shell=True,
        check=True,
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

    if os.getenv("maple_mpi"):
        options = options + "--bind $maple_mpi:$maple_mpi"

    command = f'"{command}"'
    process = subprocess.run(
        f"singularity exec {options} --no-home --bind $maple_source:$maple_target \
                                              --pwd  $maple_target \
                               $maple_home/images/$maple_image.sif bash -c {command}",
        shell=True,
        check=True,
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
    command = f'"{command}"'
    process = subprocess.run(
        f"singularity exec --pwd $maple_target \
                          instance://$maple_container bash -c {command}",
        shell=True,
        check=True,
    )

    return process.returncode


def publish(cmd_list=None):
    """
    Publish container to an image

    Arguments
    ---------
    cmd_list: list of commands to publish
    """
    print("[MAPLE ERROR]: container publish not available for singularity backend")
    raise NotImplementedError()


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
        f"jupyter notebook --port={port} --no-browser --ip=0.0.0.0 --allow-root"
    )
    rinse()

    if result != 0:
        raise Exception("[maple] Error inside container")


def list():
    """
    List all containers on system
    """
    subprocess.run("singularity instance list", shell=True, check=True)
