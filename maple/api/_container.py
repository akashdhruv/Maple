"""Python API for maple"""

import os

from . import Maple
from ..backend import Backend


class Container(Maple):
    """
    Class to manage containers
    """

    def __init__(self, **attributes):
        """
        Parameters
        ----------
        attributes : dictionary
                     { 'name'      : container name,
                       'source'    : source directory,
                       'target'    : target directory,
        """
        self._name = "ubuntu"
        self._source = None
        self._target = None

        super().__init__(self.__dict__, attributes)

        # Condition to check if target and source directories are defined in the Maplefile
        # assign default if they are not, and deal with exceptions
        if not self._target:
            self._target = "/home/mount"
        if not self._source:
            self._source = os.getenv("PWD")

        # Set container name for environment variables
        self._container = self._name

    @property
    def name(self):
        """
        Getter for container name
        """
        return self._name

    def run(self, image, command, options=""):
        """
        Run a container and commit to image
        """
        self.setenv()
        image.setenv()
        Backend().container.run(command, options)

    def publish(self, image, command):
        """
        Publish a container to an image
        """
        cmd_list = None
        if command:
            cmd_list = [command]

        self.setenv()
        image.setenv()
        Backend().container.publish(cmd_list)

def Run(name, image, command, options=""):
    """
    Standalone run command
    """
    container = Container(name=name)
    container.run(image, command, options)


def Publish(name, image, command):
    """
    Standalone publish command
    """
    container = Container(name=name)
    container.publish(image, command)
