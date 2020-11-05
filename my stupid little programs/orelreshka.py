import matplotlib.pyplot as plt
from random import randint
hh = [0,0,0]
for i in range(1000):
    one = randint(1, 2)
    two = randint(1, 2)
    if one != two:
        hh[2] += 1
    elif one == 1:
        hh[0] += 1
    else:
        hh[1] += 1
print(hh)
plt.bar([1,2,3],hh)
plt.xlabel("hh                                   tt                                   ht")
plt.show()