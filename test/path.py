e = 0

from math import factorial

def find_path(depth,x,y):
    
    if depth == 15:
        if x == 6 and y == 8:
            print('Found')
            global e 
            e += 1
    else:
        find_path(depth + 1, x + 1, y)
        find_path(depth + 1, x, y + 1)

find_path(1,0,0)

print(e)

print(factorial(14)//(factorial(8)*factorial(6)))

print(factorial(9)/(factorial(3)*factorial(6))*(factorial(6)/(factorial(3)*factorial(3)))*(factorial(3)/(factorial(3)*factorial(0))))