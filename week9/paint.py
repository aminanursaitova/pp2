import pygame
import pygame.gfxdraw
import math

pygame.init()


global mode
global color
# draw a line
def draw_line(surface, color, start_pos, end_pos):
    pygame.draw.line(surface, color, start_pos, end_pos, radius)

# draw a circle on the surface
def draw_circlein(surface, color, center_pos, radius1):
    pygame.draw.circle(surface, color, center_pos, radius1)
def draw_circleout(surface, color, center_pos, radius1, l):
    pygame.draw.circle(surface, color, center_pos, radius1, l)

# draw a rectangle on the surface
def draw_rectin(surface, color, start_pos, end_pos):
    pygame.draw.rect(surface, color, (start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])))

def draw_rectout(surface, color, start_pos, end_pos, l):
    pygame.draw.rect(surface, color, (start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])), l)

# draw a square on the surface
def draw_sqin(surface, color, start_pos, end_pos):
    m = max(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])
    pygame.draw.rect(surface, color, (start_pos, (m, m)))

def draw_sqout(surface, color, start_pos, end_pos, l):
    m = max(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])
    pygame.draw.rect(surface, color, (start_pos, (m, m)), l)

# draw a right triangle on the surface
def draw_rtrianglein(surface, color, start_pos, end_pos):
    pos1 = start_pos
    pos2 = end_pos
    pos3 = (start_pos[0], end_pos[1])
    pygame.draw.polygon(surface, color, (pos1, pos2, pos3))

def draw_equilateral_triangle(surface, color, start_pos, end_pos):
    length = abs(start_pos[1] - end_pos[1]) * 2 / 3 ** 0.5
    pos1 = ((start_pos[0] + end_pos[0])/2, start_pos[1])
    pos2 = (pos1[0] + length / 2, end_pos[1])
    pos3 = (pos1[0] - length / 2, end_pos[1])

    pygame.draw.polygon(surface, color, (pos1, pos2, pos3))

def draw_rhombus(surface, color, start_pos, end_pos):
    pos1 = ((start_pos[0] + end_pos[0])/2, start_pos[1])
    pos2 = (start_pos[0], (start_pos[1] + end_pos[1])/2)
    pos4 = (end_pos[0], (start_pos[1] + end_pos[1])/2)
    pos3 = ((start_pos[0] + end_pos[0])/2, end_pos[1])

    pygame.draw.polygon(surface, color, (pos1, pos2, pos3, pos4))



# function for drawing a line
def drawLineBetween(screen, start, end, radius):   
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if y > 120 + radius:
            pygame.draw.circle(screen, color, (x, y), radius)


# buttons class
class Button:
    def __init__(self, image, position, c, cl):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.c = c
        self.cl = cl
 
    def on_click(self, event):
        x, y = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.c = 'red'
                    for t in self.cl:
                        if t != self:
                            t.c = 'black'
                    return True
            return False    
        
 
# Define and create buttons

# images
image1 = pygame.image.load("C:/Users/amina/Downloads/eraser.png")
image1 = pygame.transform.scale(image1, (80, 100))
image2 = pygame.image.load("C:/Users/amina/Downloads/pen.png")
image2 = pygame.transform.scale(image2, (80, 100))
image3 = pygame.image.load("C:/Users/amina/Downloads/Strawberry.png")
image3 = pygame.transform.scale(image3, (80, 45))
image4 = pygame.transform.scale(image3, (40, 45))
image5 = pygame.transform.scale(image3, (60, 45))

