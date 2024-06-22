import numpy as np

ENV_NAME = 'FrozenLakeNotSlippery-v0'

# Episodes
EPOCHS = 20000

# Learning rate
ALPHA = 0.8

# Discount rate
GAMMA = 0.95

EPSILON = 1.0
MAX_EPSILON = 1.0
MIN_EPSILON = 0.01
DECAY_RATE = 0.001

Q_TABLE = None

def initialize_q_table(state_size, action_size):
    global Q_TABLE
    Q_TABLE = np.zeros([state_size, action_size])

class ACTION:
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3
