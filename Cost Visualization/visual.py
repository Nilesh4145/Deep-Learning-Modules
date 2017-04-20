'''
Author : Nilesh Chaturvedi
Last Updated : 20th April, 2017

Description: This code plots the cost function of linear and logistic regression for one point and varying theta's.
'''

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
X1 = [60.1826, 86.30855]
X2 = [0.051267, 0.69956]

def logistic(x, y, X, Y):
	return math.log(1+ math.exp(x*X + y*Y))

def linear(x, y, X, Y):
	bias = 5
	return (x*X + y*Y -1) ** 2

xs = np.linspace(0, 1, 100)
ys = np.linspace(0, 1, 100)
z1 = [logistic(x, y, X1[0], X1[1]) for x,y in zip(xs,ys)]
z2 = [logistic(x, y, X2[0], X2[1]) for x,y in zip(xs,ys)]
z3 = [linear(x, y, X2[0], X2[1]) for x,y in zip(xs,ys)]

plt.figure()

plt.subplot(221, projection='3d')
plt.plot(xs, ys, z1, label = "Logistic Regression with point : [60.1826, 86.30855]")
plt.title('Logistic Regression with dataset 1')
plt.grid(True)

plt.subplot(222, projection='3d')
plt.plot(xs, ys, z2, label = "Logistic Regression with point : [0.051267, 0.69956]")
plt.title('Logistic Regression with dataset 2')
plt.grid(True)

plt.subplot(223, projection='3d')
plt.plot(xs, ys, z3, label = "Linear Regression with point : [0.051267, 0.69956]")
plt.title('Linear Regression with dataset 2')
plt.grid(True)

plt.show()