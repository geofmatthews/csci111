import math
### DO NOT NAME A FILE turtle.py !!!
import turtle
bob = turtle.Turtle()
alice = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def square2(t,length):
    for i in range(4):
        t.fd(length)
        t.rt(90)


def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
def circle (t, r):
    circumference = 2* math .pi*r
    n = max(int( circumference /5) , 5)
    polygon (t, n, circumference /n)

def arc (t, r, angle ):
    arc_length = 2 * math .pi * r * angle / 360
    n = max(int( arc_length / 3) , 1)
    step_length = arc_length / n
    step_angle = angle / n
    for i in range (n):
        t.fd( step_length )
        t.lt( step_angle )


def polyline (t, n, length , angle ):
    for i in range (n):
        t.fd( length )
        t.lt( angle )
    
def polygon2 (t, n, length ):
    angle = 360.0 / n
    polyline (t, n, length , angle )


def arc2 (t, r, angle ):
    arc_length = 2 * math .pi * r * angle / 360
    n = int( arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float ( angle ) / n
    polyline (t, n, step_length , step_angle )
    
def circle2 (t, r):
    arc (t, r, 360)


arc2(bob, 50, 90)
circle2(alice, 60)
