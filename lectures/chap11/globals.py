
x = 10

def show_global():
    print(x)
show_global()
print(x)

def mod_global_bad():
    x = 20
    print(x)
mod_global_bad()
print(x)

def mod_global_good():
    global x
    x = 20
    print(x)
mod_global_good()
print(x)

