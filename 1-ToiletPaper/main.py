import matplotlib.pyplot as plt

from Agent import Agent
from Environment import Environment

if __name__ == "__main__":
    env = Environment(0, 1.2)
    ag = Agent(env)

    prices = []
    n = []

    for i in range(1000):
        ag.act()
        prices.append(env.price)
        n.append(env.n)

    plt.plot(prices)
    plt.show()

    plt.plot(n)
    plt.show()

    plt.plot(ag.spendings)
    plt.show()
