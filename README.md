
---

# Gridworld Simulation 🌍🚀

## Overview 📖

Welcome to the Gridworld Simulation project! This repository showcases an implementation of a classic reinforcement learning problem, where an agent navigates through a grid to maximize its rewards. The primary focus is on utilizing the Value Iteration algorithm to determine the optimal policy for the agent, allowing it to find the most efficient path to the goal.

## Components of the Repository 🗂️

- `gridworld.py`: Defines the Gridworld class, encapsulating the environment, including states, actions, rewards, and transitions.
- `value_iteration.py`: Implements the Value Iteration algorithm, a dynamic programming method used to compute the optimal policy for the agent.
- `visualizations.py`: Contains functions to visually represent the optimal policy and the evolution of the value function throughout the algorithm's execution.
- `main.py`: The executable script that ties all components together, running the simulation and generating insightful visualizations.

## Environment Details 🌐

### States
Each position in a 5x5 grid is represented as a state (x, y), where both x and y range from 0 to 4.

### Actions
The agent can move in four directions:
- 'Up' 🡑
- 'Down' 🡓
- 'Left' 🡐
- 'Right' 🡒

### Rewards
- **Terminal State Reward**: The agent receives a reward of +10 upon reaching the terminal state located at the bottom-right corner of the grid.
- **Step Penalty**: To encourage efficiency, a penalty of -1 is applied for each movement, pushing the agent to find the quickest route.

## Setup & Installation 🛠️

Before running the simulation, ensure you have Python and the following packages installed:
- `numpy`
- `matplotlib`

You can install these using pip with the following command:

```bash
pip install numpy matplotlib
```

## Running the Simulation 🚀

To execute the simulation and see the algorithm in action, run:

```bash
python main.py
```

## Visualizations 📊

### Optimal Policy Grid

The Optimal Policy Grid visualization indicates the best action to take from each state to reach the terminal state most efficiently.

![Optimal Policy Grid](optimal_policy_grid.png)

### Value Function Evolution

This plot shows how the value estimates for each state converge over iterations of the Value Iteration algorithm, demonstrating the algorithm's efficiency and effectiveness.

![Value Function Evolution](value_function_evolution.png)

## Inferences from Visualizations 🧐

- **Optimal Policy Grid**: Clearly illustrates the strategic moves the agent should take at each point in the grid to minimize penalties and maximize rewards.
- **Value Function Evolution**: Provides a visual representation of the algorithm's convergence, highlighting how quickly and effectively it reaches optimal values.

This project offers a fascinating glimpse into the capabilities of dynamic programming in solving decision-making problems in a defined environment. Feel free to tweak the parameters, explore the code, and observe how changes impact the agent's strategy and efficiency!

---
