import pygame
from random import  randint

BLACK=(0,0,0)
class Ball(pygame.sprite.Sprite):
    # This class represent a ball
    def __init__(self,color,width,height):
        # call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height
        # set the background color and set it to be transparent
        
        self.image=pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # Drawinng the ball rectangle
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.velocity=[randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimension of the image
        self.rect=self.image.get_rect()
    
    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]
        
    def bounce(self):
        self.velocity[0]= -self.velocity[0]
        self.velocity[1] =randint(-8,8)