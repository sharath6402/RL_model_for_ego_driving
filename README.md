# RL_model_for_ego_driving
Building an Reinforcement model for ego driving


# 🚗 Lane Merging RL Simulator

A simple **custom Gymnasium environment** for testing **Reinforcement Learning (RL)** algorithms on a **lane merging scenario** (bottleneck highway situation).

The environment simulates an **ego car** trying to merge between a front and back car, learning safe and efficient strategies via RL (e.g., **DQN**).

---

## 📌 Features

* Custom **Gymnasium environment** (`LaneMergingEnv`)
* Simple **state space**: ego position, speed, gap front, gap back
* Discrete **action space**:

  * `0 = slow down`
  * `1 = keep speed`
  * `2 = speed up`
* Reward shaping for **safe merging** and **collision penalties**
* **Matplotlib animation** to visualize cars on the highway
* Compatible with **Stable-Baselines3** for training

---

## 🛠 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/lane-merging-rl.git
cd lane-merging-rl
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### requirements.txt

```
gymnasium
numpy
matplotlib
stable-baselines3
```

---

## ▶️ Usage

### 1. Run the environment manually

```python
from lane_merge_env import LaneMergingEnv

env = LaneMergingEnv(render_mode="human")
obs, _ = env.reset()

for _ in range(200):
    action = env.action_space.sample()  # random action
    obs, reward, done, _, _ = env.step(action)
    env.render()
    if done:
        obs, _ = env.reset()
```

---

### 2. Train a DQN agent

```python
from lane_merge_env import LaneMergingEnv
from stable_baselines3 import DQN

env = LaneMergingEnv(render_mode=None)

model = DQN("MlpPolicy", env, verbose=1, learning_rate=1e-3,
            buffer_size=10000, batch_size=32,
            tensorboard_log="./dqn_lane_merge_log/")

model.learn(total_timesteps=50000)
model.save("dqn_lane_merge")
```

---

### 3. Visualize trained agent

```python
model = DQN.load("dqn_lane_merge", env=LaneMergingEnv(render_mode="human"))
obs, _ = env.reset()

for _ in range(200):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, _, _ = env.step(action)
    env.render()
    if done:
        obs, _ = env.reset()
```

---

## 🎥 Animation Example

The environment uses **Matplotlib** to visualize:

* 🟦 Ego car (blue)
* 🟥 Front car (red)
* 🟩 Back car (green)

<img src="docs/sample_animation.gif" width="600" />

---

## 📂 Project Structure

```
.
├── lane_merge_env.py      # Custom Gymnasium environment
├── train_dqn.py           # Training script with Stable-Baselines3 DQN
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── docs/
    └── sample_animation.gif   # Example animation (for GitHub preview)
```

---

## 📊 Research Motivation

This project is intended as a **research tool** to test and benchmark RL algorithms in **traffic bottleneck / lane merging scenarios**, where decision-making is critical for safety and efficiency.

Possible extensions:

* Multi-agent interactions
* Continuous action spaces (throttle/brake)
* Realistic traffic flow simulations

---

## 📜 License

MIT License – free to use and modify.

---

👉 Do you also want me to create a **`requirements.txt` and sample `train_dqn.py`** so that someone cloning your repo can literally run it without editing?

