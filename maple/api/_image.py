"""Python API for maple"""

import os
import pwd

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
        self._uid = str(os.getuid())
        self._gid = str(os.getgid())
        self._user = pwd.getpwuid(os.getuid())[0]

        # Set container name for environment variables
        self._image = self._name

    @property
    def name(self):
        return self._name

    def build(self):
        """
        Builds a local image from base image
        """
        self.setenv()
        Backend().image.build()

    def squash(self):
        """
        Squash an the image
        """
        self.setenv()
        Backend().image.squash()

    def delete(self):
        """
        Delete the image
        """
        self.setenv()
        Backend().image.delete()
