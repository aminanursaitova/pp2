# import pygame

# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# done = False

# is_blue = True

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             is_blue = not is_blue 
#     # Add this somewhere after the event pumping and before the display.flip()
#     if is_blue: color = (0, 128, 255)
#     else: color = (255, 100, 0)
#     pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))  
#     pygame.display.flip()

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        if is_blue: color = (255, 204, 255)
        else: color = (204, 204, 255)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)