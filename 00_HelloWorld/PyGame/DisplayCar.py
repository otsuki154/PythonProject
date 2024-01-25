import pygame
import math

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Kích thước cửa sổ
width, height = 800, 600

pygame.init()
size = (width, height)  # width=800, heigh=600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Load Image")
# Loop until the user clicks the close button
done = False
# Used to manage how fast then screen updates
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
scaleCarImage = pygame.transform.scale(carImg, [100, 100])  # scale nho image lai


def placeCar(x, y):
    screen.blit(scaleCarImage, [x, y])


def rotateCar(x, y, angle):
    rotateCar = pygame.transform.rotate(scaleCarImage, angle)
    screen.blit(rotateCar, (x, y))


# Main Programe Loop
while not done:
    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ---Game logic should go here
    screen.fill(WHITE)
    # Lay position cua mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.degrees(math.atan2(mouse_y - (height // 2), mouse_x - (width // 2)))
    # placeCar(100, 200)
    # rotate car theo mouse
    rotateCar(100, 100, angle)

    pygame.display.flip()  # de dao giua man hinh buffer va man hinh display
    clock.tick(60)  # 60 khung hinh/s

pygame.quit()
