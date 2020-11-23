from PIL import Image
from numpy import transpose, array_equal, array
import copy

ima = Image.open('/Users/glebsvarcer/Desktop/my-stupid-little-programs/maze_solver/maze3.png')

og = ima.load()


matrix = []

#print(og)

row = []

for pix_row_index in range(ima.size[0]):
    row = []
    for pix_column_index in range(ima.size[1]):
        print(og[pix_row_index,pix_column_index])
        try:
            row.append(og[pix_row_index,pix_column_index][0]//128*255)
        except TypeError:
            row.append(og[pix_row_index,pix_column_index]//128*255)
    if 0 in row or (0,0,0) in row or (0,0,0,255) in row:
        matrix.append(row)

print(matrix)

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


final_matrix = copy.deepcopy(transpose(final_matrix))
print(final_matrix)

for row in range(len(final_matrix)):
    #print(row)
    for column in range(len(final_matrix[row])):
        pix = final_matrix[row][column]
        #print("Pix:",pix)
        pixs[column,row] = (pix,pix,pix)

for i in final_matrix:
    for j in i:
        if j == 0:
            print(chr(9633),end='')
        else:
            print(' ', end='')
    print()

#final_ima = new_ima.rotate(270).transpose(Image.FLIP_LEFT_RIGHT)
#final_ima.show()

new_ima.show()

new_ima.save('cleaned_up.png')

print('Start:', final_matrix[0])
