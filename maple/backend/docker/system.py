"""Python API for docker interface in maple"""

import subprocess


def login():
    """
    Login to docker account
    """
    subprocess.run("docker login", shell=True, check=True)


def prune():
    """
    Prune system
    """
    subprocess.run("rm -f -v $maple_home/context/Dockerfile*", shell=True, check=True)
    subprocess.run("docker system prune -a", shell=True, check=True)
