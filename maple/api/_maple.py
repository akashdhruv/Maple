"""Python API for maple"""

import os


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
        self._set_attributes(default_attributes, attributes)

    def setenv(self):
        """
        Set environment variables
        """
        for key, value in self.__dict__.items():
            if value and key != "name":
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
            if key in default_attributes:
                default_attributes[key] = attributes[key]
            else:
                raise ValueError(f'[maple]: attribute "{key}" not present')

        for key, value in default_attributes.items():
            setattr(self, key, value)
