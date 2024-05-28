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