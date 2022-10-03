"""Python API for docker interface in maple"""

import os
import subprocess

from . import container


def build(as_root=False, options="", cmd_list=None, env_list=None, create_tar=False):
    """
    Builds a local image from remote image

    Arguments
    ---------
    as_root    : Build image as root (True/False)
    cmd_list   : Command list for build
    env_list   : List of persistent environment variables
    """
    # Create a context directory
    subprocess.run(
        f'mkdir -pv {os.getenv("maple_home")}/context', shell=True, check=True
    )

    # Set Dockerfile for the build
    dockerfile_build = (
        os.getenv("maple_home") + "/context/Dockerfile." + os.getenv("maple_image")
    )

    # Select the base and user Dockerfile
    dockerfile_base = os.getenv("maple_dir") + "/resources/Dockerfile.base"
    dockerfile_mpi = os.getenv("maple_dir") + "/resources/Dockerfile.mpi"

    if as_root:
        dockerfile_user = os.getenv("maple_dir") + "/resources/Dockerfile.root"
    else:
        dockerfile_user = os.getenv("maple_dir") + "/resources/Dockerfile.user"

    # Populate Dockerfile for the build
    subprocess.run(
        f"cat {dockerfile_base} > {dockerfile_build}", shell=True, check=True
    )

    if os.getenv("maple_mpi"):
        options = options + " --build-arg maple_mpi=$maple_mpi"
        subprocess.run(
            f"cat {dockerfile_mpi} >> {dockerfile_build}", shell=True, check=True
        )

    if os.getenv("maple_platform"):
        options = options + " --platform $maple_platform"
        print(f"Building on platform: {str(os.getenv('maple_platform'))}")

    with open(f"{dockerfile_build}", "a") as dockerfile:  # append mode
        if env_list:
            for variable in env_list:
                dockerfile.write(f"\nENV {variable}\n")
        if cmd_list:
            for command in cmd_list:
                dockerfile.write(f"\nRUN {command}\n")

    subprocess.run(
        f"cat {dockerfile_user} >> {dockerfile_build}", shell=True, check=True
    )

    print(
        "[MAPLE WARNING]: source cannot be mounted inside container target during docker build"
    )

    # execute docker build
    subprocess.run(
        f"docker build {options} -t $maple_image --no-cache \
                                 --build-arg maple_base=$maple_base \
                                 --build-arg maple_user=$maple_user \
                                 --build-arg maple_uid=$maple_uid \
                                 --build-arg maple_gid=$maple_gid \
                                 --file={dockerfile_build} \
                                 $maple_home/context",
        shell=True,
        check=True,
    )

    if create_tar:
        subprocess.run(
            "docker save -o $maple_image.tar $maple_image",
            shell=True,
            check=True,
        )

    # subprocess.run('rm $maple_home/context/Dockerfile.build', shell=True, check=True)


def pull(target, base):
    """
    Pull remote image

    Arguments
    ---------
    target : target image to pull into
    base   : base image in remote registry
    """
    subprocess.run(f"docker pull {base}", shell=True, check=True)
    subprocess.run(f"docker tag {base} {target}", shell=True, check=True)


def push(base, target):
    """
    Push local image to remote tag/image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run(f"docker tag {base} {target}", shell=True, check=True)
    subprocess.run(f"docker push {target}", shell=True, check=True)


def tag(base, target):
    """
    Tag a target image from base image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run(f"docker tag {base} {target}", shell=True, check=True)


def list():
    """
    List all images on system
    """
    subprocess.run("docker images", shell=True, check=True)


def squash():
    """
    Squash an image and remove layers
    """
    os.environ["maple_container"] = os.environ["maple_image"] + "_container"

    container.pour()
    subprocess.run(
        "docker export $maple_container > $maple_image.tar", shell=True, check=True
    )
    subprocess.run(
        "cat $maple_image.tar | docker import - $maple_image", shell=True, check=True
    )
    subprocess.run("rm $maple_image.tar", shell=True, check=True)
    container.rinse()


def scan(image):
    """
    Scan an image

    Arguments
    ---------
    image : image name

    """
    subprocess.run(f"docker scan {image}", shell=True, check=True)


def delete():
    """
    Delete an image
    """
    subprocess.run(
        "docker rmi $maple_image $(docker images --filter dangling=true -q --no-trunc)",
        shell=True,
        check=True,
    )
