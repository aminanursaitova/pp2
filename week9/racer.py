import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (230, 200, 250)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
YUM = 0
count = 0
new = True
 
#Setting up Fonts
font = pygame.font.SysFont("candara", 60)
font_small = pygame.font.SysFont("candara", 20)
game_over = font.render("game over):", True, BLACK)
 
background = pygame.image.load("C:/Users/amina/Downloads/wp10043053-solid-light-pink-desktop-wallpapers.jpg")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
pos = [50, 150, 250, 350]
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/amina/Downloads/hk.png")
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.image.get_rect()
        self.rect.center=(random.choice(pos),0) 
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.choice(pos), 0)
 
class strawberry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/amina/Downloads/Strawberry.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center=(random.choice(pos),0) 
 
    def move(self):
        global new, YUM
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.choice(pos), 0)
    def new(self):
        global YUM
        YUM += 1
        global count
        count += 1
        global SPEED
        if count > 15:
            count = 0
            SPEED += 2
        self.rect.top = 0
        self.rect.center = (random.choice(pos), 0)

class banana(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/amina/Downloads/banana.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center=(random.choice(pos), 0) 
 
    def move(self):
        global new, YUM
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.choice(pos), 0)
    def new(self):
        global YUM
        YUM += 2
        global count
        count += 2
        global SPEED
        if count > 15:
            count = 0
            SPEED += 2
        self.rect.top = 0
        self.rect.center = (random.choice(pos), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/amina/Downloads/kuromi.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)   
 
         
P1 = Player()
E1 = Enemy()
C1 = strawberry()
C2 = banana()
scoins = pygame.sprite.Group()
scoins.add(C1)
bcoins = pygame.sprite.Group()
bcoins.add(C2)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(E1)
all_sprites.add(C2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
while True:     
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    yum = font_small.render(str(YUM), True, BLACK)
    DISPLAYSURF.blit(yum, (SCREEN_WIDTH - 20, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (60,250))
        scores = font.render(str(SCORE), True, BLACK)
        scores1 = font_small.render("YOU SLAYED!", True, BLACK)
        DISPLAYSURF.blit(scores1, (50,30))
        DISPLAYSURF.blit(scores, (90,70))
        yum = font.render(str(YUM), True, BLACK)
        yum1 = font_small.render("YOU ATE!", True, BLACK)
        DISPLAYSURF.blit(yum1, (SCREEN_WIDTH - 150, 30))
        DISPLAYSURF.blit(yum, (SCREEN_WIDTH - 120, 70))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(5)
        pygame.quit()
        sys.exit()  

    # coin counter
    if pygame.sprite.spritecollideany(P1, scoins):
        C1.new()
    if pygame.sprite.spritecollideany(P1, bcoins):
        C2.new()


         
    pygame.display.update()
    FramePerSec.tick(FPS)