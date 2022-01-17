"""Python API for maple"""

class MapleContainer(object):
    """
    Class to manage containers
    """
    def __init__(self,MapleEnv):
        super().__init__()
        self.env=MapleEnv

    def execute(self,command,commit=False):
        """
        Execute command
        """
        self.env.set_vars()
        self.env.backend.container.execute(command,commit)

    def notebook(self):
        """
        Launch ipython notebook inside the container
        """
        self.env.set_vars()
        self.env.backend.container.notebook()
