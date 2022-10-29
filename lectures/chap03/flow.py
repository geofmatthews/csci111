

def f():
    print(1)
    i()
    g()
    i()
    print(2)

def g():
    print(3)
    h()
    i()
    h()
    print(4)

def h():
    print(5)
    i()
    print(6)

def i():
    print(7)
    
f()
