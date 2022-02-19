import time
import pygame
from pygame import gfxdraw
pygame.init()
clock = pygame.time.Clock()
screen=pygame.display.set_mode([1280,720])
pygame.display.set_caption("paint")
color = (0,0,0)

done = False
screen.fill((255,255,255))
drawing= False

#class main(self,self.spot,self.fps):
drawing = False
def main(fps):
    pygame.display.update()
    clock.tick(300)
    global drawing
    for event in pygame.event.get():
        main.spot = pygame.mouse.get_pos()
        
        m_x = int(main.spot[0])
        m_y = int(main.spot[1])    
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
            DrawPen(5,m_x,m_y,drawing)
            
            
                  
            


def DrawPen(radius,m_x,m_y,drawing):
        if drawing == True:
            pygame.draw.circle(screen,color,main.spot,radius)
            for i in range(4):
                pygame.gfxdraw.aacircle(screen,m_x-1,m_y,radius,color)
                radius -= 1
            radius = 5

while not done:
    main(120)
