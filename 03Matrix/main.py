from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
print_matrix(matrix)
for each in range(100):
    add_edge(matrix, 0, each*5, 0, 499, 499-each*5, 0)
for each in range(100):
    add_edge(matrix, each*5, 0, 0, 499-each*5, 499, 0)
add_edge(matrix, 0, 499, 0, 499, 0, 0)
draw_lines( matrix, screen, color )
print_matrix(matrix)
ident = ident(matrix)
print_matrix(ident)
matrix_mult(ident, matrix)
print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)
