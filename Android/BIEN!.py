import pygame
import random

s = random.randint(30,60)
c = 525
y = 325
q = 1
u = 1
flag = False
platform_x = 450
end = False

a = 0

pygame.init()
screen = pygame.display.set_mode((1125, 750))
pygame.display.set_caption("BIEN!")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 48)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_, y_ = event.pos
            flag = True

            if 100 < x_ < 300 and 550 < y_ < 650 and platform_x < 925:
                platform_x -= 40
            if 825 < x_ < 1025 and 550 < y_ < 650 and platform_x > 0:
                platform_x += 40

    if flag == True:
        if q == 1:
            c += 5
            if 1125 - c < s:
                q = 2
        
        if q == 2:
            c -= 5
            if c - s < 5:
                q = 1


        if u == 1:
            y += 5

        if u == 2:
            y -= 5
            if y - s < 5:
                u = 1

        if c + s > platform_x and y + s >= 700 and c - s < platform_x + 200:
            u = 2
            a += 1
            y = 700 - s

        if y - s > 950:
            flag = False
            end = True

    screen.fill((50,0,100))
    pygame.draw.circle(screen, (240, 200, 0), (c, y), s)
    pygame.draw.rect(screen, (250,250,250), (platform_x, 700, 200, 25))
    screen.blit(font.render(str(a), True, (255,255,255)), (50, 50))
    if end == True:
        screen.blit(font.render("Game Over", True, (200, 0, 0)), (400, 100))
    pygame.draw.rect (screen, (10,10,10), (100, 550, 200, 100))
    pygame.draw.rect(screen, (10,10,10), (825, 550, 200, 100))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
