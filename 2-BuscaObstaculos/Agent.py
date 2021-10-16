class AgentBFS:
    def __init__(self, env):

        self.belief_state = env.initial_percepts()
        self.env = env

    def act(self):

        F = [[self.belief_state["position"]]]

        while F:
            path = F.pop(0)

            self.belief_state = self.env.signal({"go_to": path[-1]})

            if (path[-1] == self.belief_state["goal"]).all():
                return path
            else:
                for p in self.belief_state["available_positions"]:
                    F.append(path + [p])

        return []


class AgentDFS:
    def __init__(self, env):

        self.belief_state = env.initial_percepts()
        self.env = env

    def act(self):

        F = [[self.belief_state["position"]]]

        while F:
            path = F.pop(0)

            self.belief_state = self.env.signal({"go_to": path[-1]})

            if (path[-1] == self.belief_state["goal"]).all():
                return path
            else:
                for p in self.belief_state["available_positions"]:

                    # Checks whether a cycle will be made
                    makes_cycle = False
                    for pos in path:
                        if (pos == p).all():
                            makes_cycle = True
                            break

                    if not makes_cycle:
                        F = [path + [p]] + F

        return []
