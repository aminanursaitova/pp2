import pygame
import datetime

now = datetime.datetime.now()

current_time = now.strftime("%H:%M:%S")
m = int(current_time[3] + current_time[4])
s = int(current_time[6] + current_time[7])

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
image1 = pygame.image.load("C:/Users/amina/Downloads/main-clock.png")
image2 = pygame.image.load("C:/Users/amina/Downloads/right-hand.png")
image3 = pygame.image.load("C:/Users/amina/Downloads/left-hand.png")

def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)
  
    # draw rectangle around the image
w1, h1 = image1.get_size()
w2, h2 = image2.get_size()
w3, h3 = image3.get_size()
anglemin = 90 - m*6
anglesec = 90 - s*6
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        
    screen.fill(0)
    screen.blit(image1, (0, 0))
    blitRotate(screen, image2, (w1/2, h1/2), (w2/2, h2/2), anglemin)
    blitRotate(screen, image3, (w1/2, h1/2), (w3/2, h3/2), anglesec)
    # anglemin -= 1/600
    anglesec -= 1/10
    
    pygame.display.flip()