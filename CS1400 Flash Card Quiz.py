import pygame
pygame.init()
window = pygame.display.set_mode((800, 600))

#rectangles and variables
NRect = pygame.Rect(697, 531, 0,0).inflate(100,50)
BRect = pygame.Rect(85, 531, 0,0).inflate(100,50)
rect1 = pygame.Rect(*window.get_rect().center, 0, 0).inflate(350, 200)
run = True
clock = pygame.time.Clock()
state = 1
BigState = 0

#list of components
comps = []

while run:
    clock.tick(60)
    event = pygame.event.wait()    

    mousePos = pygame.mouse.get_pos()#gets mouseposition everytime the loop runs
    if event.type == pygame.QUIT: #close game window
        run = False#quits loop
        break
        
    #Sets up font to use for text
    font = pygame.font.Font(None, 65)
    headerFont = pygame.font.Font(None, 45)
    
    window.fill(100)#fills window with a specific color
    if BigState == 0:#makes one big state that will be "review" before the quiz
        collide = rect1.collidepoint(mousePos)#collision with main rectangle(flash card)

        #draws the next and back buttons using rect functions
        #checks if the mouse is in the rectangles and if the user is clicking a mouse button
        if NRect.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
            state += 1#increments state by 1
            if state > 3:#if greater than a certain value revert to first state
                state = 1
        if BRect.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
            state -=1#decrements state by 1
            if state < 1:#if less than a certain value revert to last state
                state = 3
        back = headerFont.render(str("BACK"),1,(0,0,0))
        next = headerFont.render(str("NEXT"),1,(0,0,0))
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
            text = font.render(str("BYE"),1, (255,255,255)) if collide else font.render(str("HI"),1,(0,0,0))
            pygame.draw.rect(window, color, rect1)
            window.blit(text, (rect1))
        if state == 2:
            text = font.render(str("THERE"),1, (255,255,255)) if collide else font.render(str("WOA"),1,(0,0,0))
            pygame.draw.rect(window, color, rect1)
            window.blit(text, (rect1))
        if state == 3:
            text = font.render(str("COMPONENT"),1, (255,255,255)) if collide else font.render(str("CPU"),1,(0,0,0))
            pygame.draw.rect(window, color, rect1)
            window.blit(text, (rect1))

    if BigState == 1:#big state that holds the quiz
        pygame.draw.rect(window, (255,0,255), (0,0,100,100))
    pygame.display.flip()#allows everything to be drawn on screen
pygame.quit()
exit()
