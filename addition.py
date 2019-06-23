
# 2019-06-23 prime prove


def addition(a, b):
    """ Routine che fa la somma. """
    return a + b

# dichiaro una variabile e assegno un intero
somma = 34
#print(somma)

# somma di interi con test
somma = addition(2, 2)
#print(somma)
assert somma == 4

somma = addition(5, 3)
print(somma)
assert somma == 8

somma = addition(-5, 5) 
#print(somma)
assert somma == 0

# addition of two strings instead of integers
somma = addition("pippo", "pluto")
#print(somma)

# same, but using floats
somma = addition(1.50, 2.25)
#print(somma)
