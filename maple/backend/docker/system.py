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
    os.system('docker system prune -a')
