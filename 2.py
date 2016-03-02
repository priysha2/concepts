def max_of_three(x,y,z):
    if  ((x>y)&(x>z)):
        print("%d is greater than %d and %d" %(x,y,z))
    elif ((y>x) & (y>z)):
        print("%d is greater than %d and %d" % (y,x,z))
    else:
        print("%d is largest of %d and %d" %(z,x,y))
        
max_of_three(20,40,10)        