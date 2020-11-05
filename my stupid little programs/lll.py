import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x = list(range(0,100000))
y = list(range(0,100000))
z = list(range(0,100000))

ax.scatter(x,y,z)

plt.show()