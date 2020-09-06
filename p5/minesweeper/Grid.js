class Grid {
    constructor(w, h) {
        this.grid = [];
        this.choices = [0, 0, 0, 0, 0, 0, 0, 1];
        var collumn = [];
        var cell = 0;
        var zero_collumn = [];
        this.zero_grid = [];
        for (let x = 0; x < w; ++x) {
            collumn = [];
            zero_collumn = [];
            for (let y = 0; y < h; ++y) {
                cell = this.choices[Math.floor(Math.random() * this.choices.length)];
                collumn.push(cell);
                zero_collumn.push(0);
            }
            this.grid.push(collumn);
            this.zero_grid.push(zero_collumn);
        }



        this.show = function() {
            let neighbors;
            for (let x = 0; x < w; ++x) {
                for (let y = 0; y < h; ++y) {
                    if (this.zero_grid[x][y] == 1) {
                        cell = this.grid[x][y];
                        fill(255 * cell, 0, 0);
                        rect(x * size_, y * size_, size_, size_);
                        neighbors = this.get_neighbors(x, y)[0];
                        if (cell == 0 && neighbors > 0) {
                            fill(255);
                            text(neighbors, x * size_ + size_ / 4, y * size_ + size_ * 0.8);
                        }
                    } else if (this.zero_grid[x][y] == 0) {
                        fill(0, 255, 0);
                        rect(x * size_, y * size_, size_, size_);
                    } else {
                        fill(127, 127, 127);
                        rect(x * size_, y * size_, size_, size_);
                    }
                }
            }
        };
        this.get_neighbors = function(x, y) {
            let left = x - 1;
            let right = x + 1;
            let top = y - 1;
            let bottom = y + 1;
            var cell;
            var neighbors = 0;
            var neighbor_list = [];
            try {
                cell = this.grid[left][y];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);

            } catch (error) {}
            try {
                cell = this.grid[left][top];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);
            } catch (error) {}
            try {
                cell = this.grid[x][top];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);
            } catch (error) {}
            try {
                cell = this.grid[right][top];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);
            } catch (error) {}
            try {
                cell = this.grid[right][y];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);
            } catch (error) {}
            try {
                cell = this.grid[right][bottom];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);
            } catch (error) {}
            try {
                cell = this.grid[x][bottom];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);
            } catch (error) {}
            try {
                cell = this.grid[left][bottom];
                if (cell == 1) {++neighbors; }
                neighbor_list.push(cell);
            } catch (error) {}
            return [neighbors, neighbor_list];
        };

        this.neighbor_grid = [];
        var neighbors;


        for (let x = 0; x < w; ++x) {
            for (let y = 0; y < h; ++y) {
                neighbors = this.get_neighbors(x, y)[1];
                this.neighbor_grid.push(neighbors);
            }
        }
        this.reveal = function(x, y) {

            this.zero_grid[x][y] = 1;
            if (this.get_neighbors(x, y)[0] == 0) {
                console.log(x, y);
                this.floodFill(x, y);
            }
        };

        this.floodFill = function(x, y) {
            let left = x - 1;
            if (left < 0) {
                left = x;
            }
            let right = x + 1;
            if (right > width_) {
                right = x;
            }
            let top = y - 1;
            if (top < 0) {
                top = y;
            }
            let bottom = y + 1;
            if (bottom > height_) {
                bottom = y;
            }
            let cell;
            try {
                cell = this.grid[left][y];
                if (cell != 1 && this.zero_grid[left][y] != 1) {
                    this.reveal(left, y);
                }
            } catch (error) {}
            try {
                cell = this.grid[left][top];
                if (cell != 1 && this.zero_grid[left][top] != 1) {
                    this.reveal(left, top);
                }
            } catch (error) {}
            try {
                cell = this.grid[x][top];
                if (cell != 1 && this.zero_grid[x][top] != 1) {
                    this.reveal(x, top);
                }
            } catch (error) {}
            try {
                cell = this.grid[right][top];
                if (cell != 1 && this.zero_grid[right][top] != 1) {
                    this.reveal(right, top);
                }
            } catch (error) {}
            try {
                cell = this.grid[right][y];
                if (cell != 1 && this.zero_grid[right][y] != 1) {
                    this.reveal(right, y);
                }
            } catch (error) {}
            try {
                cell = this.grid[right][bottom];
                if (cell != 1 && this.zero_grid[right][bottom] != 1) {
                    this.reveal(right, bottom);
                }
            } catch (error) {}
            try {
                cell = this.grid[x][bottom];
                if (cell != 1 && this.zero_grid[x][bottom] != 1) {
                    this.reveal(x, bottom);
                }
            } catch (error) {}
            try {
                cell = this.grid[left][bottom];
                if (cell != 1 && this.zero_grid[left][bottom] != 1) {
                    this.reveal(left, bottom);
                }
            } catch (error) {}
        };
    }
}