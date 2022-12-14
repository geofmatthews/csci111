

from functions import *
from vector import V
from gradient import Gradient
from polygon import Polygon

def lerp(x, a, b, c, d):
    return ((x-a)/(b-a))*(d-c) + c

class ParametricSurface():
    def __init__(self, func, n):
        self.func = func.function
        self.n = n
        self.xrange = func.xrange
        self.yrange = func.yrange
        self.gradient = Gradient(func.zrange)
        self.makeHeightfield()

    def makeHeightfield(self):
        """calculate nxn 3d points in xrange x yrange
           store V(x,y,z) in self.heightfield[i,j]
           precondition:  initialized:
               self.func
               self.xrange
               self.gradient
               self.n
           postcondition: initialized:
               self.heightfield
           """
        pass

    def projectPoints(self, eye):
        """project 3d points in heightfield to
              2d points (x,y) in plane of camera
              store in self.points[i,j]
           also calculate for these points
              self.minx, maxx, miny, maxy
           also calculate color based on gradient and height and normal
              store in self.color[i,j]
           also calculate eye distance
              store in self.distance[i,j]
           precondition: initialized:
               self.heightfield
           postcondition: initialized:
               self.points
               self.distance
               self.color
               self.xmin, xmax, ymin, ymax
        """
        pass

    def normal(self, i, j):
        """find normal to surface at self.heightfield[i,j]
           use cross product of vectors from [i,j] to [i+1,j]
           and from [i,j] to [i,j+1]
        """
        pass
       
    def scale(self, size):
        '''loop over all the points in all the polygons
           lerping their x,y from minx,maxx and miny,maxy ranges
           into screen size ranges, flipping y
           optional: first shrink the screen range 10% if you like
           modifies points in place
           precondition: initialized:
               self.points
               self.xmin, xmax, ymin, ymax
           postcondition: initialized:
               self.points
        '''
        pass
          
    def makePolygons(self, eye, size):
        """
           then build polygons from self.points, self.color, self.distance
           using [i,j], [i+1,j], [i+1,j+1], [i,j+1] indices
           then sort the polygons based on distance (farthest first)
           precondition: initialized:
               self.heightfield
           postcondition: initialized:
               self.polygons
        """
        self.projectPoints(eye)
        self.scale(size)
  
        ## The following enables this project to run before it is
        ## finished and is only for demonstration purposes.
        ## DELETE the following after you finish this function:
        self.polygons = [Polygon([(100,100), (200,100), (200,200), (100,200)],
                                 '#0000ff',
                                 1.0),
                         Polygon([(150,150), (250,150), (250,250), (150,250)],
                                 '#ff0000',
                                 2.0)
                         ]
        
   
                
        
        
        
        
        
            
