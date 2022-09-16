"""Python API for maple"""

import os
import pwd

from . import Maple
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

    def __init__(self, **attributes):
        """ """
        self._name = "ubuntu"
        self._base = "ubuntu:latest"
        self._backend = "docker"
        self._target = None
        self._source = None

        super().__init__(self.__dict__, attributes)

        # Condition to check if target and source directories are defined in the Maplefile
        # assign default if they are not, and deal with exceptions
        if not self._target:
            self._target = "/home/mount"
        if not self._source:
            self._source = os.getenv("PWD")

        # Set values for user and group
        self._uid = str(os.getuid())
        self._gid = str(os.getgid())
        self._user = pwd.getpwuid(os.getuid())[0]

        # Set container name for environment variables
        self._image = self._name

    @property
    def name(self):
        """
        Getter for image name
        """
        return self._name

    def build(self, command=None, options=""):
        """
        Builds a local image from base image
        """
        cmd_list = None
        if command:
            cmd_list = [command]

        self.setenv()
        Backend().image.build(options=options, cmd_list=cmd_list)

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
