import pygame
import random

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
size = (800, 600)  # width=800, heigh=600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button
done = False
# Used to manage how fast then screen updates
clock = pygame.time.Clock()
rect_x = 50
background = WHITE
rectBg = RED

# Cấu hình font
font = pygame.font.SysFont("Courier New", 36)  # Chọn font và kích thước
# Tạo văn bản
text = "aaaaaa"
textOb = font.render(text, True, (255, 255, 255))  # Văn bản, chữ màu trắng

# Main Programe Loop
while not done:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if (mouse_x > 50) and (mouse_x < 100) and (mouse_y > 50) and (mouse_y < 100):
                    text = "Left click in rectangle"
                    textOb = font.render(text, True, WHITE)  # Văn bản, chữ màu trắng

                    background = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    print("background is: ", background)

                if not ((mouse_x > 50) and (mouse_x < 100) and (mouse_y > 50) and (mouse_y < 100)):
                    text = "Left click not in rectangle"
                    textOb = font.render(text, True, WHITE)  # Văn bản, chữ màu trắng

                    rectBg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    print("Rectangle background is: ", background)

    # ---Game logic should go here
    screen.fill(background)
    screen.blit(textOb, (20, 550))
    pygame.draw.rect(screen, rectBg, [rect_x, 50, 50, 50])

    pygame.display.flip()  # de dao giua man hinh buffer va man hinh display
    clock.tick(60)  # 60 khung hinh/s

pygame.quit()
