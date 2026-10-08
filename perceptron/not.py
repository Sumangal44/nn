# NOT
import numpy as np



# Unit Step Function
def step(x):
    return 1 if x >= 0 else 0


# Perceptron
def neuron(x, w, b):
    return step(np.dot(w, x) + b)


# NOT Gate
def NOT(x):
    w = -1
    b = 0.5

    return neuron(x, w, b)


# Test NOT Gate
inputs = [0, 1]

for x in inputs:
    print(f"NOT({x}) = {NOT(x)}")