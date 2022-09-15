"""Python API for singularity interface in maple"""

import subprocess


def login():
    """
    Login to container account
    """
    print("[MAPLE ERROR]: system login not available for singularity backend")
    raise NotImplementedError()


def prune():
    """
    Prune system
    """
    subprocess.run("singularity cache clean", shell=True, check=True)
