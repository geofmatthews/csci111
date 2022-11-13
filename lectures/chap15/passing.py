
def initialize():
    return 1,2,3,4

def process(a,b,c,d):
    a = 2*a
    b = 2*b
    c = 2*c
    d = 2*d
    return (a,b,c,d)

a,b,c,d = initialize()
print(a,b,c,d)
a,b,c,d = process(a,b,c,d)
print(a,b,c,d)
a,b,c,d = initialize()
print(a,b,c,d)
