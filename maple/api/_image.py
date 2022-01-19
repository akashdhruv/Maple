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
        Builds a local image from base image
        """
        self.env.set_vars()
        self.env.backend.image.build()

    def set(self):
        """
        Set a base image from local image
        """
        self.env.set_vars()
        self.env.backend.image.set()

    def get(self):
        """
        Get a local image from base image
        """
        self.env.set_vars()
        self.env.backend.image.get()

    def clean(self):
        """
        Clean local image
        """
        self.env.set_vars()
        self.env.backend.image.clean()

    def remove(self):
        """
        Remove a base image
        """
        self.env.set_vars()
        self.env.backend.image.remove()
