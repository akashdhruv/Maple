"""Python API for maple"""

import os
import random

from . import docker,singularity

class Maple(object):
    """
    User interface to maple
    """
    dict_backend = {'docker' : docker, 'singularity': singularity}

    def __init__(self,**attributes):
        """
        Parameters
        ----------
        attributes : dictionary
                     { 'container' : container name,
                       'image'     : remote image name,
                       'source'    : source directory,
                       'target'    : target directory,
                       'user'      : local user,
                       'group'     : user's group,
                       'backend'   : container backend - docker/singularity
                       'port'      : port ID to deploy jupyter notebooks}
        """

        self._set_attributes(attributes)
           
    def __getitem__(self,key):
        """
        Get variable data
        """
        if not key in self._attributes: 
            raise ValueError('[maple]: attribute "{}" not present'.format(key))
        else:
            return self._attributes[key]

    def __setitem__(self,key,value):
        """
        Set variable data
        """
        if not key in self._attributes:
            raise ValueError('[maple]: attribute "{}" not present'.format(key))
        elif key=='backend' or key=='port':
            raise NotImplementedError('[maple]: cannot edit "{0}" after intitialization'.format(key))
        else:
            self._attributes[key] = value

    def _set_env(self):
        """
        private method for initialization
        """
        for key, value in self._attributes.items():
            if(value): os.environ['maple_'+key] = str(value)

    def _set_attributes(self,attributes):
        """
        Private method for initialization
        """
        self._attributes = { 'container' : 'ubuntu', 'image':'ubuntu:latest', 
                             'source'    : None, 'target' : None, 
                             'user'      : os.popen('id -u').read().split()[0],
                             'group'     : os.popen('id -g').read().split()[0],
                             'backend'   : 'docker',
                             'port'      : str(random.randint(1111,9999)) }
 
        for key in attributes:
            if key in self._attributes:
                self._attributes[key] = attributes[key]
            else:
                raise ValueError('[maple]: attribute "{}" not present'.format(key))

        # Set backend docker/singularity
        self._attributes['backend'] = Maple.dict_backend[self._attributes['backend']]

        # Condition to check if target and source directories are defined in the Maplefile
        # assign default if they are not, and deal with execptions
        if not self._attributes['target']:
            self._attributes['target'] = '/home'
            self._attributes['source'] = None
        else:
            if not self._attributes['source']: self._attributes['source'] = os.getenv('PWD')
 
    def build(self):
        """
        Builds a local image from remote image
        """
        self._set_env()
        self._attributes['backend'].build()

    def commit(self):
        """
        Commit changes from local container to local image
        """
        self._set_env()
        self._attributes['backend'].commit()

    def pull(self):
        """
        Pull remote image
        """
        self._set_env()
        self._attributes['backend'].pull()

    def push(self,tag):
        """
        Push local image to remote tag/image
        """
        self._set_env()
        self._attributes['backend'].push(tag)

    def login(self):
        """
        Login to container backend (currently docker)
        """
        self._set_env()
        self._attributes['backend'].login()

    def run(self,command):
        """
        Run local image in a container
        """
        self._set_env()
        self._attributes['backend'].run(command)

    def pour(self):
        """
        Pour local image in a container, opposite of maple rinse
        """
        self._set_env()
        self._attributes['backend'].pour()

    def bash(self):
        """
        Get shell access to the local container
        """
        self._set_env()
        self._attributes['backend'].bash()

    def execute(self,command):
        """
        Execute command
        """
        self._set_env()
        self._attributes['backend'].execute(command)

    def notebook(self):
        """
        Launch ipython notebook inside the container
        """
        self._set_env()
        self._attributes['backend'].notebook()

    def rinse(self):
        """
        Stop and remove the local container, opposite of maple pour
        """
        self._set_env()
        self._attributes['backend'].rinse()

    def images(self):
        """
        List all images on system
        """
        self._set_env()
        self._attributes['backend'].images()

    def containers(self):
        """
        List all containers on system
        """
        self._set_env()
        self._attributes['backend'].containers()

    def squash(self):
        """
        Squash and prune layers
        """
        self._set_env()
        self._attributes['backend'].squash()

    def clean(self):
        """
        Clean local container envment
        """
        self._set_env()
        self._attributes['backend'].clean()

    def remove(self):
        """
        Remove a remote image
        """
        self._set_env()
        self._attributes['backend'].remove()

    def prune(self):
        """
        Prune system
        """
        self._set_env()
        self._attributes['backend'].prune()
