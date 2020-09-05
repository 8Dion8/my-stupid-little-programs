const height_ = 20;
const width_ = 40;
const size_ = 1200 / width_;

function setup() {
    createCanvas(1200, 600);
    cells = new Grid(width_, height_);
    textSize(1200 / width_);
    stroke(255);
}

function draw() {
    background(0);
    cells.show();
}


class Grid {
    constructor(w, h) {
        this.grid = [];
        this.choices = [0, 0, 0, 0, 0, 0, 0, 1];
        var collumn = [];
        var cell = 0;
        var zero_collumn = [];
        this.zero_grid = [];
        for (var x = 0; x < w; ++x) {
            collumn = [];
            zero_collumn = [];
            for (var y = 0; y < h; ++y) {
                cell = this.choices[Math.floor(Math.random() * this.choices.length)];
                collumn.push(cell);
                zero_collumn.push(0);
            }
            this.grid.push(collumn);
            this.zero_grid.push(zero_collumn);
        }

        this.neighbor_grid = [];

        for (var x = 0; x < w; ++x) {
            for (var y = 0; y < h; ++y) {

            }
        }

        this.show = function() {
            let neighbors;
            for (var x = 0; x < w; ++x) {
                for (var y = 0; y < h; ++y) {
                    if (this.zero_grid[x][y]) {
                        cell = this.grid[x][y];
                        fill(255 * cell, 0, 0);
                        rect(x * size_, y * size_, size_, size_);
                        neighbors = this.get_neighbors(x, y);
                        if (cell == 0 && neighbors > 0) {
                            fill(255);
                            text(neighbors, x * size_ + size_ / 4, y * size_ + size_ * 0.8);
                        }
                    } else {
                        fill(0, 255, 0);
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
            try {
                cell = this.grid[left][y]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            try {
                cell = this.grid[left][top]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            try {
                cell = this.grid[x][top]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            try {
                cell = this.grid[right][top]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            try {
                cell = this.grid[right][y]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            try {
                cell = this.grid[right][bottom]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            try {
                cell = this.grid[x][bottom]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            try {
                cell = this.grid[left][bottom]
                if (cell == 1) {++neighbors; }
            } catch (error) {}
            return neighbors
        }
    }
}

function mouseClicked() {
    let x_pos = Math.floor(mouseX / size_);
    let y_pos = Math.floor(mouseY / size_);
    cells.zero_grid[x_pos][y_pos] = 1;
}