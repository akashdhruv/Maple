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
    Setup a configuration file from user provided path
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
