import numpy as np

from Agent import AgentBFS, AgentDFS
from Environment import Environment


def generate_map(tam, prob):
    map = np.zeros((tam, tam))
    for i in range(len(map)):
        for j in range(len(map[0])):
            map[i][j] = 1 if np.random.random() < prob else 0

    map[0][0] = 0
    map[tam - 1][tam - 1] = 0
    print(map)
    return map


def show_result(agent_type, path):
    print(f"~~~ {agent_type} ~~~~~~~~~~~~~~~")
    print(f"Path: {path}")
    print(f"Size: {len(path)}")
    print("================================================")


if __name__ == "__main__":

    tam = 8
    prob = 1

    map = generate_map(tam, prob)
    """map = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
    ]"""

    start = [0, 0]
    goal = [tam - 1, tam - 1]

    # Busca em largura BFS
    env = Environment(map, start, goal)
    ag = AgentBFS(env)
    path = ag.act()
    show_result("BFS", path)

    # Busca em profundidade DFS
    env = Environment(map, start, goal)
    ag = AgentDFS(env)
    path = ag.act()
    show_result("DFS", path)
    # Guloso

    # Menor custo primeiro

    # A*

    # Branch and Bound
