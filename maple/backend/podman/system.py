"""Python API for podman interface in maple"""

import subprocess


def login():
    """
    Login to podman account
    """
    subprocess.run("podman login docker.io", shell=True, check=True)


def prune():
    """
    Prune system
    """
    subprocess.run("rm -f -v $maple_home/context/Dockerfile*", shell=True, check=True)
    subprocess.run("podman system prune -a", shell=True, check=True)
