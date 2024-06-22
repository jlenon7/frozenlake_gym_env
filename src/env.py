import gym
from src.constants import initialize_q_table, ENV_NAME

gym.register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False},
    max_episode_steps=100,
    reward_threshold=.8196
)

env = gym.make(ENV_NAME,  render_mode='human')
rgb_env = gym.make(ENV_NAME, render_mode='rgb_array')

action_size = env.action_space.n
state_size = env.observation_space.n

initialize_q_table(state_size, action_size)
