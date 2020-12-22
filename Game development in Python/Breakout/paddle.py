import pygame
BLACK=(0,0,0)

class Paddle(pygame.sprite.Sprite):
    # This class represent a paddle. It drives from the "Sprite class"
    def __init__(self, color,width,height):
        # call the parent class (Sprite) constrctor
        super().__init__()
        
        # pass in the color of the car and its x and y position
        # set the background color and set it to be transparent
        self.image=pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        
        # Draw the paddle(a rectangle)
        pygame.draw.rect(self.image,color,[0,0,width,height])
        
        # Fetch the rectangle object that has the dimension of the image
        self.rect=self.image.get_rect()
    
    # step 1: Adding method to the paddle class
    
    def moveLeft(self,pixels):
        self.rect.x -=pixels
        # check that you are not going too far(off the screen)
        if self.rect.x<0:
            self.rect.x=0
    
    def moveRight(self,pixels):
        self.rect.x +=pixels
        # check that you are not going too far(off the screen)
        if self.rect.x >700:
            self.rect.x=700
            