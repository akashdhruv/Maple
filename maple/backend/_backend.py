"""Backend interface"""

import os

import maple.backend.docker as docker
import maple.backend.singularity as singularity
import maple.backend.podman as podman


def Backend():
    """
    Function to call backend based on 'maple_backend' environment variable

    Returns
    -------
    docker/singularity backend module

    """
    backend_dict = {"docker": docker, "singularity": singularity, "podman": podman}

    return backend_dict[os.getenv("maple_backend")]
