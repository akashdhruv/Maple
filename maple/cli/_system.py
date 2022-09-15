"""
Command Line Interface (CLI) for system configuration management.
"""
import os
import subprocess
import click

from ..backend import Backend
from . import maple


# Setup environment
#
@maple.command(name="config")
@click.argument("maplefile")
def config(maplefile):
    """
    Setup a TOML configuration file from user provided path

    \b
    List of TOML variables
    =========================================================
    \b
    base      : Name of the base image either local or remote.
                Include proper prefix when using images from 
                different registries
                \b
                base = "ubuntu:latest"
    \b
    platform  : Hardware platform (amd64, ppc64le, etc.). 
                Default is amd64 
                \b
                platform = "linux/ppc64le"
    \b
    container : Name of the local container
                \b
                container = "local_container"
    \b
    image     : Name of the local image.
                Default is taken from 'container' name
                \b
                image = "local_image"
    \b
    source    : Source directory to mount inside container.
                Default is $PWD
                \b
                source = "/path/to/source"
    \b
    target    : Name of the target directory inside container
                to mount 'source'. Default is '/home/mount'
                \b
                target = "/path/to/target"
    \b
    mpi       : Path to host MPI directory. If this is not
                defined, MPI installed inside the container 
                will be used
                \b
                mpi = "/path/to/mpi"
    \b
    environ   : A list of enivronment varibles to be defined
                inside the container.
                \b 
                environ = ["VAR1=<definition>","VAR2=<definition>"]                
    \b
    build     : A list of commands to be executed during build
                \b
                build = ["echo Add a list of build commands"]
    \b
    publish   : A list of commands to be executed to update
                an image invoked during 'maple container publish'
                \b
                publish = ["echo Add a list of publish commands"]
    \b
    backend   : Backend. Default is docker
                \b
                backend = "docker"
    """
    if maplefile == "Maplefile":
        print("Cannot link a file to itself. Operation not permitted. ABORTING")
        raise ValueError()

    if os.path.exists("Maplefile"):
        print(f"Maplefile already exists in current directory")
        overwrite = input("Overwrite? Y/n ")

        if overwrite == "y" or overwrite == "Y":
            print("OVERWRITING")
            subprocess.run(
                f"rm Maplefile && ln -s {maplefile} Maplefile", shell=True, check=True
            )
        else:
            print("SKIPPING")
    else:
        subprocess.run(f"ln -s {maplefile} Maplefile", shell=True, check=True)


# Login to remote registry
#
@maple.command(name="login")
def login():
    """
    Login to container backend
    """
    Backend().system.login()


# Prune system
#
@maple.command("prune")
def prune():
    """
    Clear backend cache
    """
    Backend().system.prune()
