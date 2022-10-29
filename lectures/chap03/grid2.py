
def two(f,x):
    f(x)
    f(x)
def four(f,x):
    two(f,x)
    two(f,x)
    
def put(x):
    print(x,end=' ')
    
def putln(x):     # this can be abstracted
    print(x)

def half_beam(x):
    put('+')
    four(put,'-')

def beam(x):
    two(half_beam,x)
    putln('+')

def half_strut(x):
    put('/')
    four(put,' ')

def strut(x):
    two(half_strut,x)
    putln('/')

def half_box(x):
    beam(x)
    four(strut,x)

def box(x):
    two(half_box,x)
    beam(x)
    
box('dummy')

    
