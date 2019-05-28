#write into the file
def writer(fopen):
    
    #setup
    fopen.write('P3\n')
    fopen.write('500 500\n')
    fopen.write('255\n')
    
    #first half from yellow to white (r goes from 0 to 249)
    for r in range (0,250):
        for c in range (0,500):
            fopen.write('255 255 '+str(r)+'  ')
        fopen.write('\n')
    
    #second half from white to yellow (r goes from 249 to 0)
    for r in range (0,250):
        for c in range (0,500):
            fopen.write('255 255 '+str(249-r)+'  ')
        fopen.write('\n')

#open and close the file
def main():
    f = open('gradient.ppm','w')
    writer(f)
    f.close

#run code
main()
