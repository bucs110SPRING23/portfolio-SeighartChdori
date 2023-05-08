import random
import pygame
import math

#Part A

pygame.init()
window = pygame.display.set_mode()
screen = pygame.display.get_window_size()

window.fill("blue")
pygame.draw.circle( window , "red" , [screen[0]/2,screen[1]/2] , screen[1]/2)
pygame.draw.line( window , "black" , [screen[0]/2,0] , [screen[0]/2,screen[1]] , width = 3)
pygame.draw.line( window , "black" , [screen[0]/2-screen[1]/2,screen[1]/2] , [screen[0]/2+screen[1]/2,screen[1]/2] , width = 3)

pygame.display.flip()
pygame.time.wait(2000)

#Part B

for x in range(10) :
    dart = [random.randrange(screen[0]),random.randrange(screen[1])]
    distance_from_center = math.hypot(screen[0]/2-dart[0],screen[1]/2-dart[1])
    is_in_circle = distance_from_center <= screen[1]/2

    if is_in_circle:
        pygame.draw.circle( window , "green" , dart , 12.5)
    else :
        pygame.draw.circle( window , "black" , dart , 12.5)
    
    pygame.display.flip()
    pygame.time.wait(500)

pygame.time.wait(2000)