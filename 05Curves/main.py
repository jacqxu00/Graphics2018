from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

body_color = [ 255, 255, 255 ]
parse_file( 'eve', edges, transform, screen, body_color )
