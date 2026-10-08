import numpy as np


def step(x):
    return 1 if x >= 0 else 0


def XOR(x):
    # Hidden layer
    h1 = step(np.dot([1, 1], x) - 0.5)
    h2 = step(np.dot([-1, -1], x) + 1.5)

    # Output layer
    return step(np.dot([1, 1], [h1, h2]) - 1.5)


# Test XOR
for x in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    print(f"XOR({x[0]}, {x[1]}) = {XOR(np.array(x))}")