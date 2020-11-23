choice = ['m','b','s','d','d']

e = 0

from itertools import permutations

perms = permutations(choice)

for i in perms:
    if i[0] == 'b' or i[0] == 'm':
        
        for j in range(len(i)):
            if i[j] == 'd':
                try:
                    if i[j+1] != 'd':
                        print(i)
                        e += 1
                    else:
                        break
                except:break


print(e)