# class for drawing tools
bubu = []
eraser = Button(image1, (10, 10), 'black', bubu)
pen = Button(image2, (100, 10), 'red', bubu)
rectin = Button(image3, (190, 10), 'black', bubu)
rectout = Button(image3, (190, 65), 'black', bubu)
circlein = Button(image3, (280, 10), 'black', bubu)
circleout = Button(image3, (280, 65), 'black', bubu)
sqin = Button(image5, (470, 10), 'black', bubu)
sqout = Button(image5, (470, 65), 'black', bubu)
rtrin = Button(image5, (540, 10), 'black', bubu)
etrin = Button(image5, (540, 65), 'black', bubu)
rhombus = Button(image5, (610, 10), 'black', bubu)
# etrout = Button(image5, (610, 65), 'black', bubu)

bubu.append(pen)
bubu.append(eraser)
bubu.append(rectout)
bubu.append(rectin)
bubu.append(sqout)
bubu.append(sqin)
bubu.append(circleout)
bubu.append(circlein)
bubu.append(rtrin)
bubu.append(etrin)
bubu.append(rhombus)

# class for colors
col = []
red = Button(image4, (370, 10), 'black', col)
green = Button(image4, (370, 65), 'black', col)
blue = Button(image4, (420, 10), 'red', col)



col.append(red)
col.append(blue)
col.append(green)

