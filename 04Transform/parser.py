from display import *
from matrix import *
from draw import *
import math

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
     line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    points = new_matrix()
    f = open(fname,'r')
    lines = f.readlines()

    for i in range(len(lines)):
        if (lines[i] == "line\n"):
            coors = lines[i+1].split(" ")
            x0 = int(coors[0])
            y0 = int(coors[1])
            z0 = int(coors[2])
            x1 = int(coors[3])
            y1 = int(coors[4])
            z1 = int(coors[5])
            add_edge(points, x0, y0, z0, x1, y1, z1)
            print "========== line =========="
            print_matrix(points)
        elif (lines[i] == "ident\n"):
            ident(transform)
            print "========== ident =========="
            print_matrix(transform)
        elif (lines[i] == "scale\n"):
            factor = lines[i+1].split(" ")
            x = int(factor[0])
            y = int(factor[1])
            z = int(factor[2])
            scale = make_scale(x, y, z)
            matrix_mult(scale, transform)
            print "========== scale =========="
            print_matrix(transform)
        elif (lines[i] == "move\n"):
            factor = lines[i+1].split(" ")
            x = int(factor[0])
            y = int(factor[1])
            z = int(factor[2])
            translate = make_translate(x, y, z)
            matrix_mult(translate, transform)
            print "========== move =========="
            print_matrix(transform)
        elif (lines[i] == "rotate\n"):
            param = lines[i+1].split(" ")
            direct = param[0]
            angle = int(param[1]) * math.pi / 180
            if (direct == "x"):
                rotate = make_rotX(angle)
            elif (direct == "y"):
                rotate = make_rotY(angle)
            else:
                rotate = make_rotZ(angle)
            matrix_mult(rotate, transform)
            print "========== rotate =========="
            print_matrix(transform)
        elif (lines[i] == "apply\n"):
            print "========== before apply =========="
            print_matrix(points)
            matrix_mult(transform, points)
            for c in range(len(points)):
                for r in range(len(points[0])):
                    points[c][r] = int(points[c][r])
            print "========== apply =========="
            print_matrix(points)
        elif (lines[i] == "display\n"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif (lines[i] == "save\n"):
            image = lines[i+1].split()
            save_extension(screen, image[0])
        else:
            pass
