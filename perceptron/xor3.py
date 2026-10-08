import numpy as np


# Unit Step Function
def step(x):
    return 1 if x >= 0 else 0


# Perceptron
def perceptron(x, weights, bias):
    value = np.dot(weights, x) + bias
    return step(value)


# NOT Gate
def NOT(x):
    weight = -1
    bias = 0.5
    return perceptron(x, weight, bias)


# AND Gate
def AND(x):
    weights = np.array([1, 1])
    bias = -1.5
    return perceptron(x, weights, bias)


# OR Gate
def OR(x):
    weights = np.array([1, 1])
    bias = -0.5
    return perceptron(x, weights, bias)


# XOR Gate
# XOR = AND(OR(x), NOT(AND(x)))
def XOR(x):
    a = AND(x)
    b = OR(x)
    c = NOT(a)

    return AND(np.array([b, c]))


# Test XOR Gate
tests = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]


for x in tests:
    result = XOR(np.array(x))
    print(f"XOR({x[0]}, {x[1]}) = {result}")