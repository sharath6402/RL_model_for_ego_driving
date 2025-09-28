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
git clone https://github.com/sharath6402/RL_model_for_ego_driving.git
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```



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
├── requirements.txt      
├── README.md              

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
