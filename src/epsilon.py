import numpy as np
from src.constants import ALPHA, GAMMA, ACTION, Q_TABLE, MAX_EPSILON, MIN_EPSILON, DECAY_RATE

def action_selection(epsilon, discrete_state):
    random_number = np.random.random()

    # EXPLOITATION (choose the action that maximizes Q)
    if random_number > epsilon:
        state = Q_TABLE[discrete_state, :]

        return np.argmax(state)

    # EXPLORATION (choose random action)
    return np.random.choice([
        ACTION.LEFT,
        ACTION.DOWN,
        ACTION.RIGHT,
        ACTION.UP
    ])

def compute_next_q_value(reward, old_q_value, next_q_value):
    return old_q_value + ALPHA * (reward + GAMMA * next_q_value - old_q_value)

def reduce_epsilon(epoch):
    return MIN_EPSILON + (MAX_EPSILON - MIN_EPSILON) * np.exp(-DECAY_RATE * epoch)
