import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
is_blue = True
x = 50
y = 50

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 20: y -= 20
        if pressed[pygame.K_DOWN] and y < 460: y += 20
        if pressed[pygame.K_LEFT] and x > 20: x -= 20
        if pressed[pygame.K_RIGHT] and x < 620: x += 20
        
        screen.fill((0, 0, 0))
        if is_blue: color = (255, 204, 255)
        else: color = (204, 204, 255)
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)