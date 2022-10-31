"""
https://www.edureka.co/blog/snake-game-with-pygame/

Improved(?) by Geoffrey Matthews, 2022
"""

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
displayWidth = 600
displayHeight = 400
 
dis = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Modified Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
cellSize = 10
speed = 8
 
gameOverFont = pygame.font.SysFont("bahnschrift", 25)
scoreFont = pygame.font.SysFont("comicsansms", 35)

def show_score(score):
    value = scoreFont.render("Your Score: " + str(score),
                              antialias = True,
                              color = yellow)
    dis.blit(value, [0, 0])
 
def show_snake(block_pixels, snake_list):
    for x in snake_list:
        pygame.draw.circle(dis, black, [x[0], x[1]], block_pixels)
 
def message(msg, color):
    mesg = gameOverFont.render(msg, True, color)
    dis.blit(mesg, [dis_width // 6, dis_height // 3])
 
def initialize():
    gameOver = False
    gameClose = False
 
    x1 = displayWidth // 2
    y1 = displayHeight // 2
 
    x1Change = 0
    y1Change = 0
 
    snakeList = []
    Length_of_snake = 1
 
    foodx = cellSize*random.randint(0,int(displayWidth/cellSize - 1))
    foody = cellSize*random.randint(0,int(displayHeight/cellSize - 1))

def gameLoop():
    while not gameOver:
 
        while gameClose == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -cellSize
                    y1Change = 0
                elif event.key == pygame.K_RIGHT:
                    x1Change = cellSize
                    y1Change = 0
                elif event.key == pygame.K_UP:
                    y1Change = -cellSize
                    x1Change = 0
                elif event.key == pygame.K_DOWN:
                    y1Change = cellSize
                    x1Change = 0
 
        if x1 >= displayWidth or x1 < 0 or y1 >= displayHeight or y1 < 0:
            gameClose = True
        x1 += x1Change
        y1 += y1Change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)

    
 
if __name__ == '__main__':
    try:
        gameLoop()
    finally:
        pygame.quit()
        
