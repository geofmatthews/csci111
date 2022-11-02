
def initialize():
    global a,b,c,d
    a = 1
    b = 2
    c = 3
    d = 4

def process():
    global a,b,c,d
    a = 2*a
    b = 2*b
    c = 2*c
    d = 2*d

initialize()
print(a,b,c,d)
process()
print(a,b,c,d)
initialize()
print(a,b,c,d)
