import pygame
pygame.init()

screen = pygame.display.set_mode() 
dimensions = screen.get_size() #Takes the resolution of your screen
starting_point = [dimensions[0] // 2, dimensions[1] // 2] #Dimensions is a list [1980,1080] 

radius = 100
for _ in range(3):
    pygame.draw.circle(screen , "red" , starting_point , radius) #pygame.draw.circle(location,color,starting point,radius)
    starting_point[1] = starting_point[1] - radius*1.5
    radius = radius // 2

pygame.display.flip()
pygame.time.wait(2000)
