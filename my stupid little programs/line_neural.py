import numpy as np
import matplotlib.pyplot as plt
import numpy as np


input_x_first = np.random.rand(50,1) * 100
input_y_first = np.random.rand(50,1) * 100
input_x_second = np.random.rand(50,1) * 100 + np.random.randint(-200,200)
input_y_second = np.random.rand(50,1) * 100 + np.random.randint(-200,200)
print()
plut = plt.scatter(input_x_first,input_y_first)
plit = plt.scatter(input_x_second,input_y_second)
plt.show()
labels = np.array([[1,
                    0,
                    0,
                    1,
                    1,
                    0,
                    1]])
labels = labels.reshape(7,1)

np.random.seed(42)
weights = np.random.rand(3,1)
bias = np.random.rand(1)
lr = 0.05

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

def is_higher(m,b,x,y):
    if m*x+b < y:
        return 0
    else:
        return 1

for epoch in range(25000):
    inputs = input_set
    XW = np.dot(inputs, weights)+ bias
    z = sigmoid(XW)
    error = z - labels
    print(error.sum())
    dcost = error
    dpred = sigmoid_derivative(z)
    z_del = dcost * dpred
    inputs = input_set.T
    weights = weights - lr*np.dot(inputs, z_del)
    
    for num in z_del:
        bias = bias - lr*num
    