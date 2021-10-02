import math


class Agent:
    def __init__(self, env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.spendings = []
        self.stockzero = 0
        self.clock = 1
        self.S = {
            "cheap": self.percepts["price"],
            "low": self.percepts["max_n"],
        }

        self.recent_prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.r_index = 0  # recent index
        for i in range(0, 10):
            self.recent_prices[i] = self.percepts["price"]
        self.recent_usage = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for i in range(0, 10):
            self.recent_usage[i] = self.percepts["usage"]

    def act(self):
        # Verifies env's state

        # Define to_buy
        to_buy = 0

        if self.percepts["price"] <= self.S["cheap"]:
            to_buy = self.percepts["max_n"] - self.percepts["n"]
        elif (
            self.percepts["n"] < self.S["low"]
            and self.percepts["price"] > 1.65 * self.S["cheap"]
        ):
            to_buy = self.S["low"] - self.percepts["n"]
        elif (
            self.percepts["n"] < self.S["low"]
            and self.percepts["price"] <= 1.65 * self.S["cheap"]
        ):
            to_buy = (self.S["low"] - self.percepts["n"]) * 2
        else:
            to_buy = 0
        action = {"to_buy": to_buy}

        # Act
        self.spendings.append(to_buy * self.percepts["price"])
        self.percepts = self.env.signal(action)

        # Update belief state
        self.recent_prices[self.r_index] = self.percepts["price"]
        self.recent_usage[self.r_index] = self.percepts["usage"]
        if self.r_index == 9:
            self.r_index = 0
        else:
            self.r_index += 1

        self.S = {
            "cheap": sum(self.recent_prices) / len(self.recent_prices),
            "low": math.floor(sum(self.recent_usage) / len(self.recent_usage)),
        }

        if self.percepts["n"] == 0:
            self.stockzero += 1

        self.clock += 1
