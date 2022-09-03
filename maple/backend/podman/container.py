"""Python API for podman interface in maple"""

import os
import subprocess
import random


def commit():
    """
    Commit changes from local container to local image
    """
    subprocess.run(
        "podman commit $maple_container $maple_image", shell=True, check=True
    )


def pour(options=""):
    """
    Pour local image in a container, opposite of maple rinse

    Arguments
    ---------
    options : string of options
    """
    process = subprocess.run(
        f"podman run --entrypoint '/bin/bash' {options} -dit \
                     --platform $maple_platform --name $maple_container \
                     --mount type=bind,source=$maple_source,target=$maple_target \
                     localhost/$maple_image",
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
        subprocess.run("podman stop $(podman ps -aq)", shell=True, check=True)
        subprocess.run("podman rm $(podman ps -aq)", shell=True, check=True)
    else:
        subprocess.run("podman stop $maple_container", shell=True, check=True)
        subprocess.run("podman rm $maple_container", shell=True, check=True)


def shell():
    """
    Get shell access to the local container
    """
    subprocess.run(
        "podman exec -it --workdir $maple_target $maple_container bash",
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

    command = f'"{command}"'
    process = subprocess.run(
        f"podman run --entrypoint '/bin/bash' {options} \
                     --name $maple_container \
                     --mount type=bind,source=$maple_source,target=$maple_target \
                     --workdir $maple_target \
                     localhost/$maple_image -c {command}",
        shell=True,
        check=True,
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
    command = f'"{command}"'
    process = subprocess.run(
        f"podman exec --entrypoint '/bin/bash' --workdir $maple_target $maple_container -c {command}",
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

    pour(options=f"-p {port}:{port}")
    result = execute(f"jupyter notebook --port={port} --no-browser --ip=0.0.0.0")
    rinse()

    if result != 0:
        raise Exception("[maple] Error inside container")


def list():
    """
    List all containers on system
    """
    subprocess.run("podman container ls -a", shell=True, check=True)
