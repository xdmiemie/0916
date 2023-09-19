import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.power(x-1,2)
def dy(f, x, delta = 0.00001):
    return (f(x + delta) - f(x - delta)) / (2*delta)
lr = 0.1
xinit= 10.0
x1 = xinit
e = 0.01
print(x1)
while f(x1) > e:
    dy1 = dy(f,x1)
    x1 = x1 - lr * dy1
    print(x1)




