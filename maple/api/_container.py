"""Python API for maple"""

import os
import random

from .  import Environment
from .. import backend

class Container(Environment):
    """
    Class to manage containers
    """
    def __init__(self,**attributes):
        """
        Parameters
        ----------
        attributes : dictionary
                     { 'name'      : container name,
                       'source'    : source directory,
                       'target'    : target directory,
        """ 

        default_attributes = {  'name'      : 'ubuntu',
                                'source'    : None,
                                'target'    : None } 

        super().__init__(default_attributes,attributes)

        # Condition to check if target and source directories are defined in the Maplefile
        # assign default if they are not, and deal with execptions
        if not self._target: self._target = '/home/mount'
        if not self._source: self._source = os.getenv('PWD')

        # Set container name for environment variables
        self._container = self._name

    @property
    def name(self):
        return self._name

    def run(self,image,command,commit=False):
        """
        Run a container and commit to image
        """
        self._backend=image.backend
        self.setvars()
        backend.dict[self._backend].container.run(image.name,command,commit)
