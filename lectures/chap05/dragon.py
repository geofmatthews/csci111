import turtle

bob = turtle.Turtle()


def ccurve(t, level):
    d = 5
    if level <= 0:
        t.fd(d)
    else:
        t.lt(45)
        ccurve(t,level-1)
        t.rt(90)
        ccurve(t,level-1)
        t.lt(45)

def dragon(t, level, left=True):
    d = 5
    if level <= 0:
        t.fd(d)
    elif left:
        t.lt(45)
        dragon(t, level-1, True)
        t.rt(90)
        dragon(t, level-1, False)
        t.lt(45)
    else:
        t.rt(45)
        dragon(t, level-1, True)
        t.lt(90)
        dragon(t, level-1, False)
        t.rt(45)
        

        
bob.speed(0)

for i in range(12,13):
    bob.penup()
    bob.setpos(-128,0)
    bob.pendown()
    bob.clear()
    dragon(bob, i, True)
    input('Press enter for level ' + str(i+1) + ' dragon:')
    

