from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]

def rand():
    return random.randint(0, 255)

for each in range(250):
    draw_line(250-each-1, 0, 250+each, 499, screen, [rand(), rand(), rand()])
for each in range(500):
    draw_line(0, each, 499, 499-each, screen, [rand(), rand(), rand()])
for each in range(250):
    draw_line(250-each-1, 499, 250+each, 0, screen, [rand(), rand(), rand()])

display(screen)
save_extension(screen, 'img.png')
