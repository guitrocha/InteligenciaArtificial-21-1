class Environment:
    """
    This class implements and interface for an Environment
    """

    def initial_percepts(self):
        raise NotImplementedError("initial_percepts")

    def signal(self, action):
        raise NotImplementedError("signal")
