from math import radians, log10, log, sin, cos, tan, sinh, cosh, tanh, acos, asin, atan, acosh, asinh, atanh, factorial


def evaluation(expr):
    # To evaluate basic expressions
    try:
        result = eval(expr)
        return result
    except:
        return "Syntax error"
    

def modulo(expr, mod):
    try:
        return expr%mod
    except:
        return "Syntax Error"

    
def fact(n):
    try:
        return factorial(n)
    except:
        return "Math Error"

    
def trig_fxn(trig, expr):
    expr = float(expr)
    try:
        # Check which trigonometric / hyperbolic function to use
        if trig == "sin":
            result = sin(radians(expr))
            return result
        elif trig == "cos":
            result = cos(radians(expr))
            return result
        elif trig == "tan":
            result = tan(radians(expr))
            return result
        elif trig == "sinh":
            result = sinh(radians(expr))
            return result
        elif trig == "cosh":
            result = cosh(radians(expr))
            return result
        elif trig == "tanh":
            result = tanh(radians(expr))
            return result
        elif trig == "asin":
            result = asin(radians(expr))
            return result
        elif trig == "acos":
            result = acos(radians(expr))
            return result
        elif trig == "atan":
            result = atan(radians(expr))
            return result
        elif trig == "asinh":
            result = asinh(radians(expr))
            return result
        elif trig == "acosh":
            result = acosh(radians(expr))
            return result
        elif trig == "atanh":
            result = atanh(radians(expr))
            return result
        elif trig == "log":
            result = log10(expr)
            return result
        elif trig == "ln":
            result = log(expr, 2.718)
        
    except:
        return "Syntax error"

