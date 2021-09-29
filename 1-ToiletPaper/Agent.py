class Agent:
    def __init__(self, env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.spendings = []
        self.clock = 1
        self.S = {
            "average_price": self.percepts["price"],
            "cheap": self.percepts["price"],
            "low": 0,
            "min": self.percepts["max_n"],
        }

    def act(self):
        # Verifies env's state

        # Define to_buy
        to_buy = 0
        if self.percepts["n"] <= self.S["low"]:
            to_buy = self.S["min"] - self.percepts["n"]
        elif self.percepts["price"] <= self.S["low"]:
            to_buy = self.percepts["max_n"] - self.percepts["n"]
        else:
            to_buy = 0

        action = {"to_buy": to_buy}

        # Act
        self.spendings.append(to_buy * self.percepts["price"])
        self.percepts = self.env.signal(action)

        # Update belief state
        self.S = {
            "average_price": (
                self.S["average_price"] * self.clock + self.percepts["price"]
            )
            / (self.clock + 1),
            "cheap": self.percepts["price"],
            "low": 100,
            "min": self.percepts["max_n"],
        }

        self.clock += 1
