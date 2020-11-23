choice = ['a','b','c','d','e','f']

e = 0

from itertools import permutations

perms = permutations(choice)

for i in perms:
    for j in range(len(i)):
        if i[j] == 'a':
            try:
                if i[(j+1)%6] not in 'fd' and i[j-1] not in 'fd':
                    print(i)
                    e += 1
            except:pass

print(e)

