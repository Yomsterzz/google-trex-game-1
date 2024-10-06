import pygame
import random
from pygame.locals import *
pygame.init()

WIDTH = 864
HEIGHT = 936

clock = pygame.time.Clock()
fps = 60
# title_font = pygame.font.SysFont("helvicta", 14)
ground_x = 0
scroll_speed = 4
running = True
game_over = False
in_the_air = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-rex Game") 

bg = pygame.image.load("./images/bg.png")
ground = pygame.image.load("./images/ground.png")

class Trex(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.counter = 0
        
        self.trex_left = pygame.image.load("./images/trex-left-foot.png")
        self.trex_right = pygame.image.load("./images/trex-right-foot.png")
        
        self.image = self.trex_right
        self.is_foot_on_right = True
        
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.animation_delay = 15
        self.animation_counter = 0
        self.velocity = 0    
        self.clicked = False
        self.in_the_air = True
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE] and not self.in_the_air:
            self.velocity = -12
            self.in_the_air = True
        
        if self.in_the_air:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            self.rect.y += int(self.velocity)
            
        if self.rect.bottom >= 768:
            self.rect.bottom = 768
            self.velocity = 0
            self.in_the_air = False
            
        if game_over == False and in_the_air == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.velocity = -10
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.animation_counter += 1
        if self.animation_counter > self.animation_delay:
            self.is_foot_on_right = not self.is_foot_on_right
            self.animation_counter = 0  

        if self.is_foot_on_right:
            self.image = self.trex_right
        else:
            self.image = self.trex_left
        
trex_group = pygame.sprite.Group()
trex1 = Trex(int(WIDTH/4), int(HEIGHT/2))     
trex_group.add(trex1)
        
while running:
    clock.tick(fps)

    screen.blit(bg, (0,0))
    
    trex_group.draw(screen)
    trex_group.update()
    
    screen.blit(ground, (ground_x, 768))
    ground_x -= scroll_speed
    if abs(ground_x) > 35:
        ground_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()