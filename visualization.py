import numpy as np
import matplotlib.pyplot as plt

def visualize_policy_grid(policy, width, height, filename=None):
    
    """
    Visualize the grid policy as a color grid where each cell represents the action taken in that state.

    Args:
        policy (dict): The policy to visualize.
        width (int): The width of the grid.
        height (int): The height of the grid.
        filename (str, optional): Path to save the visualization.
    """
    
    grid = np.full((height, width), ' ')
    for y in range(height):
        for x in range(width):
            grid[y, x] = policy[(x, y)][0] if policy[(x, y)] != 'None' else 'T'
    
    fig, ax = plt.subplots(figsize=(7, 7))
    cax = ax.matshow(np.arange(width*height).reshape(height, width), cmap='viridis')
    plt.colorbar(cax)
    
    for (i, j), val in np.ndenumerate(grid):
        ax.text(j, i, val, ha='center', va='center', color='white')
        
    ax.set_xticks(np.arange(grid.shape[1]))
    ax.set_yticks(np.arange(grid.shape[0]))
    ax.set_xticklabels(np.arange(1, grid.shape[1]+1))
    ax.set_yticklabels(np.arange(1, grid.shape[0]+1))
    plt.title("Optimal Policy")
    if filename:
        plt.savefig(filename)
    plt.show()
    
def plot_value_function_evolution(env, gamma=0.99, threshold=0.01, filename=None):
    
    """
    Plot the evolution of the value function over iterations during value iteration.

    Args:
        env (Gridworld): The Gridworld environment.
        gamma (float): Discount factor.
        threshold (float): Threshold for convergence.
        filename (str, optional): Path to save the plot.
    """
    
    V = {s: 0 for s in env.states}
    iteration = 0
    values_over_time = []

    while True:
        delta = 0
        for s in env.states:
            if s in env.terminals:
                continue
            Vs_old = V[s]
            V[s] = max(sum(p * (r + gamma * V[s_next]) for (p, s_next, r) in env.transition_probs[s][a]) for a in env.actions)
            delta = max(delta, abs(V[s] - Vs_old))
        values_over_time.append(list(V.values()))
        iteration += 1
        if delta < threshold:
            break

    values_over_time = np.array(values_over_time).T
    plt.figure(figsize=(10, 6))
    for i, values in enumerate(values_over_time):
        plt.plot(values, label=f'State {env.states[i]}')
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.title('Value Function Evolution Over Iterations')
    plt.legend()
    plt.grid(True)
    plt.show()