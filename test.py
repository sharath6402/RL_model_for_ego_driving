"""
Test script for LaneMergingEnv
- Runs random actions (sanity check)
- Runs trained DQN agent (if model exists)
"""

import os
from lane_merge_env import LaneMergingEnv
from stable_baselines3 import DQN


def run_random_policy(steps=50):
    print("🚗 Running random policy...")
    env = LaneMergingEnv(render_mode="human")
    obs, _ = env.reset()

    for _ in range(steps):
        action = env.action_space.sample()
        obs, reward, done, _, _ = env.step(action)
        env.render()
        if done:
            print("⚠️ Episode ended (random policy)")
            obs, _ = env.reset()


def run_trained_agent(model_path="dqn_lane_merge.zip", steps=200):
    if not os.path.exists(model_path):
        print(f"❌ No trained model found at {model_path}. Run train_dqn.py first.")
        return

    print("🤖 Running trained agent...")
    env = LaneMergingEnv(render_mode="human")
    model = DQN.load(model_path, env=env)

    obs, _ = env.reset()
    for _ in range(steps):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, _, _ = env.step(action)
        env.render()
        if done:
            print("✅ Episode finished (trained agent)")
            obs, _ = env.reset()


if __name__ == "__main__":
    run_random_policy(steps=50)
    run_trained_agent(steps=200)
