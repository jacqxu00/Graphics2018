from display import *

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
