from sympy import *

# Function for integration
def integr(expr):
    try:
        return integrate(expr)
    except:
        return "Syntax error"
    
# Function for differentiation
def diffr(expr, symbol):
    try:
        return diff(expr, symbol)
    except:
        return "Syntax error"
    
#x = Symbol('x')
#print(diffr("x**12345678", x))
#print(integr("x"))