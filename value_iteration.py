def value_iteration(env, gamma=0.99, threshold=0.01):
    
    """
    Perform the value iteration method to find the optimal value function.

    Args:
        env (Gridworld): The Gridworld environment.
        gamma (float): Discount factor.
        threshold (float): Threshold for determining convergence.

    Returns:
        dict: Optimal value function mapping each state to its value.
    """
    
    V = {s: 0 for s in env.states}
    while True:
        delta = 0
        for s in env.states:
            if s in env.terminals:
                continue
            Vs_old = V[s]
            V[s] = max(sum(p * (r + gamma * V[s_next]) for (p, s_next, r) in env.transition_probs[s][a]) for a in env.actions)
            delta = max(delta, abs(V[s] - Vs_old))
        if delta < threshold:
            break
    return V