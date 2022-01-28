"""Python API for docker interface in maple"""

import os

def login():
    """
    Login to docker account
    """
    os.system('docker login')

def prune():
    """
    Prune system
    """
    os.system('rm -f -v $maple_home/context/Dockerfile*')
    os.system('docker system prune -a')
