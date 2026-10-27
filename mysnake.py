from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

def draw_board():
    noir = (0, 0, 0)
    screen.fill(noir)
    for c in range(30):
        for l in range(30):
            if c%2==0 and l%2==0:
                x, y = c*20,l*20
                width, height = 20, 20     # largeur et hauteur, en pixels
                color = (255, 255, 255)        
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, color, rect) 
            if c%2==1 and l%2==1:
                x, y = c*20,l*20
                width, height = 20, 20     # largeur et hauteur, en pixels
                color = (255, 255, 255)        
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, color, rect)
    pg.display.update()

SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]

def draw_snake(snake):
    for x,y in snake:
        color=(255,0,0)
        width, height = 20, 20
        rect = pg.Rect(x*20, y*20, width, height)
        pg.draw.rect(screen, color, rect)
    pg.display.update()


def move_snake(snake, direction):
    x_d, y_d=direction
    snake2=snake
    x_t, y_t=snake[-1]
    snake2.append((x_t+x_d, y_t+y_d))
    snake2.pop(0)
    return snake2

DIRECTION = (1, 0)

running =True
while running:
    clock.tick(2)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running=False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                DIRECTION= (0,-1)
            elif event.key == pg.K_DOWN:
                DIRECTION= (0,1)
            elif event.key == pg.K_LEFT:
                DIRECTION= (-1,0) 
            elif event.key == pg.K_RIGHT:
                DIRECTION= (1,0)   
        
    draw_board()
    draw_snake(SNAKE)
    move_snake(SNAKE,DIRECTION)

#3.3 : le serpent disparait lorsqu'il atteint le bord de la fenêtre



