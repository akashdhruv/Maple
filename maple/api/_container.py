"""Python API for maple"""

from .  import Environment
from .. import backend

class Container(Environment):
    """
    Class to manage containers
    """
    def __init__(self,**attributes):
        super().__init__(**attributes)

    def pour(self,image):
        """
        Pour a container
        """
        self.setvars()
        backend.dict[self.backend].container.pour(image)

    def rinse(self):
        """
        Rinse a container
        """
        self.setvars()
        backend.dict[self.backend].container.rinse()

    def execute(self,command):
        """
        Execute command
        """
        self.setvars()
        backend.dict[self.backend].container.execute(command)
