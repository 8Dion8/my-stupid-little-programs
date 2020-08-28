var snek;


function setup() {
    createCanvas(800, 800);
    snek = new Snake()
}

function draw() {
    background(50);
    snek.show();
    snek.update();
    background(50);
    snek.show();
    snek.update();
    background(50);
    snek.show();
    snek.update();
    e();

}

function Snake() {
    this.coords = [
        [0, 0],
        [1, 0],
        [2, 0]
    ];
    this.head = [3, 0]
    this.xSpeed = 1;
    this.ySpeed = 0;
    this.update = function() {
        this.head[0] += this.xSpeed;
        this.head[1] += this.ySpeed;
        this.coords.shift();
        this.coords.push(this.head.splice());

    }
    this.show = function() {
        for (var i = 0; i < this.coords.length; i++) {
            rect(this.coords[i][0] * 10, this.coords[i][1] * 10, 10, 10)
        }
        rect(this.head[0] * 10, this.head[1] * 10, 10, 10)
    }
}
