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

n = 10
xs = np.linspace(0, 1, 50)
ys = np.linspace(0, 1, 50)
z1 = [logit(x, y, X1[0], X1[1]) for x,y in zip(xs,ys)]
z2 = [logit(x, y, X2[0], X2[1]) for x,y in zip(xs,ys)]
z3 = [linear(x, y, X2[0], X2[1]) for x,y in zip(xs,ys)]

plt.figure()

plt.subplot(221, projection='3d')
plt.plot(xs, ys, z1, label = "Logistic Regression with dataset 1")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.zlabel('Z')
plt.title('Logistic Regression with dataset 1')
plt.grid(True)

plt.subplot(222, projection='3d')
plt.plot(xs, ys, z2, label = "Logistic Regression with dataset 2")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.zlabel('Z')
plt.title('Logistic Regression with dataset 2')
plt.grid(True)

plt.subplot(223, projection='3d')
plt.plot(xs, ys, z3, label = "Linear Regression with dataset 2")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.zlabel('Z')
plt.title('Linear Regression with dataset 2')
plt.grid(True)



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