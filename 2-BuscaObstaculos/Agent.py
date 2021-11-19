class Agent:
    """
    This class implements an interface for an agent
    """

    def __init__(self, env):
        self.env = env

    def act(self):
        raise NotImplementedError("act")
