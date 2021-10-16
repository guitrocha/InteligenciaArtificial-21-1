from Agent import AgentBFS, AgentDFS
from Environment import Environment

if __name__ == "__main__":

    map = [
        [0, 0, 1],
        [1, 0, 1],
        [1, 0, 0],
    ]

    # Busca em largura BFS
    # Busca em profundidade DFS
    # Guloso
    # Menor custo primeiro
    # A*
    # Branch and Bound
    env = Environment(map, [0, 0], [2, 2])
    ag = AgentDFS(env)
    path = ag.act()
    print(path)

    env = Environment(map, [0, 0], [2, 2])
    ag = AgentBFS(env)
    path = ag.act()
    print(path)


def generate_map():
    pass
