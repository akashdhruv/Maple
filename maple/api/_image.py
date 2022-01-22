"""Python API for maple"""

import os

from .  import Maple
from ..backend import Backend

class Image(Maple):
    """
    Class to manage images

    Parameters
    ----------
    **attributes  : dictionary of user attributes
                    { 'base'      : remote image name,
                      'name'      : name of the image,
                      'backend'   : container backend - docker/singularity

   """

    def __init__(self,**attributes):
        """
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

    def build(self):
        """
        Builds a local image from base image
        """
        self.setenv()
        Backend().image.build(self._name,self._base)

    def squash(self):
        """
        Squash an the image
        """
        self.setenv()
        Backend().image.squash(self._name)

    def tag(self,target):
        """
        Tag an image
 
        target: target image for tagging
        """
        self.setenv()
        Backend().image.tag(self._name,target)

    def delete(self):
        """
        Delete the image
        """
        self.setenv()
        Backend().image.delete(self._name)
