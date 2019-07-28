import time
import pygame
from pygame import gfxdraw
pygame.init()
clock = pygame.time.Clock()
screen=pygame.display.set_mode([1280,720])
pygame.display.set_caption("paint")
color = (255,255,255)
radius = 5
done = False
screen.fill((255,255,255))
drawing = True

class main(self,self.spot,self.fps):

def main(fps):
    pygame.display.update()
    clock.tick(300)
    main.spot = pygame.mouse.get_pos()

    m_x = int(spot[0])
    m_y = int(spot[1])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if  event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255,255,255))
            if event.key == pygame.K_ESCAPE:
                done = True

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEMOTION:
            DrawPen()


def DrawPen():
                if drawing == True:
                    pygame.draw.circle(screen,color,main.spot,radius)
                    for i in range(4):
                        pygame.gfxdraw.aacircle(screen,m_x-1,m_y,radius,color)
                        radius -= 1
                    radius = 5
while not done:
    main(60)
