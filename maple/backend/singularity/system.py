"""Python API for singularity interface in maple"""

import os


def login():
    """
    Login to container account
    """
    print("[maple.system.login] command not available for singularity backend")


def prune():
    """
    Prune system
    """
    os.system("singularity cache clean")
