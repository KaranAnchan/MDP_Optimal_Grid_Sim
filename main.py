from gridworld import Gridworld
from value_iteration import value_iteration, extract_policy
from visualizations import visualize_policy_grid, plot_value_function_evolution

def main():
    """
    Main function to initialize the gridworld, run value iteration, extract the optimal policy,
    and generate visualizations.
    """
    # Initialize the Gridworld environment
    env = Gridworld(5, 5)

    # Perform value iteration to find optimal values
    V = value_iteration(env)

    # Extract the optimal policy based on the optimal value function
    policy = extract_policy(V, env)

    # Visualize the optimal policy grid
    visualize_policy_grid(policy, env.width, env.height, "optimal_policy_grid.png")

    # Visualize the evolution of the value function during the value iteration process
    plot_value_function_evolution(env, "value_function_evolution.png")

if __name__ == "__main__":
    main()