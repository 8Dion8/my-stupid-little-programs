def print_grid(grid):
    print(grid[0],'|',grid[1],'|',grid[2],'|',grid[3],'|',grid[4])
    print('------------------')
    print(grid[5],'|',grid[6],'|',grid[7],'|',grid[8],'|',grid[9])
    print('------------------')
    print(grid[10],'|',grid[11],'|',grid[12],'|',grid[13],'|',grid[14])
    print('------------------')
    print(grid[15],'|',grid[16],'|',grid[17],'|',grid[18],'|',grid[19])
    print('------------------')
    print(grid[20],'|',grid[21],'|',grid[22],'|',grid[23],'|',grid[24])
'''
def check_win(grid):
    if grid[0] == grid[1] == grid[2]:
        return -10 if grid[0] == 'X' else 10
    elif grid[3] == grid[4] == grid[5]:
        return -10 if grid[3] == 'X' else 10
    elif grid[6] == grid[7] == grid[8]:
        return -10 if grid[6] == 'X' else 10
    elif grid[0] == grid[3] == grid[6]:
        return -10 if grid[0] == 'X' else 10
    elif grid[4] == grid[1] == grid[7]:
        return -10 if grid[1] == 'X' else 10
    elif grid[8] == grid[5] == grid[2]:
        return -10 if grid[2] == 'X' else 10
    elif grid[0] == grid[4] == grid[8]:
        return -10 if grid[0] == 'X' else 10
    elif grid[6] == grid[4] == grid[2]:
        return -10 if grid[2] == 'X' else 10
    empty_spaces = 0
    for i in grid:
        if i != 'X' and i != 'O':
            empty_spaces += 1
    if empty_spaces == 0:
        return 0
    else:
        return None
'''

def check_win(grid):
    for w in range(5):
        if grid[w*5] == grid[w*5+1] == grid[w*5+2] == grid[w*5+3] == grid[w*5+4]:
            return -10 if grid[w*5] == 'X' else 10
    for w in range(5):
        if grid[w] == grid[w+5] == grid[w+10] == grid[w+15] == grid[w+20]:
            return -10 if grid[w] == 'X' else 10
    if grid[0] == grid[6] == grid[12] == grid[18] == grid[24]:
        return -10 if grid[0] == 'X' else 10
    if grid[4] == grid[8] == grid[12] == grid[16] == grid[20]:
        return -10 if grid[4] == 'X' else 10
    empty_spaces = 0
    for i in grid:
        if i != 'X' and i != 'O':
            empty_spaces += 1
    if empty_spaces == 0:
        return 0
    else:
        return None
def minimax(grid, depth, isMaximizing):
    result = check_win(grid)
    if result != None:
        score = result
        return score
    if isMaximizing:
        best_score = -100
        for i in grid:
            if i != 'X' and i != 'O':
                grid[i] = 'O'
                score = minimax(grid,depth+1,False)
                grid[i] = i
                best_score = max((score, best_score))
        return best_score
    else:
        best_score = 100
        for i in grid:
            if i != 'X' and i != 'O':
                grid[i] = 'X'
                score = minimax(grid,depth+1,True)
                grid[i] = i
                best_score = min((score, best_score))
        return best_score




def get_best_move(grid):
    best_score = -100
    for i in grid:
        if i != 'X' and i != 'O':
            grid[i] = 'O'
            score = minimax(grid, 0, False)
            grid[i] = i
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

grid = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
while True:
    print_grid(grid)
    grid[int(input('Where do you want your x?'))] = 'X'
    print_grid(grid)
    if check_win(grid) != None:
        break
    grid[get_best_move(grid)] = 'O'
    if check_win(grid) != None:
        break

#grid = ['O','O',2,'X','X',5,'X',7,8]
#print(get_best_move(grid))



