"""Python API for singularity interface in maple"""

import os
import subprocess


def login():
    """
    Login to container account
    """
    print("[maple.system.login] command not available for singularity backend")


def prune():
    """
    Prune system
    """
    subprocess.run("singularity cache clean", shell=True)
