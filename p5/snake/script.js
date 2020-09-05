var snek;
var running = true;
var score = 0;



function setup() {
    createCanvas(1380, 810);
    snek = new Snake();
    fod = new Food();
    textSize(32);

}

function draw() {
    if (running) {
        if (keyIsDown(UP_ARROW) && snek.ySpeed != 1) {
            snek.xSpeed = 0;
            snek.ySpeed = -1;
        } else if (keyIsDown(DOWN_ARROW) && snek.ySpeed != -1) {
            snek.xSpeed = 0;
            snek.ySpeed = 1;
        } else if (keyIsDown(RIGHT_ARROW) && snek.xSpeed != -1) {
            snek.xSpeed = 1;
            snek.ySpeed = 0;
        } else if (keyIsDown(LEFT_ARROW) && snek.xSpeed != 1) {
            snek.xSpeed = -1;
            snek.ySpeed = 0;
        }
        background(0);
        snek.show();

        if (fod.x == snek.head[0] && fod.y == snek.head[1]) {
            snek.coords[snek.coords.length] = snek.head.slice(0, 2);
            snek.head = fod.coor.slice(0, 2)
            fod.update();
            ++score;

        } else {
            snek.update();
        }

        fod.show();
        text(score, 10, 30);
        fill(255);
        if (0 > snek.head[0] || snek.head[0] > 138) {
            console.log(snek.head[0], 'first')
            running = false;
        } else if (0 > snek.head[1] || snek.head[1] > 81) {
            console.log(snek.head[1], 'second')
            running = false;
        } else if (snek.coords.includes(snek.head)) {
            console.log(snek.head, snek.coords, 'third')
            running = false;
        }
    } else {
        textSize(128);
        background(0);
        text(score, 650, 300);
        fill(255);

        if (0 < snek.head[0] < 1380 || 0 < snek.head[1] < 810) { running = false; }
    }
}

function Snake() {
    this.coords = [
        [0, 0],
        [1, 0],
        [2, 0]
    ];
    this.head = [3, 0];
    this.xSpeed = 1;
    this.ySpeed = 0;
    this.update = function() {
        this.coords.shift();
        this.coords[this.coords.length] = this.head.slice(0, 2);
        this.head[0] += this.xSpeed;
        this.head[1] += this.ySpeed;

    }
    this.show = function() {
        for (var i = 0; i < this.coords.length; i++) {
            rect(this.coords[i][0] * 10, this.coords[i][1] * 10, 10, 10);
        }
        rect(this.head[0] * 10, this.head[1] * 10, 10, 10);

    }
}

function Food() {
    this.x = getRandomInt(137);
    this.y = getRandomInt(80);
    this.coor = [this.x, this.y];


    this.update = function() {
        this.x = getRandomInt(137);
        this.y = getRandomInt(80);
        this.coor = [this.x, this.y];

    }

    this.show = function() {
        rect(this.x * 10, this.y * 10, 10, 10);
    }
}

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}