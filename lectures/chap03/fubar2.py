
x = 11

def foo(y):
    z = 2*y
    print(x,y,z)
    bar(2*z)

def bar(x):
    y = 2*x
    print(x,y,z)

foo(x)
print(x,y,z)
