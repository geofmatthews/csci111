

def two(f):
    f()
    f()
def four(f):
    two(f)
    two(f)
    
def beam():
    print('+ - - - - + - - - - +')

def strut():
    print('/         /         /')

def half_box():
    beam()
    four(strut)

def box():
    two(half_box)
    beam()

box()

    
