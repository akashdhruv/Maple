"""Python API for docker interface in maple"""

import os
import subprocess

from . import container


def build(as_root=False, cmd_list=[]):
    """
    Builds a local image from remote image

    Arguments
    ---------
    as_root    : Build image as root (True/False)
    cmd_list   : Command list for build
    """
    # Create a context directory
    subprocess.run(
        "mkdir -pv {0}".format(os.getenv("maple_home") + "/context"), shell=True
    )

    # Set Dockerfile for the build
    dockerfile_build = (
        os.getenv("maple_home") + "/context/Dockerfile." + os.getenv("maple_image")
    )

    # Select the base and user Dockerfile
    dockerfile_base = os.getenv("maple_dir") + "/resources/Dockerfile.base"

    if as_root:
        dockerfile_user = os.getenv("maple_dir") + "/resources/Dockerfile.root"
    else:
        dockerfile_user = os.getenv("maple_dir") + "/resources/Dockerfile.user"

    # Populate Dockerfile for the build
    subprocess.run(
        "cat {0} > {1}".format(dockerfile_base, dockerfile_build), shell=True
    )

    dockerfile = open("{0}".format(dockerfile_build), "a")  # append mode

    if cmd_list:
        for command in cmd_list:
            dockerfile.write("\nRUN {0}\n".format(command))

    dockerfile.close()

    subprocess.run(
        "cat {0} >> {1}".format(dockerfile_user, dockerfile_build), shell=True
    )

    # execute docker build
    subprocess.run(
        "docker build -t $maple_image --no-cache \
                                   --build-arg maple_base=$maple_base \
                                   --build-arg maple_user=$maple_user \
                                   --build-arg maple_uid=$maple_uid \
                                   --build-arg maple_gid=$maple_gid \
                                   --file={0} \
                                   $maple_home/context".format(
            dockerfile_build
        ),
        shell=True,
    )

    # subprocess.run('rm $maple_home/context/Dockerfile.build', shell=True)


def pull(target, base):
    """
    Pull remote image

    Arguments
    ---------
    target : target image to pull into
    base   : base image in remote registry
    """
    subprocess.run("docker pull {0}".format(base), shell=True)
    subprocess.run("docker tag {0} {1}".format(base, target), shell=True)


def push(base, target):
    """
    Push local image to remote tag/image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run("docker tag {0} {1}".format(base, target), shell=True)
    subprocess.run("docker push {0}".format(target), shell=True)


def tag(base, target):
    """
    Tag a target image from base image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run("docker tag {0} {1}".format(base, target), shell=True)


def list():
    """
    List all images on system
    """
    subprocess.run("docker images", shell=True)


def squash():
    """
    Squash an image and remove layers
    """
    os.environ["maple_container"] = os.environ["maple_image"] + "_container"

    container.pour()
    subprocess.run("docker export $maple_container > $maple_image.tar", shell=True)
    subprocess.run("cat $maple_image.tar | docker import - $maple_image", shell=True)
    subprocess.run("rm $maple_image.tar", shell=True)
    container.rinse()


def scan(image):
    """
    Scan an image

    Arguments
    ---------
    image : image name

    """
    subprocess.run("docker scan {0}".format(image), shell=True)


def delete():
    """
    Delete an image
    """
    subprocess.run(
        "docker rmi $maple_image $(docker images --filter dangling=true -q --no-trunc)",
        shell=True,
    )
