from src.Game import Game
import numpy as np
# https://github.com/ramonhagenaars/nptyping
from nptyping import NDArray, Shape, Int
from typing import TypeVar, Generic, Tuple

# DimX = TypeVar('DimX') 
# DimY = TypeVar('DimY')
# ValueType = TypeVar('ValueType')


class Game2D(Game):
    """An implementation of a 2D game
    
    Each position is a state
    """

    
    def __init__(self, board: NDArray[Shape['N, M'], Int]):
        self.board = board
        pass

    def valueOf(self, state: Tuple[int, int]) -> float | None:
        if (2 != len(state)):
            print("Dimensions mismatches")
            return None
        return self.board[state]

