"""Python CLI for maple"""

import click
import os

# CLI group
#
@click.group(name='maple')
def maple():
    """
    Simple CLI for using docker/singularity containers for HPC applications
    """
    # Check if required environment variables are defined in the Maplefile
    # If not then assign default values

    # VARIABLE                                             DESCRIPTION
    # ----------------------------------------------------------------
    # maple_user                Name of the user - usually current user
    # maple_group               Name of the users group
    # maple_image               Name of the image in remote registry    
    # maple_container           Name of the local container
    # maple_target              Name of the target dir to mount source dir
    # maple_source              Name of the source dir - usually $PWD
    # maple_port                Port ID for the container (used when running jupyter notebooks)
    # maple_docker              Container backend (docker/singularity)

    if not os.getenv('maple_backend'): os.environ['maple_backend'] = 'docker'
    if not os.getenv('maple_user'): os.environ['maple_user'] = os.popen('id -u').read().split()[0]
    if not os.getenv('maple_group'): os.environ['maple_group'] = os.popen('id -g').read().split()[0]
    if not os.getenv('maple_port'): os.environ['maple_port'] = '8888'

    # Condition to check if target and source directories are defined in the Maplefile
    # assign default if they are not, and deal with execptions
    if not os.getenv('maple_target'):
        os.environ['maple_target'] = '/home'
        if os.getenv('maple_source'): del os.environ['maple_source']
    else:
        if not os.getenv('maple_source'): os.environ['maple_source'] = os.getenv('PWD')
