

def two(f):
    f()
    f()
def four(f):
    two(f)
    two(f)
    
def plus():
    print('+',end=' ')

def dash():
    print('-',end=' ')

def bar():
    print('/',end=' ') # this is easier to change to |

def space():
    print(' ',end=' ')

def half_beam():
    plus()
    four(dash)

def beam():
    two(half_beam)
    plus()
    print()

def half_strut():
    bar()
    four(space)

def strut():
    two(half_strut)
    bar()
    print()

def half_box():
    beam()
    four(strut)

def box():
    two(half_box)
    beam()

box()

    
