import random

def randomColumn(width=100, cellSize=10):
    return cellSize*random.randint(0,int(width/cellSize)-1)

cellSize = 8
width = cellSize*5 + 3
for i in range(0, int(width/cellSize)):
    print(cellSize*i)



    
