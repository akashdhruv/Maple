"""Python CLI for maple"""

import click
import toml
import os

# CLI group
#
@click.group(name='maple')
@click.option('--docker',  is_flag=True, help='option for docker backend (default) ')
@click.option('--singularity',  is_flag=True, help='option for singularity backend')
def maple(docker,singularity):
    """
    CLI for using docker/singularity containers for HPC applications
    """
    # Check if required environment variables are defined in the Maplefile
    # If not then assign default values

    # VARIABLE                                             DESCRIPTION
    # ----------------------------------------------------------------
    # base                Name of the base image to build container
    # user                Name of the user - usually current user
    # group               Name of the users group
    # target              Name of the target dir to mount source dir
    # source              Name of the source dir - usually $PWD
    # backend             Container backend (docker/singularity)

    Maplefile = os.path.exists('Maplefile')

    if Maplefile:
        for key,value in toml.load('Maplefile').items():
            os.environ['maple_'+key] = str(value)

    if not os.getenv('maple_backend'): os.environ['maple_backend'] = 'docker'
    if not os.getenv('maple_user'): os.environ['maple_user'] = os.popen('id -u').read().split()[0]
    if not os.getenv('maple_group'): os.environ['maple_group'] = os.popen('id -g').read().split()[0]

    # Condition to check if target and source directories are defined in the Maplefile
    # assign default if they are not, and deal with execptions
    if not os.getenv('maple_target'): os.environ['maple_target'] = '/home/mount'
    if not os.getenv('maple_source'): os.environ['maple_source'] = os.getenv('PWD')

    if docker: os.environ['maple_backend'] = 'docker'
    if singularity: os.environ['maple_backend'] = 'singularity'
