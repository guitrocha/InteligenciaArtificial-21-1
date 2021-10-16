import numpy as np


class Environment:
    def __init__(self, map, start, goal):
        self.map = np.array(map)
        self.start = np.array(start)
        self.goal = np.array(goal)
        self.agent_position = np.array(start)
        self.actions = np.array(
            [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1],
                [1, 1],
                [-1, 1],
                [1, -1],
                [-1, -1],
            ]
        )

    def initial_percepts(self):
        available = []
        for a in self.actions:
            pos = self.start + a
            if (
                (0 <= pos[0] < self.map.shape[0])
                and (0 <= pos[1] < self.map.shape[1])
                and self.map[pos[0]][pos[1]] == 0
            ):
                available.append(pos)

        return {
            "available_positions": available,
            "position": self.agent_position,
            "goal": self.goal,
        }

    def signal(self, action):

        self.agent_position = action["go_to"]

        available = []
        for a in self.actions:
            pos = self.agent_position + a
            if (
                (0 <= pos[0] < self.map.shape[0])
                and (0 <= pos[1] < self.map.shape[1])
                and self.map[pos[0]][pos[1]] == 0
            ):
                available.append(pos)

        return {
            "available_positions": available,
            "position": self.agent_position,
            "goal": self.goal,
        }
