# 25 x 25 grid with 5 random squares
# each having a 50% reprogus chance and 50% death chance

import pygame
import random 

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sim.py")

GREY = (150, 150, 150)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

RADIUS = 25
FPS = 1

BIRTHRATE = 2
DEATHRATE = 5

red_dots = [[250, 100,], [100, 100,], [400, 100,]]
green_dots = [[250, 250,], [100, 250,], [400, 250,]]
blue_dots = [[250, 400,], [100, 400,], [400, 400,]]


def draw_window():
    WIN.fill(GREY)


    red_dead = 0
    for i in range(len(red_dots)):
        # death
        if random.randint(1,DEATHRATE) == 1:
            red_dots.pop(i-red_dead)
            red_dead += 1
        else:
            pygame.draw.circle(WIN, RED, (red_dots[i-red_dead][0], red_dots[i-red_dead][1]), RADIUS)
            
        # birth
        if random.randint(1,BIRTHRATE) == 1:
            red_dots.append([random.randint(0, 500), random.randint(0, 500)])
    

    green_dead = 0
    for i in range(len(green_dots)):
        # death
        if random.randint(1,DEATHRATE) == 1:
            green_dots.pop(i-green_dead)
            green_dead += 1
        else:
            pygame.draw.circle(WIN, GREEN, (green_dots[i-green_dead][0], green_dots[i-green_dead][1]), RADIUS)
            
        # birth
        if random.randint(1,BIRTHRATE) == 1:
            green_dots.append([random.randint(0, 500), random.randint(0, 500)])
    
    blue_dead = 0
    for i in range(len(blue_dots)):
        # death
        if random.randint(1,DEATHRATE) == 1:
            blue_dots.pop(i-blue_dead)
            blue_dead += 1
        else:
            pygame.draw.circle(WIN, BLUE, (blue_dots[i-blue_dead][0], blue_dots[i-blue_dead][1]), RADIUS)
            
        # birth
        if random.randint(1,BIRTHRATE) == 1:
            blue_dots.append([random.randint(0, 500), random.randint(0, 500)])

    print('red:', len(red_dots), 'green:', len(green_dots), 'blue:', len(blue_dots))
    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == '__main__':
    main()
