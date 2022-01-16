"""Python API for maple"""

import os
import random

from ..backend import docker,singularity

class MapleEnv(object):
    """
    Base class for defining maple environment
    """
    backend = {'docker':docker, 'singularity':singularity}

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
        super().__init__()
        self._set_attributes(attributes)
           
    def __getitem__(self,key):
        """
        Get variable data
        """
        if not key in self.__dict__.keys(): 
            raise ValueError('[maple]: attribute "{}" not present'.format(key))
        else:
            return getattr(self,key)

    def __setitem__(self,key,value):
        """
        Set variable data
        """
        if not key in self.__dict__.keys():
            raise ValueError('[maple]: attribute "{}" not present'.format(key))
        elif key=='backend' or key=='port':
            raise NotImplementedError('[maple]: cannot edit "{0}" after intitialization'.format(key))
        else:
            setattr(self,key,value)

    def set_vars(self):
        """
        Set environment variables
        """
        for key, value in self.__dict__.items():
            if(value): os.environ['maple_'+key] = str(value)

    def _set_attributes(self,attributes):
        """
        Private method for initialization
        """
        _default_attributes = { 'container' : 'ubuntu', 'image':'ubuntu:latest', 
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

        for key, value in _default_attributes.items(): setattr(self,key,value)

        # Set backend docker/singularity
        self.backend = MapleEnv.backend[self.backend]

        # Condition to check if target and source directories are defined in the Maplefile
        # assign default if they are not, and deal with execptions
        if not self.target:
            self.target = '/home'
            self.source = None
        else:
            if not self.source: self.source = os.getenv('PWD')
