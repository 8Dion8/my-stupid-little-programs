import pygame as p
import neat, time, os, random

WINDOW_WIDTH = 600
WINDOW_WIDTH = 800
RUNNING = True

BIRD_IMGS = [p.transform.scale2x(p.image.load("/Users/glebsvarcer/Desktop/my-stupid-little-programs/neat/flappy_bird/imgs/bird1.png")), 
             p.transform.scale2x(p.image.load("/Users/glebsvarcer/Desktop/my-stupid-little-programs/neat/flappy_bird/imgs/bird2.png")), 
             p.transform.scale2x(p.image.load("/Users/glebsvarcer/Desktop/my-stupid-little-programs/neat/flappy_bird/imgs/bird3.png"))]

PIPE_IMG = p.transform.scale2x(p.image.load("/Users/glebsvarcer/Desktop/my-stupid-little-programs/neat/flappy_bird/imgs/pipe.png"))
BASE_IMG = p.transform.scale2x(p.image.load("/Users/glebsvarcer/Desktop/my-stupid-little-programs/neat/flappy_bird/imgs/base.png"))
BG_IMG = p.transform.scale2x(p.image.load("/Users/glebsvarcer/Desktop/my-stupid-little-programs/neat/flappy_bird/imgs/bg.png"))


class Birb:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.velocity = -10
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        displacement = self.velocity * self.tick_count + 1.5 * self.tick_count ** 2

        if displacement >= 16:
            displacement = 16

        if d < 0:
            d -= 2

birb = Birb()
while RUNNING:
    birb.move()
