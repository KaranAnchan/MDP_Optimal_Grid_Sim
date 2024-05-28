class Gridworld:
    
    """
    Represents a gridworld environment where an agent can move in four directions with specific rewards and terminal states.

    Attributes:
        width (int): The width of the grid.
        height (int): The height of the grid.
        states (list of tuples): All possible (x, y) positions in the grid.
        rewards (dict): Dictionary with terminal state(s) and corresponding rewards.
        terminals (list of tuples): States where the game ends.
        actions (list): List of possible actions (up, down, left, right).
        transition_probs (dict): Transition probabilities for moving from one state to another given an action.
    """

    def __init__(self, width, height):
        
        """Initialize the gridworld environment with given dimensions."""
        
        self.width = width
        self.height = height
        self.states = [(x, y) for x in range(width) for y in range(height)]
        self.rewards = {(width-1, height-1): 10}
        self.terminals = [(width-1, height-1)]
        self.actions = ['up', 'down', 'left', 'right']
        self.transition_probs = self.create_transition_probs()
        
    def create_transition_probs(self):
        
        """Generate the transition probabilities for each action in each state."""
        
        probs = {}
        for s in self.states:
            probs[s] = {}
            for a in self.actions:
                next_state = self.move(s, a)
                probs[s][a] = [(1.0, next_state, self.rewards.get(next_state, 0) if next_state in self.terminals else -1)]
        return probs
    
    def move(self, state, action):
        
        """Calculate the next state given the current state and an action."""
        
        x, y = state
        if action == 'up':
            y = max(y - 1, 0)
        elif action == 'down':
            y = min(y + 1, self.height - 1)
        elif action == 'left':
            x = max(x - 1, 0)
        elif action == 'right':
            x = min(x + 1, self.width - 1)
        return (x, y)