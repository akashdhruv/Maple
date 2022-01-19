"""Python API for maple"""

from .  import Environment, Image, Container
from .. import backend

class Maple(Environment):
    """
    User interface to maple
    """
    def __init__(self,**attributes):
        """
        Parameters
        ----------
        attributes : dictionary
                     { 'container' : container name,
                       'image'     : remote image name,
                       'source'    : source directory,
                       'target'    : target directory,
                       'user'      : local user,
                       'group'     : user's group,
                       'backend'   : container backend - docker/singularity
                       'port'      : port ID to deploy jupyter notebooks}
        """
        super().__init__(**attributes)
        self.image = Image(**attributes)
        self.container = Container(**attributes)
