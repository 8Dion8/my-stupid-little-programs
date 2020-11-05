import matplotlib.pyplot as plt
import numpy as np

x = [100,200,300,400,500]
y = [2,3,1.5,1,1]

y2 = [1,1,2,5,2]

plt.style.use("dark_background")

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.set_ylim(0,10)
ax1.bar(x, y, width=100,edgecolor="black")
ax1.set_title('Before')

plt.ylabel("f-density")
plt.xlabel("daily sales")

ax2.set_ylim(0,10)
ax2.bar(x,y2, width=100,edgecolor="black")
ax2.set_title('After')


plt.ylabel("f-density")
plt.xlabel("daily sales")
plt.show()