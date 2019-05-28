import math

#print the matrix so rows are vertical
def print_matrix( matrix ):
    for c in range(len(matrix[0])):
        row_str = ""
        for r in range(len(matrix)):
            val = matrix[r][c]
            if val < 10:
                row_str += "    "+str(val)
            elif val < 100:
                row_str += "   "+str(val)
            else:
                row_str += "  "+str(val)
        print row_str
    print ""

#print the matrix so rows are horizontal
def print_matrix_2( matrix ):
    for r in matrix:
        row_str = ""
        for c in r:
            if c < 10:
                row_str += "    "+str(c)
            elif c < 100:
                row_str += "   "+str(c)
            else:
                row_str += "  "+str(c)
        print row_str
    print ""


#returns a new identity matrix
def ident( matrix ):
    ident = []
    for r in range(4):
        ident.append([])
        for c in range(4):
            if r==c:
                ident[r].append(1)
            else:
                ident[r].append(0)
    return ident

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #can't multiply if the m1 cols != m2 rows
    if len(m1[0]) != len(m2):
        print "Matrix multiplication impossible with these 2 matrices."
        pass

    #populate ans matrix
    ans = new_matrix( len(m1), len(m2[0]))
    for r in range( len(ans) ):
        for c in range( len(ans[0]) ):
            for i in range( len(m2) ):
                ans[r][c] += m1[r][i] * m2[i][c]

    #transfer ans to m2
    for r in range( len(ans) ):
        for c in range( len(ans[0]) ):
            m2[r][c] = ans[r][c]

#returns a new matrix
def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m


#def grow_matrix(matrix, new_rows):
#    temp = []
#    for r in range( len(matrix)+new_rows ):
#        m.append( [] )
#        for c in range( rows ):
#            m[r].append( 0 )
#    matrix = temp
