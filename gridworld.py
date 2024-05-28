class Gridworld:
    
    """
    Defines the Gridworld environment.
    
    Attributes:
        width (int): Width of the grid.
        height (int): Height of the grid.
        states (list): List of all possible states in the grid.
        rewards (dict): Specifies rewards for each state.
        terminals (list): List of terminal states.
        actions (list): Possible actions in the gridworld.
        transition_probs (dict): Transition probabilities for each action in each state.
    """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.states = [(x, y) for x in range(width) for y in range(height)]
        self.rewards = {(width-1, height-1): 10}
        self.terminals = [(width-1, height-1)]
        self.actions = ['up', 'down', 'left', 'right']
        self.transition_probs = self.create_transition_probs()
        
    def create_transition_probs(self):
        
        
        
        probs = {}
        for s in self.states:
            probs[s] = {}
            for a in self.actions:
                next_state = self.move(s, a)
                probs[s][a] = [(1.0, next_state, self.rewards.get(next_state, 0) if next_state in self.terminals else -1)]
        return probs
    
    def move(self, state, action):
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