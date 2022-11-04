import math
class V:
    """ simple 3d vectors """

    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        x = str(self.x)
        y = str(self.y)
        z = str(self.z)
        return 'V(' + x + ', ' + y + ', ' + z + ')'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return V(x,y,z)

    def __mul__ (self, c):
        x = c * self.x
        y = c * self.y
        z = c * self.z
        return V(x,y,z)

    def __truediv__(self, c):
        return self.__mul__(1/c)

    def __rmul__(self, c):
        return self.__mul__(c)

    def __xor__(self, other):
        """ dot product """
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return (x+y+z)

    def norm(self):
        n = math.sqrt(self ^ self)
        self.x = self.x/n
        self.y = self.y/n
        self.z = self.z/n
        return v

    def tuple(self):
        return (self.x, self.y, self.z)


if __name__ == '__main__':
    v = V(1,2,3)
    print(v)
    print(v+v)
    print(3*v)
    print(v*4)
    print(v/10)
    root3 = math.sqrt(3)
    w = V(root3, root3, root3)
    print(w ^ w)
    u = V(3, 4, 0)
    print(u ^ u)
    v.norm()
    print(v)
    print(v ^ v)

    v = V(2,4)
    print(v)
    print(v^v)
        
