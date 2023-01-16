from typing import Generic, TypeVar, Tuple, Annotated, Dict, Callable

State = TypeVar('State')
ValueType = TypeVar('ValueType')
# MemoryTuple = TypeVar('MemoryTuple', bound=Tuple)

class Game(Generic[State, ValueType]):
    """ Class handling the core logic of what a game is. In that case a finite state vector, with a return value function for each state.
    """
    def __init__(self, 
    state_value_function: Callable[[State], ValueType], 
    action_dict: Dict[str, Callable[[State, list],  State | None]],  
    memory_length: int = 0):
        self.state_value_function  = state_value_function
        self.action_dict  = action_dict
        self.memory_length = memory_length
        self.memory: list =  memory_length * [None]
        pass

    def takeAction(self, current_state: State, action_key: str) -> State | None:
        next_state = self.action_dict[action_key](current_state, self.memory)
        if (self.memory_length > 0):
            self.memory.append(next_state)
            self.memory = self.memory[- self.memory_length:]
        print(self.memory)
        return next_state

    def initialState(self, state):
        next_state = state
        if (self.memory_length > 0):
            self.memory.append(next_state)
            self.memory = self.memory[- self.memory_length:]
        return next_state

    """Take a state and return the associated value
    """
    def valueOf(self, state: State | None) -> ValueType | None:
        if (state is None):
            return None
        return self.state_value_function(state)

