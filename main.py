from src.Game2D import Game2D
from src.Action import Action
from src.Trajectory import Trajectory

import numpy as np
from typing import TypeVar, Generic, Tuple
# Actions

# top = Action("top"



game1 = Game2D(np.array([
    [0, 0, 0, 0, -1000], 
    [0, -1000, 0, 0, -1000],
    [0, 0, -1000, 0, 0],
    [-1000, 0, 0, 0, -1000],
    [0, 0, 0, 0, +1000],
    ]))

game1.valueOf((1, 2))

board = np.array([
    [0, 0, 0, 0, -1000], 
    [0, -1000, 0, 0, -1000],
    [0, 0, -1000, 0, 0],
    [-1000, 0, 0, 0, -1000],
    [0, 0, 0, 0, +1000],
    ])

def right(state: Tuple[int, int]) -> Tuple[int, int] | None:
    # valid initial state
    assert(state[0] >= 0 and state[0] < board.shape[0]) # X axis
    assert(state[1] >= 0 and state[1] < board.shape[1]) # Y axis
    if (state[1] + 1 < board.shape[1] and state[1] + 1 >= 0):
        return (state[0], state[1] + 1)
    else:
        return None
    
def left(state: Tuple[int, int]) -> Tuple[int, int] | None:
    # valid initial state
    assert(state[0] >= 0 and state[0] < board.shape[0]) # X axis
    assert(state[1] >= 0 and state[1] < board.shape[1]) # Y axis
    if (state[1] - 1 < board.shape[1] and state[1] - 1 >= 0):
        return (state[0], state[1] - 1)
    else:
        return None

def bottom(state: Tuple[int, int]) -> Tuple[int, int] | None:
    # valid initial state
    assert(state[0] >= 0 and state[0] < board.shape[0]) # X axis
    assert(state[1] >= 0 and state[1] < board.shape[1]) # Y axis
    if (state[0] + 1 < board.shape[0] and state[0] + 1 >= 0):
        return (state[0] + 1, state[1])
    else:
        return None
    
def top(state: Tuple[int, int]) -> Tuple[int, int] | None:
    # valid initial state
    assert(state[0] >= 0 and state[0] < board.shape[0]) # X axis
    assert(state[1] >= 0 and state[1] < board.shape[1]) # Y axis
    if (state[0] - 1 < board.shape[0] and state[0] - 1 >= 0):
        return (state[0] - 1, state[1])
    else:
        return None
    
# Exploration de l'espace en fonction des actions disponibles
# On "sait" que l'espace est petit, on peut "donc" faire tous les parcours possibles
all_actions = [
    top,
    bottom,
    right,
    left
]
all_pathes = np.ndarray(shape = (board.shape[0], board.shape[1], len(all_actions)), dtype = int)
all_pathes.fill(0)
all_pathes_visit = np.ndarray(shape = (board.shape[0], board.shape[1], len(all_actions)), dtype = bool)
all_pathes_visit.fill(False)
# initialState = (0, board.shape[1] - 1)
initialState = (0, 0)
cpt = 0
def compute(state):
    global cpt
    for action_index in range(0, len(all_actions)):
        action = all_actions[action_index]
        next_state = action(state)
        if next_state is not None and not all_pathes_visit[state[0], state[1], action_index]:
            value = board[next_state[0], next_state[1]]
            all_pathes[state[0], state[1], action_index] = value
            all_pathes_visit[state[0], state[1], action_index] = True
            compute(next_state)
            cpt = cpt + 1

compute(initialState)


