import numpy as np

x = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])

y = np.array([[0,0,1,1]]).T

weights = np.random.rand((3, 1))

def train():
    for iteration in range(10000):
        for p in range(4):
            z = np.dot(x[p], weights)
            sigmoid = 1/(1+np.exp(-z))
            error = y[p] - sigmoid
            sigmoidDerivative = sigmoid * (1 - sigmoid)
            delta = error * sigmoidDerivative
            dW = (delta * x[p])
            dW = np.array([dW]).T
            weights = weights + dW
    print("weight", weights)