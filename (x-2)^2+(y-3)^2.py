import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.power(x-2,2) + np.power(y-3,2)
def dx(f, x, y, delta = 0.00001):
    return  (f(x + delta, y) - f(x - delta, y)) / (2*delta)
def dy(f, x, y, delta = 0.00001):
    return  (f(x , y + delta) - f(x , y + delta)) / (2*delta)
lr = 0.1
xinit = yinit = 10.0
x1 = xinit
y1 = xinit
maxl = 30
for i in range(maxl):
    dx1 = dx(f, x1, y1)
    x1 = x1 - lr * dx1
    dy1 = dx(f, x1, y1)
    y1 = y1 - lr * dy1
    print("x = " , x1)
    print("y = " , y1)