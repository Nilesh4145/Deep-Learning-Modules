import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import math
X1 = [60.1826, 86.30855]
X2 = [0.051267, 0.69956]

def fun(x, y):
  return math.log(1+ math.exp(x*X1[0] + y*X1[1]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 10
xs = np.linspace(0, 1, 50)
ys = np.linspace(0, 1, 50)
zs = [fun(x, y) for x,y in zip(xs,ys)]

ax.plot(xs, ys, zs)

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')


plt.show()

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