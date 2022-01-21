"""Backend interface"""

import os

from . import docker
from . import singularity

def Backend():
    """
    Function to call backend based on 'maple_backend' environment variable 
    """
    backend_dict = { 'docker'      : docker,
                     'singularity' : singularity}

    return backend_dict[os.getenv('maple_backend')]
