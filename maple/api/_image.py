"""Python API for maple"""

from .  import Environment
from .. import backend

class Image(Environment):
    """
    Class to manage images
    """
    def __init__(self,**attributes):
        super().__init__(**attributes)

    def build(self,image):
        """
        Builds a local image from base image
        """
        self.setvars()
        backend.dict[self.backend].image.build(image)
