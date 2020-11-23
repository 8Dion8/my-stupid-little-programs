#include <iostream>
#include <string>
using namespace std;

void print_grid(string grid) {
    cout << grid[0] << "|" << grid[1] << "|" << grid[2] << "|" << grid[3] << "|" << grid[4];
    cout << "------------------";
    cout << grid[5] << "|" << grid[6] << "|" << grid[7] << "|" << grid[8] << "|" << grid[9];
    cout << "------------------";
    cout << grid[10] << "|" << grid[11] << "|" << grid[12] << "|" << grid[13] << "|" << grid[14];
    cout << "------------------";
    cout << grid[15] << "|" << grid[16] << "|" << grid[17] << "|" << grid[18] << "|" << grid[19];
    cout << "------------------";
    cout << grid[20] << "|" << grid[21] << "|" << grid[22] << "|" << grid[23] << "|" << grid[24];
}

int check_win(string grid) {
    for (int w = 0; w < 5; ++w) {
        if (grid[w*5] == grid[w*5+1] == grid[w*5+2] == grid[w*5+3] == grid[w*5+4]) {
            if (grid[w*5] == 'X') {
                return -10;
            } else {
                return 10;
            }
        
        }
    }
    for (int w = 0; w < 5; ++w) {
        if (grid[w] == grid[w+5] == grid[w+10] == grid[w+15] == grid[w+20]) {
            if (grid[w] == 'X') {
                return -10;
            } else {
                return 10;
            }
        }
    }
    int empty_spaces = 0;
    for (int i = 0; i < 25; ++i) {
        if (grid[i] != 'X' and grid[i] != 'O') {
            ++empty_spaces;
        }
    }
    if (empty_spaces == 0) {
        return 0;
    } else {
        return 3;
    }
}

int minimax(string grid, int depth, bool isMaximizing) {
    int result = check_win(grid);
    if (result != 3) {
        return result;
    }
    if (isMaximizing) {
        int best_score = -100;
        for (int i = 0; i < 25; ++i) {
            if (grid[i] != 'X' and grid[i] != 'O') {
                grid[i] = 'O';
                int score = minimax(grid,depth+1,false);
                grid[i] = to_string(i);
                best_score = max(score, best_score);
            }
        }
        return best_score;
    } else {
        int best_score = 100;
        for (int i = 0; i < 25; ++i) {
            if (grid[i] != 'X' and grid[i] != 'O') {
                grid[i] = 'X';
                int score = minimax(grid,depth+1,true);
                grid[i] = to_string(i);
                best_score = min(score, best_score);
            }
        }
        return best_score;
    }
}

int get_best_move(string grid) {
    int best_score = -100;
    int score;
    int best_move;
    for (int i = 0; i < 25; ++i) {
        if (grid[i] != 'X' and grid[i] != 'O') {
            grid[i] = 'O';
            score = minimax(grid,0,false);
            grid[i] = i;
            if (score > best_score) {
                best_score = score;
                best_move = i;
            }
        }
    }
    return best_move;
}

int main() {
    string grid = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"};
    int place;
    while (true) {
        print_grid(grid);
        cout << "Where do you want your X?\n";
        cin >> place;
        grid[place] = 'X';
        if (check_win(grid) != 3) {
            return 0;
        }
        grid[get_best_move(grid)] = 'O';
        if (check_win(grid) != 3) {
            return 0;
        }
    }
}