def main():
    # creating a screen
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()
    # some constants
    global radius
    radius = 15
    x = 0
    y = 0
    cir = False
    global mode
    mode = 'blue'
    global mode1 
    mode1 = mode
    global drawing
    drawing = False
    global start_pos
    start_pos = (0, 120)
    global end_pos
    end_pos = (0, 120)
    global shape
    shape = ''
    points = []
    global color
    if mode == 'blue':
        color = (153, 204, 255)
    elif mode == 'red':
        color = (255, 153, 204)
    elif mode == 'green':
        color = (153, 255, 204)
    elif mode == 'black':
        color = (0, 0, 0)



    while True:
        
        pressed = pygame.key.get_pressed()
        # no idea what this is for but ig it needs to be here
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        # the loop
        for event in pygame.event.get():
            # makes the top white in case if it gets drawn on
            draw_rectin(screen, (255, 255, 255), (0, 0), (800,120))

            # displaying buttons
            for k in bubu:
                screen.blit(k.image, k.rect)
            # outlines for a buttons
                if k.c == 'black':
                    pygame.draw.rect(screen, (0, 0, 0), k.rect, 1)
                else:
                    pygame.draw.rect(screen, (255, 0, 0), k.rect, 1)
            for k in col:
                screen.blit(k.image, k.rect)
            # outlines for a buttons
                if k.c == 'black':
                    pygame.draw.rect(screen, (0, 0, 0), k.rect, 1)
                else:
                    pygame.draw.rect(screen, (255, 0, 0), k.rect, 1)
            # drawing symbols on buttons, didn't know how to do it other way
            draw_rectin(screen, (0, 0, 0), (195, 15), (265, 50))
            draw_rectout(screen, (0, 0, 0), (195, 70), (265, 105), 5)
            draw_circlein(screen, (0, 0, 0), (320, 32.5), 20)
            draw_circleout(screen, (0, 0, 0), (320, 87.5), 20, 5)
            draw_rectin(screen, (255, 153, 204), (375, 15), (405, 50))
            draw_rectin(screen, (153, 255, 204), (375, 70), (405, 105))
            draw_rectin(screen, (153, 204, 255), (425, 15), (455, 50))
            draw_sqin(screen, (0, 0, 0), (482.5, 15), (492.5, 50))
            draw_sqout(screen, (0, 0, 0), (482.5, 70), (492.5, 105), 5)
            draw_rtrianglein(screen, (0, 0, 0), (545, 15), (595, 50))
            draw_equilateral_triangle (screen, (0, 0, 0), (545, 70), (595, 105))
            draw_rhombus(screen, (0, 0, 0), (620, 15), (660, 50))
            # nice line
            pygame.draw.line(screen, (0, 0, 0), (0, 120), (800,120), 1)  
            # didn't work when in main() so i moved it here, works now
            if mode == 'blue':
                color = (153, 204, 255)
            elif mode == 'red':
                color = (255, 153, 204)
            elif mode == 'green':
                color = (153, 255, 204)
            elif mode == 'white':
                color = (255, 255, 255)  
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used        
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # changing the size of the brush
                if event.key == pygame.K_UP :
                    radius = min(200, radius + 5)
                if event.key == pygame.K_DOWN: 
                    radius = max(1, radius - 5) 
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # checking if the buttons got clicked
                if event.button == 1:  
                    if event.pos[1] < 120:
                        cir = True
                        if eraser.on_click(event) == True:
                            mode1 = mode
                            mode = 'white'
                            shape = ''
                        elif red.on_click(event) == True:
                            mode = 'red'
                            mode1 = mode
                        elif green.on_click(event) == True:
                            mode = 'green'
                            mode1 = mode
                        elif blue.on_click(event) == True:
                            mode = 'blue'
                            mode1 = mode
                        elif pen.on_click(event) == True:
                            mode = mode1
                            shape = ''
                        elif rectin.on_click(event) == True:
                            shape = 'rectin'
                            mode = mode1
                        elif rectout.on_click(event) == True:
                            shape = 'rectout'
                            mode = mode1
                        elif sqin.on_click(event) == True:
                            shape = 'sqin'
                            mode = mode1
                        elif sqout.on_click(event) == True:
                            shape = 'sqout'
                            mode = mode1
                        elif circlein.on_click(event) == True:
                            shape = 'circlein'
                            mode = mode1
                        elif circleout.on_click(event) == True:
                            shape = 'circleout' 
                            mode = mode1
                        elif rtrin.on_click(event) == True:
                            shape = 'rtrin'
                            mode = mode1
                        elif etrin.on_click(event) == True:
                            shape = 'etrin' 
                            mode = mode1
                        elif rhombus.on_click(event) == True:
                            shape = 'rhombus' 
                            mode = mode1
                        points = []
                        
                    # indicating the drawing process
                    else:
                        cir = False
                        drawing = True
                        start_pos = event.pos
                
            #drawing a line
            elif pygame.mouse.get_pressed()[0] and event.pos[1] > 120 + radius and shape == '':
                position = event.pos
                points = points + [position]
                points = points[-2:]
                i = 0
                while i < len(points) - 1:
                    drawLineBetween(screen, points[i], points[i + 1], radius)
                    i += 1
            # drawing using tools
            elif event.type == pygame.MOUSEBUTTONUP  and not cir:
                if event.button == 1:  # left mouse button
                    drawing = False
                    end_pos = event.pos
                    
                    if shape == 'circlein':
                        radius1 = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        center_pos = start_pos[0], start_pos[1]
                        draw_circlein(screen, color, center_pos, radius1)
                    elif shape == 'circleout':
                        radius1 = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        center_pos = start_pos[0], start_pos[1]
                        draw_circleout(screen, color, center_pos, radius1, radius)
                    elif shape == 'rectin':
                        draw_rectin(screen, color, start_pos, end_pos)
                    elif shape == 'rectout':
                        draw_rectout(screen, color, start_pos, end_pos, radius)
                    elif shape == 'sqin':
                        draw_sqin(screen, color, start_pos, end_pos)
                    elif shape == 'sqout':
                        draw_sqout(screen, color, start_pos, end_pos, radius)
                    elif shape == 'rtrin':
                        draw_rtrianglein(screen, color, start_pos, end_pos)
                    elif shape == 'etrin':
                        draw_equilateral_triangle(screen, color, start_pos, end_pos)
                    elif shape == 'rhombus':
                        draw_rhombus(screen, color, start_pos, end_pos)
            
                    # drawing a single point
                    elif event.button == 1 and event.pos[1] > 120 + radius:
                        pygame.draw.circle(screen, color, event.pos, radius)
                        position = event.pos
                        points = points + [position]   
                    points = []           
        pygame.display.flip()
        
        clock.tick(60)

main()