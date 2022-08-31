"""Python API for podman interface in maple"""

import os
import subprocess

from . import container


def build(as_root=False, cmd_list=None):
    """
    Builds a local image from remote image

    Arguments
    ---------
    as_root    : Build image as root (True/False)
    cmd_list   : Command list for build
    """
    # Create a context directory
    subprocess.run(
        f'mkdir -pv {os.getenv("maple_home")}/context', shell=True, check=True
    )

    # Set Dockerfile for the build
    podmanfile_build = (
        os.getenv("maple_home") + "/context/Dockerfile." + os.getenv("maple_image")
    )

    # Select the base and user Dockerfile
    podmanfile_base = os.getenv("maple_dir") + "/resources/Dockerfile.base"

    # Populate Dockerfile for the build
    subprocess.run(
        f"cat {podmanfile_base} > {podmanfile_build}", shell=True, check=True
    )

    with open(f"{podmanfile_build}", "a") as podmanfile:  # append mode
        if cmd_list:
            for command in cmd_list:
                podmanfile.write(f"\nRUN {command}\n")

    # execute podman build
    subprocess.run(
        f"podman build -t $maple_image --no-cache \
                                   --build-arg maple_base=$maple_base \
                                   --build-arg maple_user=$maple_user \
                                   --build-arg maple_uid=$maple_uid \
                                   --build-arg maple_gid=$maple_gid \
                                   --file={podmanfile_build} \
                                   $maple_home/context",
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
    subprocess.run(f"podman pull {base}", shell=True, check=True)
    subprocess.run(f"podman tag {base} {target}", shell=True, check=True)


def push(base, target):
    """
    Push local image to remote tag/image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run(f"podman tag {base} {target}", shell=True, check=True)
    subprocess.run(f"podman push {target}", shell=True, check=True)


def tag(base, target):
    """
    Tag a target image from base image

    Arguments
    ---------
    base   : base image
    target : target image to push
    """
    subprocess.run(f"podman tag {base} {target}", shell=True, check=True)


def list():
    """
    List all images on system
    """
    subprocess.run("podman images", shell=True, check=True)


def squash():
    """
    Squash an image and remove layers
    """
    os.environ["maple_container"] = os.environ["maple_image"] + "_container"

    container.pour()
    subprocess.run(
        "podman export $maple_container > $maple_image.tar", shell=True, check=True
    )
    subprocess.run(
        "cat $maple_image.tar | podman import - $maple_image", shell=True, check=True
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
    print("[maple.image.scan] not available for podman backend")


def delete():
    """
    Delete an image
    """
    subprocess.run(
        "podman rmi $maple_image $(podman images --filter dangling=true -q --no-trunc)",
        shell=True,
        check=True,
    )