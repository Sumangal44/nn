# AND 
import numpy as np


def step(x):
    return 1 if x >= 0 else 0


def neuron(x, w, b):
    return step(np.dot(w, x) + b)


def AND(x):
    w = np.array([1, 1])
    b = -1.5
    return neuron(x, w, b)


inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

for x in inputs:
    print(f"AND({x[0]}, {x[1]}) = {AND(np.array(x))}")