           ## Function ##

# Simple function
# function with argument
# return type
# def is a reserved keyword

# user define function
 
def bikrom():
    print('Adatya is a computer science student')

bikrom() # call the function 

# function with argument:

def Sum(a,b):
    print(a+b)
n=10
n1=30
Sum(n, n1)

e=30
rr=70
Sum(e, rr)

def Sum(a,b=5):
    print(a+b)

Sum(20)
Sum(30,40)


# return type

def Add(a,b=5):
    c = a+b
    return c
output=Add(30,80)
print(output)
