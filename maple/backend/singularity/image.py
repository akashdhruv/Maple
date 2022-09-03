"""Python API for singularity interface in maple"""

import os
import subprocess


def build(as_root=False, cmd_list=None, env_list=None, options=""):
    """
    Builds a local image from remote image

    Arguments
    ---------
    as_root    : Build image as root (True/False)
    cmd_list   : List of build commands
    env_list   : List of persistent environment variables
    """
    if as_root:
        print("Rootless mode only with singularity backend. ABORTING")
        raise ValueError()

    # Create image directory
    subprocess.run(
        f'mkdir -pv {os.getenv("maple_home")}/images', shell=True, check=True
    )

    # Build image
    subprocess.run(
        "singularity build --sandbox $maple_image.sif $maple_base", shell=True, check=True
    )
    subprocess.run(
        "mv $maple_image.sif $maple_home/images/$maple_image.sif",
        shell=True,
        check=True,
    )


def pull(target, base):
    """
    Pull remote image

    Arguments
    ---------
    target : target image to pull into
    base   : base image in remote registry
    """
    subprocess.run(
        f"singularity pull $maple_home/images/{target}.sif {base}",
        shell=True,
        check=True,
    )


def push(base, target):
    """
    Push local image to remote tag/image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run(
        f"singularity pull $maple_home/images/{base}.sif {target}",
        shell=True,
        check=True,
    )


def tag(base, target):
    """
    Tag a target image from base image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run(
        f"cp $maple_home/images/{base}.sif $maple_home/images/{target}.sif",
        shell=True,
        check=True,
    )


def list():
    """
    List all images on system
    """
    subprocess.run("ls $maple_home/images/*.sif 2> /dev/null", shell=True, check=True)


def squash():
    """
    Squash an image and remove layers
    """
    print("[maple.image.squash] not available for singularity backend")


def scan(image):
    """
    Scan an image

    Arguments
    ---------
    image : image name
    """
    print("[maple.image.scan] not available for singularity backend")


def delete():
    """
    Delete an image
    """
    subprocess.run(
        "rm -f -v $maple_home/images/$maple_image.sif", shell=True, check=True
    )
