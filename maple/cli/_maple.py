"""
Command Line Interface (CLI) for Maple. Reads Maplefile
and sets environment variables
"""

import os
import pwd
import click
import toml

# CLI group
#
@click.group(name="maple")
@click.option("--docker", is_flag=True, help="option for docker backend (default) ")
@click.option("--singularity", is_flag=True, help="option for singularity backend")
@click.option("--podman", is_flag=True, help="option for podman backend")
def maple(docker, singularity, podman):
    """
    CLI for using docker/singularity/podman containers for HPC applications
    """
    # Check if required environment variables are defined in the Maplefile
    # If not then assign default values

    os.environ["maple_uid"] = str(os.getuid())
    os.environ["maple_gid"] = str(os.getgid())
    os.environ["maple_user"] = pwd.getpwuid(os.getuid())[0]

    Maplefile = os.path.exists("Maplefile")

    if Maplefile:
        for key, value in toml.load("Maplefile").items():
            if key not in ["build", "publish", "environ"]:
                os.environ["maple_" + key] = str(value)

    if not os.getenv("maple_image"):
        os.environ["maple_image"] = str(os.getenv("maple_container"))

    if not os.getenv("maple_backend"):
        os.environ["maple_backend"] = "docker"

    if docker:
        os.environ["maple_backend"] = "docker"
    if singularity:
        os.environ["maple_backend"] = "singularity"
    if podman:
        os.environ["maple_backend"] = "podman"

    # Condition to check if target and source directories are defined in the Maplefile
    # assign default if they are not, and deal with execptions
    if not os.getenv("maple_target"):
        os.environ["maple_target"] = "/home/mount"
    if not os.getenv("maple_source"):
        os.environ["maple_source"] = os.getenv("PWD")
