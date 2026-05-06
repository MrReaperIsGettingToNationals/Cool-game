import pygame
pygame.init()

screen = pygame.display.set_mode([600,600])
pygame.display.set_caption('Ball Bouncer')
red = (255,0,0)
green = (0, 255, 0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
orange = (255, 165, 0)
background = blue
framerate = 60
circle_x = 300
circle_y = 300
circle_x_direction = 3
circle_y_direction = 6

player_width = 30
player_height = 50
player_x = 300
player_y = 500
player_x_direction = 0
player_y_direction = 0
player_speed = 3

font = pygame.font.Font("freesansbold.ttf", 20)
score = 0
timer = pygame.time.Clock()

def update_player_position():
    global player_x
    global player_y
    global player_x_direction
    global player_y_direction
    if player_x_direction > 0:
        if player_x < 600 - player_width:
            player_x += player_x_direction * player_speed
    if player_x_direction < 0:
        if player_x > 0:
            player_x += player_x_direction * player_speed
    if player_y_direction > 0:
        if player_y < 600 - player_height:
            player_y += player_y_direction * player_speed
    if player_y_direction < 0:
        if player_y > 0:
            player_y += player_y_direction * player_speed



def update_ball_position():
    global circle_x
    global circle_y
    global circle_x_direction
    global circle_y_direction
    global score
    if circle_x_direction > 0:
        if circle_x < 570:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1
            score += 1
    elif circle_x_direction < 0:
        if circle_x > 30:
            circle_x += circle_x_direction
        else:
            circle_x_direction *= -1
            score += 1
    if circle_y_direction > 0:
        if circle_y < 570:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
            score += 1
    elif circle_y_direction < 0:
        if circle_y > 30:
            circle_y += circle_y_direction
        else:
            circle_y_direction *= -1
            score += 1
    

running = True
while running:
    timer.tick(framerate)
    update_ball_position()
    update_player_position()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_direction = -1
            if event.key == pygame.K_RIGHT:
                player_x_direction = 1
            if event.key == pygame.K_UP:
                player_y_direction = -1
            if event.key == pygame.K_DOWN:
                player_y_direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_direction = 0
            if event.key == pygame.K_RIGHT:
                player_x_direction = 0
            if event.key == pygame.K_UP:
                player_y_direction = 0
            if event.key == pygame.K_DOWN:
                player_y_direction = 0

        screen.fill((background))

        pygame.draw.circle(screen, green, (circle_x, circle_y), 30, 5)
        pygame.draw.circle(screen, red, (circle_x, circle_y), 25)
        pygame.draw.rect(screen, orange, [player_x, player_y, player_width, player_height])
        display_score = font.render("Score: "+ str(score), True, white, black)
        screen.blit(display_score, (10, 10))
        pygame.display.flip()

pygame.quit()
