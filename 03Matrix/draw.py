from display import *
from matrix import *

#draws the lines based on the matrix of coordinates
def draw_lines( matrix, screen, color ):
    for c in range( len(matrix[0])/2 ):
        x0 = matrix[0][2*c]
        y0 = matrix[1][2*c]
        x1 = matrix[0][2*c+1]
        y1 = matrix[1][2*c+1]
        draw_line(x0, y0, x1, y1, screen, color)

#adds two points to the matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

#adds a point to the matrix
def add_point( matrix, x, y, z=0 ):
    for i in range(len(matrix)):
        if (i == 0):
            matrix[i].append(x)
        elif (i == 1):
            matrix[i].append(y)
        elif (i == 2):
            matrix[i].append(z)
        else:
            matrix[i].append(1)

#draws the lines based on two coordinates given
def draw_line( x0, y0, x1, y1, screen, color):
    # switch coordinates if from right to left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    A = y1 - y0
    B = x0 - x1
    x = x0
    y = y0

    # octant 1
    if (abs(B) >= abs(A) and A * B <= 0):
        d = 2 * A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    # octant 2
    elif (abs(A) >= abs(B) and A * B <= 0):
        d = A + 2 * B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    # octant 7
    elif (abs(A) >= abs(B) and A * B >= 0):
        d = A - 2 * B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B

    # octant 8
    elif (abs(B) >= abs(A) and A * B >= 0):
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
