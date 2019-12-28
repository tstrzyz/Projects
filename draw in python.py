import time
import pygame
import time
from pygame import gfxdraw
pygame.init()
clock = pygame.time.Clock()
screen=pygame.display.set_mode([1000,600])
pygame.display.set_caption("idk")
color = (255,255,255)
radius = 6
done = False
screen.fill((255,255,255))
drawing = True

while not done:
    pygame.display.update()
    clock.tick(60)
    spot = pygame.mouse.get_pos()

    m_x = int(spot[0])
    m_y = int(spot[1])
    for event in pygame.event.get():
        if  event.type == pygame.KEYDOWN:
            screen.fill((255,255,255))

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            if drawing == True:
                pygame.draw.circle(screen,color,spot,radius)
                for i in range(2):
                    pygame.gfxdraw.aacircle(screen,m_x-1,m_y,radius,color)
                    radius -= 1
                radius = 6
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen,color,spot,radius)
            for i in range(2):
                pygame.gfxdraw.aacircle(screen,m_x-1,m_y,radius,color)
                radius -= 1
            radius = 6
            drawing = True
            color = (0,0,0)
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

            









            
        
