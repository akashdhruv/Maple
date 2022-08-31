"""Backend interface"""

import os

from . import docker
from . import singularity
from . import podman


def Backend():
    """
    Function to call backend based on 'maple_backend' environment variable

    Returns
    -------
    docker/singularity backend module

    """
    backend_dict = {"docker": docker, "singularity": singularity, "podman": podman}

    return backend_dict[os.getenv("maple_backend")]
