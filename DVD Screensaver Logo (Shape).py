import pygame
pygame.init()
import random

X, Y = 600, 600
FPS = 30

window = pygame.display.set_mode((X, Y))
caption = pygame.display.set_caption("DVD Screensaver Logo (Shape)")
clock = pygame.time.Clock()
x_vel, y_vel = random.randint(1, 5), random.randint(1, 5)
RED, BLUE, YELLOW, GREEN, WHITE, BLACK, PURPLE, PINK, ORANGE, CYAN = (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 0), (255, 255, 255), (0, 0, 0), (255, 0, 255), (255, 192, 203), (255, 165, 0), (0, 255, 255)

colours = [RED, BLUE, YELLOW, GREEN, WHITE, CYAN, PURPLE, PINK, ORANGE]
colour = random.choice(colours)

def move(form):
    global x_vel
    global y_vel

    form.x += x_vel
    form.y += y_vel

def draw(form): #Help Needed in displaying the text, everything is done right but placement was important in this scenario
    window.fill(BLACK)
    pygame.draw.rect(window, colour, form)
    text = font.render(("Edge Hit: " + str(edge_hit)), 1, (255, 255, 255))
    window.blit(text, (30, 10))
    text = font.render(("Corner Hit: " + str(corner_hit)), 1, (255, 255, 255))
    window.blit(text, (30, 30))
    pygame.display.update()

shape = pygame.Rect((X // 2), (Y // 2), 30, 30)
edge_hit = 0
corner_hit = 0
font = pygame.font.SysFont("Comic Sans Ms", 30, "Bold", True)

run = True
while run:    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    move(shape)

    if (shape.right > X or shape.left <= 0) and (shape.bottom > Y or shape.top <= 0): #Help Needed in corner detection
        colour = random.choice(colours)
        x_vel, y_vel = random.randint(1, 5), random.randint(1, 5)
        x_vel *= -1
        y_vel *= -1
        corner_hit += 1
    
    if shape.right > X or shape.left <= 0:
        colour = random.choice(colours)
        x_vel = random.randint(1, 5)
        x_vel *= -1
        edge_hit += 1

    if shape.bottom > Y or shape.top <= 0:
        colour = random.choice(colours)
        y_vel = random.randint(1, 5)
        y_vel *= -1
        edge_hit += 1

    draw(shape)
    pygame.display.update()
pygame.quit()