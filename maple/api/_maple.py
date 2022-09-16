"""Python API for maple"""

import os
import toml


class Maple:
    """
    Base class for defining maple environment

    Parameters
    ----------
    default_attributes : dictionary of default attributes
    attributes         : dictionary of user attributes
    """

    def __init__(self, default_attributes, attributes):

        super().__init__()

        Maplefile = os.path.exists("Maplefile")

        if Maplefile:
            for key, value in toml.load("Maplefile").items():
                if key in ["mpi", "platform", "backend"]:
                    default_attributes["_" + key] = str(value)

        self._set_attributes(default_attributes, attributes)

    def setenv(self):
        """
        Set environment variables
        """
        for key, value in self.__dict__.items():
            if value and key != "_name":
                os.environ["maple" + key] = str(value)

    def _set_attributes(self, default_attributes, attributes):
        """
        Private method for initialization

        Parameters
        ----------
        default_attributes : dictionary of default attributes
        attributes         : dictionary of user attributes
        """

        for key in attributes:
            if "_" + key in default_attributes:
                default_attributes["_" + key] = attributes[key]
            else:
                raise ValueError(f'[maple]: attribute "{key}" not present')

        for key, value in default_attributes.items():
            setattr(self, key, value)
