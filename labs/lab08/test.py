import random

def foo(width=109, pixels=10):
    return pixels*random.randint(0,int(width/pixels)-1)

for i in range(50):
    print(foo())
    
