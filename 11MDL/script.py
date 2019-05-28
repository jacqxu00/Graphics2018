import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],#[0,191,255]]
             [0,
              255,
              255]]
    areflect = [0.1,
                0.1,
                0.1]
    dreflect = [0.5,
                0.5,
                0.5]
    sreflect = [0.5,
                0.5,
                0.5]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )
    polygons=[]
    systems = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    edges=[]
    step_3d = 20

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
        for args in commands:
            line = args[0]

            if line == 'sphere':
                add_sphere(polygons,float(args[1]), float(args[2]), float(args[3]),float(args[4]), step_3d)
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []

            elif line == 'torus':
                add_torus(polygons,float(args[1]), float(args[2]), float(args[3]),float(args[4]), float(args[5]), step_3d)
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []

            elif line == 'box':
                add_box(polygons,float(args[1]), float(args[2]),float(args[3]), float(args[4]), float(args[5]), float(args[6]))
                matrix_mult( systems[-1], polygons )
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []


            elif line == 'line':
                add_edge( edges,float(args[1]), float(args[2]), float(args[3]),float(args[4]), float(args[5]), float(args[6]) )
                matrix_mult( systems[-1], edges )
                draw_lines(edges, screen, zbuffer, color)
                edges = []

            elif line == 'scale':
                t = make_scale(float(args[1]), float(args[2]), float(args[3]))
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]

            elif line == 'move':
                t = make_translate(float(args[1]), float(args[2]), float(args[3]))
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]

            elif line == 'rotate':
                theta = float(args[2]) * (math.pi / 180)
                if args[1] == 'x':
                    t = make_rotX(theta)
                elif args[1] == 'y':
                    t = make_rotY(theta)
                else:
                    t = make_rotZ(theta)
                matrix_mult( systems[-1], t )
                systems[-1] = [ x[:] for x in t]

            elif line == 'push':
                systems.append( [x[:] for x in systems[-1]] )

            elif line == 'pop':
                systems.pop()

            elif line == 'display':
                display(screen)

            elif line == 'save':
                save_extension(screen, args[1]+args[2])

    else:
        print "Parsing failed."
        return
