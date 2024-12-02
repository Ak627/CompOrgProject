#_______________________________________________________________________
# Flash Card Quiz in Python
# Author: Alexander Kindall CS1400 Team 5 (Alex, Sam, Dawson, and Brian)
#_______________________________________________________________________
import pygame
import random
import time
pygame.init()
window = pygame.display.set_mode((800, 600))


def blit_text(surface, text, pos, font, rectangle):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = (rectangle.width, rectangle.height)
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, (0,0,0))
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width + 200:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.





#rectangles and variables
NRect = pygame.Rect(697, 531, 0,0).inflate(100,50)
BRect = pygame.Rect(85, 531, 0,0).inflate(100,50)
rect1 = pygame.Rect(*window.get_rect().center, 0, 0).inflate(350, 200)
RedRect = pygame.Rect(window.get_rect().width/2, window.get_rect().height/2+250, 0,0).inflate(120, 50)
run = True
clock = pygame.time.Clock()
state = (random.randrange(0,6)+1)


while run:
    clock.tick(60)
    event = pygame.event.wait()    

    mousePos = pygame.mouse.get_pos()#gets mouseposition everytime the loop runs
    if event.type == pygame.QUIT: #close game window
        run = False#quits loop
        break
    
    #Sets up font to use for text
    font = pygame.font.Font(None, 30)
    headerFont = pygame.font.Font(None, 45)
    
    window.fill(100)#fills window with a specific color
    collide = rect1.collidepoint(mousePos)#collision with main rectangle(flash card)

    #draws the next and back buttons using rect functions
    #checks if the mouse is in the rectangles and if the user is clicking a mouse button
    if NRect.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        state += 1#increments state by 1
        if state > 6:#if greater than a certain value revert to first state
            state = 1
    if BRect.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        state -=1#decrements state by 1
        if state < 1:#if less than a certain value revert to last state
            state = 6
    back = headerFont.render(str("BACK"),1,(0,0,0))
    next = headerFont.render(str("NEXT"),1,(0,0,0))
    ready = headerFont.render(str("READY"),1,(0,0,0))
    pygame.draw.rect(window, (255,255,255), NRect)
    pygame.draw.rect(window, (255,255,255), BRect)
    window.blit(back,(BRect))
    window.blit(next, (NRect))
    color = (150, 100, 150) if collide else (200, 255, 200)

    header = headerFont.render(str("Hover on card to see answer!"),1,(0,0,0))
    cardNum = headerFont.render(str(state),1,(0,0,0))
    Title = headerFont.render(str("Flash Card Quiz!(CPU COMPOPNENTS)"),1,(0,0,0))
    window.blit(Title, (0,0))
    window.blit(header,(200,153))
    window.blit(cardNum,(380,420))
    if state == 1:#if state is a certain value, different things will show on the screen
        text = ("ALU(Arithmetic Logic Unit)") if collide else ("Processes data and instructions from the memory unit, and stores the results in primary memory")
        
        pygame.draw.rect(window, color, rect1)
        blit_text(window, text, (rect1.x, rect1.y), font, rect1)
        
    if state == 2:
        text = ("CU(Control Unit)") if collide else ("Collects data from the input unit, processes it, and presents the output to the user")
        
        pygame.draw.rect(window, color, rect1)
        blit_text(window, text, (rect1.x, rect1.y), font, rect1)
        
    if state == 3:
        text = ("IR(Instruction Register)") if collide else ("Holds each instruction after it is fetched from memory")
        
        pygame.draw.rect(window, color, rect1)
        blit_text(window, text, (rect1.x, rect1.y), font, rect1)
        
    if state == 4:
        text = ("Cache") if collide else ("An essential component of CPU architecture that helps bridge the gap between processing power and main memory access latency")
        
        pygame.draw.rect(window, color, rect1)
        blit_text(window, text, (rect1.x, rect1.y), font, rect1)
    
    if state == 5:
        text = ("Register") if collide else ("One of a small set of data holding places that are part of the computer processor")
        
        pygame.draw.rect(window, color, rect1)
        blit_text(window, text, (rect1.x, rect1.y), font, rect1)

    if state == 6:
        text = ("Buses") if collide else ("A collection of signal lines that enable the flow of electrical impulses between components of the computer")
        
        pygame.draw.rect(window, color, rect1)
        blit_text(window, text, (rect1.x, rect1.y), font, rect1)
        
    
        
        
    pygame.display.flip()#allows everything to be drawn on screen
pygame.quit()
exit()
