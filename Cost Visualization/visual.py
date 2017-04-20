import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import math
X1 = [60.1826, 86.30855]
X2 = [0.051267, 0.69956]

def logit(x, y, X, Y):
	return math.log(1+ math.exp(x*X + y*Y))

def linear(x, y, X, Y):
	bias = 5
	return x*X + y*Y + bias

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax2 = fig.add_subplot(121, projection='3d')
ax3 = fig.add_subplot(222, projection='3d')
n = 10
xs = np.linspace(0, 1, 50)
ys = np.linspace(0, 1, 50)
z1 = [logit(x, y, X1[0], X1[1]) for x,y in zip(xs,ys)]
z2 = [logit(x, y, X2[0], X2[1]) for x,y in zip(xs,ys)]
z3 = [linear(x, y, X2[0], X2[1]) for x,y in zip(xs,ys)]

ax1.plot(xs, ys, z1, label = "Logistic Regression with dataset 1")
ax2.plot(xs, ys, z2, label = "Logistic Regression with dataset 2")
ax3.plot(xs, ys, z3, label = "Linear Regression with dataset 2")

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')



plt.savefig("new.pdf")

# import math
# import numpy
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# X1 = [60.1826, 86.30855]
# X2 = [0.051267, 0.69956]

# x1 = numpy.linspace(0, 1, 100)
# x2 = numpy.linspace(0, 1, 100)

# funct_logit_1 = math.log(1+ math.exp(x1*X1[0] + x2*X1[1]))

# funct_logit_1 = math.log(1+ math.exp(x1*X2[0] + x2*X2[1]))

# fig = plt.figure()

# ax = fig.add_subplot(111, projection = '3D')

# Axes3D.plot(x1, x2, funct_logit_1)

# plt.show()