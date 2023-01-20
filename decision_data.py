
import random as rm
import numpy as np


moves = {0: [0,1], 1: [0,-1], 2: [1,0], 3: [-1,0]} # All possible moves
rf = np.array([5, 5, 5, 5]) # Initial Relative Frequencies/Probability of picking a move
ls = [0, 1, 2, 3]
chc = rm.choices(moves, weights=rf)[0]
print(chc)
