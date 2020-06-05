def check_win(grid):
    if grid[0] == grid[1] == grid[2]:
        return 1 if grid[0] == 'X' else -1
    elif grid[3] == grid[4] == grid[5]:
        return 1 if grid[3] == 'X' else -1
    elif grid[6] == grid[7] == grid[8]:
        return 1 if grid[6] == 'X' else -1
    elif grid[0] == grid[3] == grid[6]:
        return 1 if grid[0] == 'X' else -1
    elif grid[4] == grid[1] == grid[7]:
        return 1 if grid[1] == 'X' else -1
    elif grid[8] == grid[5] == grid[2]:
        return 1 if grid[2] == 'X' else -1
    elif grid[0] == grid[4] == grid[8]:
        return 1 if grid[0] == 'X' else -1
    elif grid[6] == grid[4] == grid[2]:
        return 1 if grid[0] == 'X' else -1
    else:
        for i in grid:
            if i != 'X' and i != 'O':
                return None
    return 0

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
                score = minimax(grid, depth + 1,False)
                grid[i] = i
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 100
        for i in grid:
            if i != 'X' and i != 'O':
                grid[i] = 'X'
                score = minimax(grid, depth + 1, True)
                grid[i] = i
                if score < best_score:
                    best_score = score
        return best_score

            



def get_best_move(grid):
    best_score = -100
    for i in grid:
        if i != 'X' and i != 'O':
            grid[i] = 'O'
            score = minimax(grid, 0, True)
            grid[i] = i
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
        
print(get_best_move([0,'X',2,3,4,5,6,7,8]))