"""Python CLI for maple"""

import click
import os

import pymaple

# CLI group
#
@click.group(name='maple')
def maple():
    """
    Simple CLI for using docker/singularity containers for HPC applications
    """
    if not os.getenv('maple_backend'): os.environ['maple_backend'] = 'docker'
    if not os.getenv('maple_user'): os.environ['maple_user'] = os.popen('id -u').read().split()[0]
    if not os.getenv('maple_group'): os.environ['maple_group'] = os.popen('id -g').read().split()[0]

# Build a container using the information supplied from Maplefile
# Currently this uses a docker build, but we intend this interface to be more general depending
# on the type of backend use for containerization
#
@maple.command(name='build')
@click.option('--image',default=os.getenv('maple_image'),help='overwrite current remote image')
def build(image):
    """
    Builds a local image from remote image
    """
    os.environ['maple_image'] = str(image)
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].build()

# Commit changes to a container
# Saves changes to local container as an image, currently uses docker
#
@maple.command(name='commit')
def commit():
    """
    Commit changes from local container to local image
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].commit()

# Pull image from remote registry
# Currently pulls maple_image for a remote registry
#
@maple.command(name='pull')
@click.option('--image',default=os.getenv('maple_image'),help='overwrite current remote image')
def pull(image):
    """
    Pull remote image
    """
    os.environ['maple_image'] = str(image)
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].pull()

# Push image to remote registry
# Tag and push changes to local container to remote registry
# Note will require 'maple login' if credentials are required
#
@maple.command(name='push')
@click.argument('tag')
def push(tag):
    """
    Push local image to remote tag/image
    """
    os.environ['maple_pushtag'] = str(tag)
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].push()

# Login to remote registry
#
@maple.command(name='login')
def login():
    """
    Login to container backend (currently docker)
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].login()

# Run an image in a local container
# This functionality executes the CMD statement in a Dockerfile.
# If maple_source or maple_target are present then they will be mounted inside the container. 
# This is useful for accessing simulation output/plotfiles
#
@maple.command('run')
@click.option('--nprocs',default=1,help='number of processes for maple container')
def run(nprocs):
    """
    Run local image in a container, opposite of maple rinse
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].run(nprocs)

# Pour an image in a local container to access interactive shell
# If maple_source or maple_traget are present then they will be mounted inside the containter.
# This is useful for mounting maple_source for development
#
@maple.command('pour')
def pour():
    """
    Pour local image in a container, opposite of maple rinse
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].pour()

# Enter the shell environment of a "poured" container
#
@maple.command('bash')
def bash():
    """
    Get shell access to the local container
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].bash()

# Rinse a local container
# Do this if the local container is not needed
#
@maple.command('rinse')
@click.option('--container',default=os.getenv('maple_container'),help='overwrite current container')
def rinse(container):
    """
    Remove the local container, opposite of maple run/pour
    """
    os.environ['maple_container'] = str(container)
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].rinse()

# List all images
#
@maple.command('images')
def images():
    """
    List all images on system
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].images()

# List all container
#
@maple.command('containers')
def containers():
    """
    List all containers on system
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].containers()

# Clean all local images and containers
#
@maple.command('clean')
@click.option('--container',default=os.getenv('maple_container'),help='overwrite current container')
def clean(container):
    """
    clean local container environment
    """
    os.environ['maple_container'] = str(container)
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].clean()

# Delete a remote image
#
@maple.command('remove')
@click.option('--image',default=os.getenv('maple_image'),help='overwrite current remote image')
def remove(image):
    """
    Remove a remote image
    """
    os.environ['maple_image']=str(image)
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].remove()

# Prune system
#
@maple.command('prune')
def prune():
    """
    Prune system
    """
    pymaple.Maple.dict_backend[os.getenv('maple_backend')].prune()

if __name__ == "__main__":
    maple()
