def koalas():
    print "koalas"

def sloths():
    return "sloths"

def capitalize(s):
    return s[0].upper() + s[1:]

def square_elements(a):
    for k,v in enumerate(a):
        a[k] = v*v

def return_square_elements(a):
    X = []
    for val in a:
        X.append(val*val) 
    return X
