"""Python API for maple"""

from . import MapleEnv, MapleImage, MapleContainer

from ..backend import docker,singularity

class Maple(object):
    """
    User interface to maple
    """
    backend = {'docker':docker, 'singularity':singularity}

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
        super().__init__()
        self.env = MapleEnv(**attributes)
        self.image = MapleImage(self.env)
        self.container = MapleContainer(self.env)
           
    def __getitem__(self,key):
        """
        Get variable data
        """
        return self.env[key]

    def __setitem__(self,key,value):
        """
        Set variable data
        """
        self.env[key] = value
