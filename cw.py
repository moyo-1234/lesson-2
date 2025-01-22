import pgzrun
from random import randint

#game wi ndow
HEIGHT = 250
WIDTH = 250



#0-255
#0-255
#0-255

def draw():
    r = 255
    g = 0
    b = randint(0,255)

    width = WIDTH
    height = HEIGHT - 150

    for i in range(20):
        rect = Rect((0,0) , (width ,height))
        rect.center = 150,150
        screen.draw.rect(rect, (r,g,b))
        width -= 10
        height += 10


pgzrun.go()