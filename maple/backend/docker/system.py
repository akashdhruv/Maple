"""Python API for docker interface in maple"""

import os
import subprocess


def login():
    """
    Login to docker account
    """
    subprocess.run("docker login", shell=True)


def prune():
    """
    Prune system
    """
    subprocess.run("rm -f -v $maple_home/context/Dockerfile*", shell=True)
    subprocess.run("docker system prune -a", shell=True)
