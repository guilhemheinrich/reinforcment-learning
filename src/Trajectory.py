from typing import TypeVar, Generic

State = TypeVar('State') 
Action = TypeVar('Action')

class Step(Generic[State, Action]):
    def __init__(self, state: State, action: Action, value = 0):
        self.state = None
        self.action = None
        self.value = None
        pass


class Trajectory(Generic[State, Action]):
    def __init__(self, state: State, action: Action):
        self.trajectory = []
        self.trajectory.append(Step(state, action))

    def append(self, state: State, action: Action, value = 0):
        self.trajectory.append(Step(state, action, value))
