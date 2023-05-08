import pygame


# Part A
def threenp1(n) :

    count = 0

    while n > 1.0:
       count += 1

       if n % 2 == 0:
        n = int(n / 2)

       else:
        n = int(3 * n + 1)
    
    return count 

def threenp1range(upper_limit) :

    sequence = {}

    for x in range(2,upper_limit+1) :
       sequence[x] = threenp1(x)

    return sequence

# Part B
def graph_coordinates(threenplus1_iters_dict) :
    pygame.init()
    window = pygame.display.set_mode()
    threenplus1_iters_dict = threenp1range(threenplus1_iters_dict)
    pos = [(i,i2) for i, i2 in threenplus1_iters_dict.items()]

    pygame.draw.lines(window, "white", True, pos)
    
    new_display = pygame.transform.flip(window, False, True)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 10, height * 0.5))
    window.blit(new_display, (0, 0))

    max_so_far = (0,0)
    for x,y in pos :
        if y > max_so_far[1]:
          max_so_far = (x,y)

    font = pygame.font.Font(None,50)
    text = font.render("The max value is: "+str(max_so_far[1]), True, "white")
    window.blit(text, (760,540))
      
def main() :

    upper_limit = int(input("What would you like the upper limit to be?\n"))
    print(threenp1range(upper_limit))
    graph_coordinates(upper_limit)
    pygame.display.flip()
    pygame.time.wait(5000)

main()