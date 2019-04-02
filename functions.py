# syntax
def funchtion_name(parameters):
    pass

# Sample Functions
def evenOdd( x ): 
    if (x % 2 == 0): 
        print ("even")
    else: 
        print ("odd")

evenOdd(6046)
evenOdd(55)

def swap(x, y): 
    temp = x
    x = y
    y = temp

x = 2
y = 3
swap(x, y) 
print(x) 
print(y) 


# Python program to illustrate   
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  

# Python program to illustrate   
# *kargs for variable number of keyword arguments 
  
def myFun2(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun2(first ='Geeks', mid ='for', last='Geeks') 

# Python code to illustrate cube of a number   
# using labmda function  
    
cube = lambda x: x*x*x  
print(cube(7))  