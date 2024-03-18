import pygame
import random

# Classes setup
class Snake(object):
    def __init__(self):
        self.left = random.randint(minleft,maxleft)
        self.top = random.randint(mintop,maxtop)
        self.length = length
        self.width = width
    
        self.rect = pygame.rect.Rect((self.left, self.top, self.length, self.width))
        # self.rect.center = 
    
    def handle_keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
           self.rect.move_ip(-self.width, 0)
        if key[pygame.K_d]:
           self.rect.move_ip(self.width, 0)
        if key[pygame.K_w]:
           self.rect.move_ip(0, -self.width)
        if key[pygame.K_s]:
           self.rect.move_ip(0, self.width)

    def draw(self, surface):
        pygame.draw.rect(surface, "green", self.rect)


class Target(object):
    def __init__(self) -> None:

        self.left = random.randint(minleft,maxleft)
        self.top = random.randint(mintop,maxtop)
        self.length = length
        self.width = width

        self.rect = pygame.rect.Rect((self.left, self.top, self.length, self.width))

    def draw(self, surface):
        pygame.draw.rect(surface, "red", self.rect)
        

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
length = 30
width = 30
minleft = 0
maxleft = 1080 - length
mintop = 0
maxtop = 720 - width
player = Snake()
target = Target()
running = True
dt = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    player.draw(screen)
    target.draw(screen)
    player.handle_keys()
    pygame.display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) 


pygame.quit()