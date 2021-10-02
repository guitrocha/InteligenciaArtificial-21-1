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

    fig, axs = plt.subplots(3)
    fig.suptitle(
        f"Days without toilet-paper = {ag.stockzero}   |   Total Spent = R$ {sum(ag.spendings):.2f}"
    )
    axs[0].plot(prices, color="orange")
    axs[0].set_title("Prices")

    axs[1].plot(n, color="green")
    axs[1].set_title("Stock")

    axs[2].plot(ag.spendings, color="blue")
    axs[2].set_title("Spendings")

    # plt.legend(["Prices", "Stock", "Spendings"])

    plt.show()
