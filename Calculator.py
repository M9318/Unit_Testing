def add(x,y):              #Function to add two number x & y
    return x+y

def sub(x,y):              #Function to subtract two number x & y
    return x-y

def multi(x,y):            #Function to multiplay two number x & y
    return x*y

def div(x,y):              #Function to divided two number if y = 0 it return invalid operation 
    if ( y == 0):
         raise ValueError('Can not divide by zero!')
    else:
        return x/y    

def modulas(x,y):          #Function to find modulas of  two number x & y
    return x % y
