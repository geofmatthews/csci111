
def initialize():
    return 1,2,3,4

def process(tupe):
    a,b,c,d = tupe
    a = 2*a
    b = 2*b
    c = 2*c
    d = 2*d
    return (a,b,c,d)

tupe = initialize()
print(tupe)
tupe = process(tupe)
print(tupe)
tupe = initialize()
print(tupe)
