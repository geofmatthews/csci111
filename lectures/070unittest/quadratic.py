import math

def quadratic(a, b, c):
    """Find the roots of the quadratic expression:
       a*x**2 + b*x + c == 0
       using the quadratic formula"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0.0:
        raise RuntimeError('negative discriminant')
    else:
        root1 = (-b - math.sqrt(discriminant))/(2*a)
        root2 = (-b + math.sqrt(discriminant))/(2*a)
        return root1, root2

if __name__ == '__main__':
    roots = quadratic(1,0,-1)
    assert roots == (-1, 1)
    roots = quadratic(1, 0, -4)
    assert roots == (-2, 2)
    roots = quadratic(1, -7, 12)
    assert roots == (3,4)
    roots = quadratic(2, 2, -12)
    assert roots == (-3,2)
    roots = quadratic(1,1,1)
                            
                                                
