"""Python API for maple"""

import os

from . import docker

class Maple(object):
    """
    User interface to maple
    """
    dict_backend = {'docker' : docker}

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
                       'parfile'   : parfile }
        """

        self._attributes = { 'container' : 'ubuntu_container', 'image':'ubuntu:latest', 
                             'source'    : None, 'target' : None, 
                             'user'      : os.popen('id -u').read().split()[0],
                             'group'     : os.popen('id -g').read().split()[0],
                             'backend'   : 'docker',
                             'parfile'   : None}
 
        for key in attributes:
            if key in self._attributes:
                self._attributes[key] = attributes[key]
            else:
                raise ValueError('[maple]: attribute "{}" not present'.format(key))

        self._attributes['backend'] = Maple.dict_backend[self._attributes['backend']]

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
        elif key == 'backend':
            raise NotImplementedError('[maple]: cannot edit "backend" after intitialization')
        else:
            self._attributes[key] = value

    def _set_environ(self):
        """
        private method for initialization
        """
        for key, value in self._attributes.items():
            if(value): os.environ['maple_'+key] = str(value)

    def build(self):
        """
        Builds a local image from remote image
        """
        self._set_environ()
        self._attributes['backend'].build()

    def commit(self):
        """
        Commit changes from local container to local image
        """
        self._set_environ()
        self._attributes['backend'].commit()

    def pull(self):
        """
        Pull remote image
        """
        self._set_environ()
        self._attributes['backend'].pull()

    def push(self,tag):
        """
        Push local image to remote tag/image
        """
        self._set_environ()
        os.environ['maple_pushtag']=str(tag)
        self._attributes['backend'].push()

    def login(self):
        """
        Login to container backend (currently docker)
        """
        self._set_environ()
        self._attributes['backend'].login()

    def run(self,nprocs=1):
        """
        Run local image in a container
        """
        self._set_environ()
        self._attributes['backend'].run(nprocs)

    def pour(self):
        """
        Pour local image in a container, opposite of maple rinse
        """
        self._set_environ()
        self._attributes['backend'].pour()

    def bash(self):
        """
        Get shell access to the local container
        """
        self._set_environ()
        self._attributes['backend'].bash()

    def rinse(self):
        """
        Stop and remove the local container, opposite of maple pour
        """
        self._set_environ()
        self._attributes['backend'].rinse()

    def images(self):
        """
        List all images on system
        """
        self._set_environ()
        self._attributes['backend'].images()

    def containers(self):
        """
        List all containers on system
        """
        self._set_environ()
        self._attributes['backend'].containers()

    def clean(self):
        """
        Clean local container environment
        """
        self._set_environ()
        self._attributes['backend'].clean()

    def remove(self):
        """
        Remove a remote image
        """
        self._set_environ()
        self._attributes['backend'].remove()

    def prune(self):
        """
        Prune system
        """
        self._set_environ()
        self._attributes['backend'].prune()
