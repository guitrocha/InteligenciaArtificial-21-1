import numpy as np


class Environment:
    def __init__(self, n, price):
        self.n = n
        self.price = price
        self.clock = 0

        self.mu_usage = [10, 100, 150, 300, 125, 50, 15]
        self.sigma_usage = [2, 10, 10, 20, 10, 10, 2]
        self.mu_price = 1.2
        self.sigma_price = 0.2
        self.on_sale = False
        self.max_n = 1500

    def initial_percepts(self):
        return {"n": self.n, "price": self.price, "max_n": self.max_n}

    def signal(self, action):

        usage = np.random.normal(
            self.mu_usage[self.clock % len(self.mu_usage)],
            self.sigma_usage[self.clock % len(self.sigma_usage)],
        )
        bought = action["to_buy"]

        self.n = self.n - usage + bought

        if self.clock % 7 == 0:
            self.price = 1.2

            self.on_sale = True if np.random.rand() < 0.5 else False

            if self.on_sale:
                self.price -= self.sigma_price
            else:
                self.price = max(np.random.normal(self.mu_price, self.sigma_price), 0.9)

        self.clock += 1
        return {"n": self.n, "price": self.price, "max_n": self.max_n}
