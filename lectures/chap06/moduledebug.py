import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result    

# The following code will be run if this module is run
# It will NOT be run if theis module is imported
if __name__ == '__main__':
    print(distance(0,0,3,4), 'should be', 5)
    print(distance(3,4,0,0), 'should be', 5)
    print(distance(1,1,4,5), 'should be', 5)
    print(distance(0,0,6,8), 'should be', 10)
