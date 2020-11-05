import matplotlib.pyplot as plt
import matplotlib.patches as pt
import numpy as np

x = np.array([[0,10],[10,15],[15,18],[18,22],[22,30]])
y = np.array([[32,32],[36,36],[30,30],[28,28],[26,26]])


for i in range(len(x)):
    f = x[i][1]-x[i][0]
    plt.bar(x[i][0] + f/2,y[i][0],width=f)
    #g = pt.Rectangle([x[i][0],0],x[i][1]-x[i][0],y[i][0])

plt.show()