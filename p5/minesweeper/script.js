document.oncontextmenu = function() { return false; }

const height_ = 10;
const width_ = 20;
const size_ = 1200 / width_;
var rightPressed = false;

function setup() {
    cnv = createCanvas(1200, 600);
    cells = new Grid(width_, height_);
    textSize(1200 / width_);
    stroke(255);
}

function draw() {
    background(0);
    cells.show();


}

function mouse_pressed() {
    console.log(mouseButton);

}

function mouseReleased() {
    let x_pos = Math.floor(mouseX / size_);
    let y_pos = Math.floor(mouseY / size_);
    if (mouseButton === LEFT) {
        try {
            cells.reveal(x_pos, y_pos);
        } catch (error) {}
    }
    if (mouseButton === RIGHT) {
        console.log(x_pos, y_pos);
        try {
            if (cells.zero_grid[x_pos][y_pos] != 1) {
                cells.zero_grid[x_pos][y_pos] = Math.abs(cells.zero_grid[x_pos][y_pos]) - 1;
            }
        } catch (error) {}
    }
    let collumn = [];
    for (let i = 0; i < width_; i++) {
        collumn = cells.zero_grid[i];
    }
}