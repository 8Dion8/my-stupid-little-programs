from PIL import Image
from numpy import transpose, array_equal, array
import copy
import sys
sys.setrecursionlimit(1000000)

ima = Image.open('/Users/glebsvarcer/Desktop/my-stupid-little-programs/maze_solver/big4.png')

og = ima.load()


matrix = []

#print(og)

row = []

for pix_row_index in range(ima.size[0]):
    row = []
    for pix_column_index in range(ima.size[1]):
        try:
            row.append(og[pix_row_index,pix_column_index][0]//128*255)
        except TypeError:
            row.append(og[pix_row_index,pix_column_index]//128*255)
    if 0 in row or (0,0,0) in row or (0,0,0,255) in row:
        matrix.append(row)


new_matrix = transpose(matrix)
second_matrix = []
for row in new_matrix:
    if 0 in row or (0,0,0) in row or (0,0,0,255) in row:
        second_matrix.append(row)

#print(matrix)

third_matrix = []

previous_row = []

for row in second_matrix:
    if not array_equal(row, previous_row):
        third_matrix.append(row)
        previous_row = copy.deepcopy(row)



fourth_matrix = transpose(third_matrix)

final_matrix = []

for row in fourth_matrix:
    if not array_equal(row, previous_row):
        final_matrix.append(row)
        previous_row = copy.deepcopy(row)

new_ima = Image.new('RGB',[len(final_matrix),len(final_matrix[0])],color=(255,0,0))

pixs = new_ima.load()


final_matrix = copy.deepcopy(transpose(final_matrix)).tolist()
#print(final_matrix)

for row in range(len(final_matrix)):
    #print(row)
    for column in range(len(final_matrix[row])):
        pix = final_matrix[row][column]
        #print("Pix:",pix)
        pixs[column,row] = (pix,pix,pix)
'''
for i in final_matrix:
    for j in i:
        if j == 0:
            print(chr(9633),end='')
        else:
            print(' ', end='')
    print()
'''
#final_ima = new_ima.rotate(270).transpose(Image.FLIP_LEFT_RIGHT)
#final_ima.show()

new_ima.show()

new_ima.save('cleaned_up.png')


start = [0,final_matrix[0].index(255)]
end = [len(final_matrix)-1,final_matrix[-1].index(255)]

print('Start:', start)
print('End:',end)

final_matrix[start[0]][start[1]] = 2

def search(x, y, path):
    if final_matrix[x][y] == 2:
        path.append([x,y])
        return True, path

    elif final_matrix[x][y] == 0:
        return False, path

    elif final_matrix[x][y] == 3:
        return False, path

    #print ('visiting %d,%d' % (x, y))
    final_matrix[x][y] = 3
    path.append([x,y])
    '''
    for i in range(len(final_matrix)):
        for j in range(len(final_matrix[i])):
            cell = final_matrix[i][j]

            if [i,j] in path:
                print(end='*')
            elif cell == 0:
                print(chr(9633),end='')
            else:
                print(end=' ')
        print()
    '''

    if x != 0:
        result, path = search(x-1,y, path)
        if result == True:
            return True, path
    if y != 0:
        result, path = search(x,y-1, path)
        if result == True:
            return True, path

    if x != len(final_matrix)-1:
        result, path = search(x+1,y, path)
        if result == True:
            return True, path

    if y != len(final_matrix[0])-1:
        result, path = search(x,y+1, path)
        if result == True:
            return True, path
    path.pop()
    return False, path


result, path = search(end[0], end[1], [])


#for i in final_matrix:
    #print(i)

#print(path)
'''
for x in range(len(final_matrix)):
    for y in range(len(final_matrix[x])):
        cell = final_matrix[x][y]

        if [x,y] in path:
            print(end='*')
        elif cell == 0:
            print(chr(9633),end='')
        else:
            print(end=' ')
    print()
'''
final_ima = Image.new(mode='RGB',size=(len(final_matrix)+10,len(final_matrix[0])+10))

final_pixs = final_ima.load()

gradient = []

for i in range(256):
    for j in range(256):
        if i % 2 == 0:
            gradient.append([j,i,128])
        else:
            gradient.append([255-j,i,128])

#print(gradient)

#tuple(gradient[step%(256*256)])

step = 0
for row in range(len(final_matrix)):
    for column in range(len(final_matrix[0])):
        cell = final_matrix[row][column]

        if cell == 0:
            final_pixs[row,column] = (0,0,0)
        else:
            final_pixs[row,column] = (255,255,255)
        

for i in path:
    final_pixs[i[0],i[1]] = tuple(gradient[int(step//1)%(256)])
    step += 256/len(path)
final_ima = final_ima.rotate(270).transpose(Image.FLIP_LEFT_RIGHT)

final_ima.save('final.png')

final_ima.show()
