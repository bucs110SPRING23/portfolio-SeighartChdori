import pygame
import random
import math

#Part A
# Screen and Target

pygame.init()

boxes = {
    "Player1" : pygame.Rect(0, 0, 50, 50),
    "Player2" : pygame.Rect(1870, 0, 50, 50)
}


while 1 :
    pygame.event.pump()

    window = pygame.display.set_mode()
    screen = pygame.display.get_window_size()

    window.fill("blue")
    pygame.draw.circle( window , "red" , [screen[0]/2,screen[1]/2] , screen[1]/2)
    pygame.draw.rect( window, "green", boxes["Player1"])
    pygame.draw.rect( window, "purple", boxes["Player2"])
    pygame.draw.line( window , "black" , [screen[0]/2,0] , [screen[0]/2,screen[1]] , width = 3)
    pygame.draw.line( window , "black" , [screen[0]/2-screen[1]/2,screen[1]/2] , [screen[0]/2+screen[1]/2,screen[1]/2] , width = 3)

    pygame.display.flip()
    break

pygame.time.wait(2000)

# Dart Betting
blank = None
while (blank is None) :
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boxes["Player1"].collidepoint(event.pos):
                blank = "Player1"
            if boxes["Player2"].collidepoint(event.pos):
                blank = "Player2"

# Dart Throwing
point = 0
point1 = 0
for x in range(10) :
    dart = [random.randrange(screen[0]),random.randrange(screen[1])]
    dart2 = [random.randrange(screen[0]),random.randrange(screen[1])]
    distance_from_center = math.hypot(screen[0]/2-dart[0],screen[1]/2-dart[1])
    distance_from_center2= math.hypot(screen[0]/2-dart2[0],screen[1]/2-dart2[1])
    is_in_circle = distance_from_center <= screen[1]/2
    is_in_circle2 = distance_from_center2 <= screen[1]/2

    if is_in_circle:
        pygame.draw.circle( window , "green" , dart , 12.5)
        point+=1
    else :
        pygame.draw.circle( window , "black" , dart , 12.5)
    
    pygame.display.flip()
    pygame.time.wait(500)
    
    if is_in_circle2:
        pygame.draw.circle( window , "purple" , dart2 , 12.5)
        point1+=1
    else :
        pygame.draw.circle( window , "black" , dart2 , 12.5)
    
    pygame.display.flip()
    pygame.time.wait(500)

pygame.time.wait(1000)

# Winner
font = pygame.font.Font(None,100)
textfail = font.render("User Guess is Wrong" , True , "White")
textpass = font.render("User Guess is Correct" , True , "White")

if point == point1 :
    text = font.render("It's a tie" , True , "White")
    window.blit(text , (760,540))
    window.blit(textfail , (570,440))
    pygame.display.flip()
    pygame.time.wait(1000)

elif point > point1 :
    text = font.render("Green wins" , True , "White")
    window.blit(text , (760,540))
    if blank == "Player1" :
        window.blit(textpass , (570,440))
    else :
        window.blit(textfail , (570,440))
    pygame.display.flip()
    pygame.time.wait(1000)

elif point < point1 :
    text = font.render("Purple wins" , True , "White")
    window.blit(text , (760,540))
    if blank == "Player2" :
        window.blit(textpass , (570,440))
    else :
        window.blit(textfail , (570,440))
    pygame.display.flip()
    pygame.time.wait(1000)