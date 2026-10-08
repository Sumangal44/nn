import numpy as np


# Activation function
def step(x):
    return 1 if x >= 0 else 0


# Hidden neuron 1
def hidden_neuron1(x):
    w = np.array([1, 1])
    b = -0.5
    return step(np.dot(w, x) + b)


# Hidden neuron 2
def hidden_neuron2(x):
    w = np.array([-1, -1])
    b = 1.5
    return step(np.dot(w, x) + b)


# Output neuron
def output_neuron(h1, h2):
    w = np.array([1, 1])
    b = -1.5
    return step(np.dot(w, [h1, h2]) + b)


# XOR Neural Network
def XOR(x):
    h1 = hidden_neuron1(x)
    h2 = hidden_neuron2(x)

    return output_neuron(h1, h2)


# Test
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

for x in inputs:
    result = XOR(np.array(x))
    print(f"XOR({x[0]}, {x[1]}) = {result}")