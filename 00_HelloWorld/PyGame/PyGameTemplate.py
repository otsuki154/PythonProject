import pygame
#Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (800, 600)  # width=800, heigh=600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
#Loop until the user clicks the close button
done = False
# Used to manage how fast then screen updates
clock = pygame.time.Clock()
rect_x = 50
# Main Programe Loop
while not done:
    #Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ---Game logic should go here
    screen.fill(WHITE)

   # pygame.draw.rect(screen, RED, [rect_x, 50, 50, 50])
    pygame.draw.ellipse(screen, GREEN, [rect_x, 50, 50, 50])
    rect_x += 1
    pygame.display.flip()  # de dao giua man hinh buffer va man hinh display
    clock.tick(60)  # 60 khung hinh/s

pygame.quit()
