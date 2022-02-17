"""Python API for singularity interface in maple"""

import os


def build(as_root=False, cmd_list=[]):
    """
    Builds a local image from remote image

    Arguments
    ---------
    as_root    : Build image as root (True/False)
    cmd_list   : List of build commands
    """
    # Create image directory
    os.system("mkdir -pv {0}".format(os.getenv("maple_home") + "/images"))

    # Build image
    os.system("singularity build $maple_image.sif $maple_base")
    os.system("mv $maple_image.sif $maple_home/images/$maple_image.sif")


def pull(target, base):
    """
    Pull remote image

    Arguments
    ---------
    target : target image to pull into
    base   : base image in remote registry
    """
    os.system("singularity pull $maple_home/images/{0}.sif {1}".format(target, base))


def push(base, target):
    """
    Push local image to remote tag/image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    os.system("singularity pull $maple_home/images/{0}.sif {1}".format(base, target))


def tag(base, target):
    """
    Tag a target image from base image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    os.system(
        "cp $maple_home/images/{0}.sif $maple_home/images/{1}.sif".format(base, target)
    )


def list():
    """
    List all images on system
    """
    os.system("ls $maple_home/images/*.sif 2> /dev/null")


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
    os.system("rm -f -v $maple_home/images/$maple_image.sif")
