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

running =True
while running:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running=False

    draw_board()


