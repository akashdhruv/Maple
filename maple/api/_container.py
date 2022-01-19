"""Python API for maple"""

class MapleContainer(object):
    """
    Class to manage containers
    """
    def __init__(self,MapleEnv):
        super().__init__()
        self.env=MapleEnv

    def pour(self):
        """
        Pour a container
        """
        self.env.set_vars()
        self.env.backend.container.pour()

    def rinse(self):
        """
        Rinse a container
        """
        self.env.set_vars()
        self.env.backend.container.rinse()

    def execute(self,command):
        """
        Execute command
        """
        self.env.set_vars()
        self.env.backend.container.execute(command)
