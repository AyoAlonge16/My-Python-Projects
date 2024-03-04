c = 5
def add (a, b):
    c = a + b
    return c
 
# will get an exception
x = add(12, 23)
 
# use global
 
def add (a, b):
    global c
    c = a + b
    return c

#if you want to set a value to a variable not declared inside the function
#or it is not a parameter, you will gwt an exception.


