
def two(f):
    f()
    f()
def four(f):
    two(f)
    two(f)
    
def makeline(a,b):
    print(((a + b*4) * 2) + a)  # uses a powerful feature of python
    
def beam():
    makeline('+ ','- ')
    
def strut():
    makeline('/ ','  ')

def half_box():
    beam()
    four(strut)

def box():
    two(half_box)
    beam()

box()
