class Game(object):
    """ Class handling the core logic of what a game is. In that case a finite state vector, with a return value function for each state.
    """

    def valueOf(self, state):
        """Take a state and return the associated value
        
        Note that while this function depend on a state, it may also depends on the previous state path. Also, nothing force the return value to be deterministic"""
        pass

