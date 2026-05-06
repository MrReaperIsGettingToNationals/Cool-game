import pygame
pygame.init()

screen = pygame.display.set_mode([600,600])
pygame.display.set_caption('Ball Bouncer')
red = (255,0,0)
green = (0, 255, 0)
blue = (0,0,255)
background = blue
framerate = 60
circle_x = 300
circle_y = 300
circle_x_direction = 3
circle_y_direction = 6

timer = pygame.time.Clock()

def update_ball_position():
    global circle_x
    global circle_y
    global circle_x_direction
    global circle_y_direction
    if circle_x_direction > 0:
        if circle_x < 570:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1
    elif circle_x_direction < 0:
        if circle_x > 30:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1
    if circle_y_direction > 0:
        if circle_y < 570:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
    elif circle_y_direction < 0:
        if circle_y > 30:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
    

running = True
while running:
    timer.tick(framerate)
    update_ball_position()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((background))

        pygame.draw.circle(screen, green, (circle_x, circle_y), 30, 5)

        pygame.display.flip()

pygame.quit()