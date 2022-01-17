"""Python API for maple"""

class MapleImage(object):
    """
    Class to manage images
    """
    def __init__(self,MapleEnv):
        super().__init__()
        self.env=MapleEnv

    def build(self):
        """
        Builds a local image from remote image
        """
        self.env.set_vars()
        self.env.backend.image.build()

    def pull(self):
        """
        Pull remote image
        """
        self.env.set_vars()
        self.env.backend.image.pull()

    def remove(self):
        """
        Remove remote container
        """
        self.env.set_vars()
        self.env.backend.image.remove()
