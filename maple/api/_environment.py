"""Python API for maple"""

import os
import random

class Environment(object):
    """
    Base class for defining maple environment
    """
    def __init__(self,**attributes):
        """
        Parameters
        ----------
        attributes : dictionary
                     { 'container' : container name,
                       'base'      : remote image name,
                       'source'    : source directory,
                       'target'    : target directory,
                       'user'      : local user,
                       'group'     : user's group,
                       'backend'   : container backend - docker/singularity
                       'port'      : port ID to deploy jupyter notebooks}
        """
        super().__init__()
        self._set_attributes(attributes)
 
    @property
    def backend(self):
        return self._backend

    @property
    def port(self):
        return self._port

    def setvars(self):
        """
        Set environment variables
        """
        for key, value in self.__dict__.items():
            if(value): os.environ['maple'+key] = str(value)

    def _set_attributes(self,attributes):
        """
        Private method for initialization
        """
        _default_attributes = { 'container' : 'ubuntu', 'base':'ubuntu:latest', 
                                'source'    : None, 'target' : None, 
                                'user'      : os.popen('id -u').read().split()[0],
                                'group'     : os.popen('id -g').read().split()[0],
                                'backend'   : 'docker',
                                'port'      : str(random.randint(1111,9999)) }
 
        for key in attributes:
            if key in _default_attributes:
                _default_attributes[key] = attributes[key]
            else:
                raise ValueError('[maple]: attribute "{}" not present'.format(key))

        for key, value in _default_attributes.items(): setattr(self,'_'+key,value)

        # Condition to check if target and source directories are defined in the Maplefile
        # assign default if they are not, and deal with execptions
        if not self._target: self._target = '/home/mount'
        if not self._source: self._source = os.getenv('PWD')
