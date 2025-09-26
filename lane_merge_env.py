import gymnasium as gym
from gymnasium import spaces
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class LaneMergingEnv(gym.Env):
    """
    Simple 1D lane merging toy environment
    """

    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode  # Gym passes this automatically

        # Continuous state
        self.observation_space = spaces.Box(
            low=np.array([0.0, 0.0, -100.0, -100.0]),
            high=np.array([100.0, 30.0, 100.0, 100.0]),
            dtype=np.float32
        )

        # Discrete actions: slow, keep, speed up
        self.action_space = spaces.Discrete(3)

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.ego_pos = 0.0
        self.ego_speed = 10.0
        self.gap_front = np.random.uniform(15, 40)
        self.gap_back = np.random.uniform(15, 40)
        self.steps = 0

        obs = np.array([self.ego_pos, self.ego_speed, self.gap_front, self.gap_back], dtype=np.float32)
        return obs, {}

    def step(self, action):
        if action == 0:
            self.ego_speed = max(0, self.ego_speed - 2)
        elif action == 2:
            self.ego_speed = min(30, self.ego_speed + 2)

        self.ego_pos += self.ego_speed * 0.1
        self.gap_front -= self.ego_speed * 0.1
        self.gap_back += self.ego_speed * 0.1

        self.steps += 1
        terminated = False
        reward = -0.1

        if 0 < self.gap_back < 30 and 0 < self.gap_front < 30:
            reward += 10
            terminated = True

        if self.gap_front <= 0 or self.gap_back <= 0:
            reward -= 100
            terminated = True

        if self.steps >= 200:
            terminated = True

        obs = np.array([self.ego_pos, self.ego_speed, self.gap_front, self.gap_back], dtype=np.float32)
        return obs, reward, terminated, False, {}

    def render(self):
        if self.render_mode == "human":
            print(f"Step {self.steps} | Ego pos={self.ego_pos:.1f}, "
                  f"speed={self.ego_speed:.1f}, "
                  f"gap_front={self.gap_front:.1f}, gap_back={self.gap_back:.1f}")
    def render(self):
        if not hasattr(self, "fig"):
            self.fig, self.ax = plt.subplots(figsize=(8, 4))
            plt.ion()
            self.ax.set_xlim(0, 100)
            self.ax.set_ylim(-2, 2)
            self.ego_car = patches.Rectangle((self.ego_pos, 0), 2, 1, color="blue", label="Ego Car")
            self.front_car = patches.Rectangle((self.ego_pos + self.gap_front, 0), 2, 1, color="red", label="Front Car")
            self.back_car = patches.Rectangle((self.ego_pos - self.gap_back, 0), 2, 1, color="green", label="Back Car")
            self.ax.add_patch(self.ego_car)
            self.ax.add_patch(self.front_car)
            self.ax.add_patch(self.back_car)
            self.ax.legend()
        
        # Update positions
        self.ego_car.set_x(self.ego_pos)
        self.front_car.set_x(self.ego_pos + self.gap_front)
        self.back_car.set_x(self.ego_pos - self.gap_back)
        
        self.ax.set_title(f"Step {self.steps} | Speed={self.ego_speed:.1f}")
        plt.pause(0.01)
