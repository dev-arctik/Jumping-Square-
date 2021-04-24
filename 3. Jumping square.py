import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 250
y = 250
width = 4
height = 4
vel = 5

isJump = False
jumpcount = 10


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        if x < 0:
            x = 500
            vel = 0.5*vel

    if keys[pygame.K_RIGHT]:
        x += vel
        if x > 500:
            x = 0
            vel = 2*vel
    if not(isJump):
        if keys[pygame.K_UP]:
            y -= vel
            if y < 0:
                y = 500
                vel = 0.5*vel

        if keys[pygame.K_DOWN]:
            y += vel
            if y > 500:
                y = 0
                vel = 2*vel

        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount<0:
                neg = -1
            y -= (jumpcount **2) * 0.5 * neg
            jumpcount -= 1
            
        else:
            isJump = False
            jumpcount = 10

        
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    


pygame.quit()
