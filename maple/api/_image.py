"""Python API for maple"""

import os

from .  import Maple
from .. import backend

class Image(Maple):
    """
    Class to manage images
    """
    def __init__(self,**attributes):
        """
        Parameters
        ----------
        attributes : dictionary
                     { 'base'      : remote image name,
                       'name'      : name of the image,
                       'backend'   : container backend - docker/singularity

        """
        default_attributes = { 'name'      : 'ubuntu',
                               'base'      : 'ubuntu:latest',
                               'backend'   : 'docker' }
 
        super().__init__(default_attributes,attributes)

        # Set values for user and group
        self._user  = os.popen('id -u').read().split()[0]
        self._group = os.popen('id -g').read().split()[0]

    @property
    def name(self):
        return self._name

    @property
    def backend(self):
        return self._backend

    def build(self,base=None):
        """
        Builds a local image from base image
        """
        if base: self._base = base
        self.setenv()
        backend.dict[self._backend].image.build(self._name)

    def squash(self):
        """
        Squash an the image
        """
        self.setenv()
        backend.dict[self._backend].image.squash(self._name)

    def tag(self,target):
        """
        Tag an image
        """
        self.setenv()
        backend.dict[self._backend].image.tag(self._name,target)

    def delete(self):
        """
        Delete the image
        """
        self.setenv()
        backend.dict[self._backend].image.delete(self._name)
