import random


class RLAgent:
    def __init__(self):
        self.q_table = {}   # (state, action) -> value
        self.actions = [0, 1, 2]  # execute, wait, ignore
        self.alpha = 0.5    # learning rate
        self.gamma = 0.9    # discount factor
        self.epsilon = 0.2  # exploration rate

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        # Exploration
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        # Exploitation
        q_values = [self.get_q(state, a) for a in self.actions]
        return self.actions[q_values.index(max(q_values))]

    def update(self, state, action, reward, next_state):
        old_q = self.get_q(state, action)
        next_max = max(self.get_q(next_state, a) for a in self.actions)

        new_q = old_q + self.alpha * (reward + self.gamma * next_max - old_q)
        self.q_table[(state, action)] = new_q
