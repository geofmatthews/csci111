import math

class Function():
    '''an object to store a function and x,y,z ranges'''
    def __init__(self, function, xrange, yrange, zrange):
        self.function = function
        self.xrange = xrange
        self.yrange = yrange
        self.zrange = zrange

zero = Function(lambda x,y : 0.0, (-1, 1), (-1, 1), (-1,1))
sincos= Function(lambda x,y : math.sin(x)*math.cos(y),
                 (-2*math.pi, 2*math.pi),
                 (-2*math.pi, 2*math.pi),
                 (-1,1)
                 )
sind = Function(lambda x,y : math.sin(math.sqrt(x**2+y**2)),
                 (-2*math.pi, 2*math.pi),
                 (-2*math.pi, 2*math.pi),
                 (-1,1)
                 )

                        
cosd = Function(lambda x,y : math.cos(math.sqrt(x**2 + y**2)),
                 (-2*math.pi, 2*math.pi),
                 (-2*math.pi, 2*math.pi),
                 (-1,1)
                 )

cosd2 = Function(lambda x,y : math.cos(x**2 + y**2)/math.sqrt(x**2+y**2+1),
                 (-1*math.pi, 1*math.pi),
                 (-1*math.pi, 1*math.pi),
                 (-0.5,1)
                 )

def mandelbrot(x0,y0):
    x = 0.0
    y = 0.0
    iteration = 0
    max_iteration = 1000
    while (x*x + y*y <= 4) and iteration < max_iteration:
        xtemp = x*x - y*y + x0
        y = 2*x*y + y0
        x = xtemp
        iteration += 1
    return iteration/max_iteration

mand = Function(mandelbrot, (-2,0.5), (-1.5,1.5), (0,1))

def functions():
    '''return all the functions we've defined'''
    return [zero, sincos, sind, cosd, cosd2, mand]

