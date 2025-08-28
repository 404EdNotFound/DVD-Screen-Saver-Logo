import pygame
import random
pygame.init()

X, Y = 600, 600
FPS = 60

window = pygame.display.set_mode((X, Y))
caption = pygame.display.set_caption("DVD Screensaver Logo (Image)")
clock = pygame.time.Clock()

DVD_Logo = pygame.image.load("DVD Logo.PNG")
DVD_IMAGE_SIZE = (100, 50)
DVD_Logo = pygame.transform.scale(DVD_Logo, DVD_IMAGE_SIZE)

class DVD(object):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.x_velocity = random.randint(1, 5)
        self.y_velocity = random.randint(1, 5)
        self.edge_hit = 0
        self.corner_hit = 0
    
    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def collision(self):
        if (self.x + self.length > X or self.x <= 0) and (self.y + self.width > Y or self.y <= 0): #Help Needed in corner detection
            self.x_velocity *= -1
            self.y_velocity *= -1
            self.corner_hit += 1
        
        elif self.x <= 0:
            self.x_velocity = random.randint(1, 5)
            self.edge_hit += 1
        
        elif self.y <= 0:
            self.y_velocity = random.randint(1, 5)
            self.edge_hit += 1

        elif self.x + self.length >= X or self.x <= 0:
            self.x_velocity *= -1
            self.edge_hit += 1

        elif self.y + self.width >= Y or self.y <= 0:
            self.y_velocity *= -1
            self.edge_hit += 1
        
        else:
            self.edge_hit += 0
            self.corner_hit += 0

def draw():
    window.fill((0, 0, 0))
    window.blit(DVD_Logo, (DVD_Screensaver.x, DVD_Screensaver.y)) #Help was needed in moving the images
    text = font.render(("Edge Hit: " + str(DVD_Screensaver.edge_hit)), 1, (255, 255, 255))
    window.blit(text, (30, 10))
    text = font.render(("Corner Hit: " + str(DVD_Screensaver.corner_hit)), 1, (255, 255, 255))
    window.blit(text, (30, 30))
    pygame.display.update()

font = pygame.font.SysFont("Comic Sans Ms", 30, "Bold", True)
DVD_Screensaver = DVD(50, 50, 100, 50)

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    DVD_Screensaver.move()
    DVD_Screensaver.collision()
    
    draw()
    pygame.display.update()


pygame.quit()
