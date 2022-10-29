import turtle
bob = turtle.Turtle()

def star(t,n,trips):
    angle = trips*360/(n)
    for i in range(n):
        t.fd(100)
        t.lt(angle)


star(bob,23,7)
