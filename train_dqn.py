from lane_merge_env import LaneMergingEnv
from stable_baselines3 import DQN

# Create env directly
env = LaneMergingEnv(render_mode="human")

# Train
model = DQN("MlpPolicy", env, verbose=1, learning_rate=1e-3,
            buffer_size=10000, batch_size=32, tensorboard_log="./dqn_lane_merge_log/")

model.learn(total_timesteps=50000)
model.save("dqn_lane_merge")

# Test
# obs, _ = env.reset()
# for _ in range(200):
#     action, _ = model.predict(obs, deterministic=True)
#     obs, reward, done, _, _ = env.step(action)
#     env.render()
#     if done:
#         obs, _ = env.reset()


obs, _ = env.reset()
for _ in range(200):
    action = env.action_space.sample()  # random action
    obs, reward, done, _, _ = env.step(action)
    env.render()
    if done:
        obs, _ = env.reset()
