import time
import pygame
from pygame import gfxdraw

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("draw")
screen=pygame.display.set_mode([1000,800])
done = False
drawing = False
screen.fill((255,255,255))

class Brush:

    def __init__(self, width, color):
        self.width = width
        self.color = color
    def circle(self,surface, x, y, r, color):
        #for i in range(10):
        #    pygame.gfxdraw.aacircle(screen,m_x,m_y,Brush.width,Brush.color)
        #    Brush.width -= 1
        #Brush.width += 10
        pygame.draw.circle(screen,Brush.color,mousepos,Brush.width)
        
            

Brush= Brush(10,(0,0,0))

while not done:
    pygame.display.update()
    mousepos = pygame.mouse.get_pos()
    m_x = int(mousepos[0])  
    m_y = int(mousepos[1])
    rel = pygame.mouse.get_rel()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            Brush.circle(screen,m_x,m_y,Brush.width,Brush.color)
                
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
        if event.type == pygame.QUIT:
            done = True
        if drawing == True:
            Brush.circle(screen,m_x,m_y,Brush.width,Brush.color)
                
         

