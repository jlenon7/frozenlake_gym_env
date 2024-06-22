import numpy as np
from src.env import env
import src.epsilon as eps
from src.helpers import path
import matplotlib.pyplot as plt
from src.constants import EPOCHS, EPSILON, Q_TABLE

rewards = []
log_interval = 100
render_interval = 1000

epoch_plot_tracker = []
total_reward_plot_tracker = []

for epoch in range(EPOCHS):
    state = env.reset()
    terminated = False
    total_rewards = 0

    # Agents play game
    while not terminated:
        if epoch % render_interval == 0:
          env.render(mode='human')

        # ACTION
        action = eps.action_selection(EPSILON, state)

        # Next steps
        new_state, reward, terminated, info = env.step(action)

        # Old (Current) Q Value. Q(st, at)
        old_q_value = Q_TABLE[state, action]

        # The next Q Value (Max Q Value for this state). Q(st+1, at+1)
        new_q_value = np.max(Q_TABLE[new_state, :])

        # Compute next Q Value
        next_q = eps.compute_next_q_value(reward, old_q_value, new_q_value)

        # Update the table
        Q_TABLE[state, action] = next_q

        # Track rewards
        total_rewards = total_rewards + reward
        state = new_state

    # Agent finished a round of the game
    epoch += 1
    EPSILON = eps.reduce_epsilon(epoch)
    rewards.append(total_rewards)

    epoch_plot_tracker.append(epoch)
    total_reward_plot_tracker.append(np.sum(rewards))

    if epoch % log_interval == 0:
        print(f'Epoch: {epoch}, Rewards: {np.sum(rewards)}')

env.close()
plt.figure(figsize=(8, 8))
plt.xlabel('Epochs')
plt.ylabel('Rewards')
plt.plot(epoch_plot_tracker, total_reward_plot_tracker)
plt.savefig(path.plots('epoch-reward-tracker.png'))
