"""Python API for maple"""

import os
import random

class Environment(object):
    """
    Base class for defining maple environment
    """
    def __init__(self,default_attributes,attributes):
        """
        Parameters
        ----------
        default_attributes : dictionary of default attributes
        attributes         : dictionary of user attributes
        """
        super().__init__()
        self._set_attributes(default_attributes,attributes)
 
    def setvars(self):
        """
        Set environment variables
        """
        for key, value in self.__dict__.items():
            if value and key != 'name': os.environ['maple'+key] = str(value)

    def _set_attributes(self,default_attributes,attributes):
        """
        Private method for initialization
        """

        for key in attributes:
            if key in default_attributes:
                default_attributes[key] = attributes[key]
            else:
                raise ValueError('[maple]: attribute "{}" not present'.format(key))

        for key, value in default_attributes.items(): setattr(self,'_'+key,value)
