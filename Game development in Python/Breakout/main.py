"""
Step 1: import pygame library
"""
import pygame
# import paddle class
from paddle import Paddle
from ball import Ball
from brick import Brick
pygame.init()

'''
Step 2: Define colours in the game
'''
#Define some colors in RGB format
WHITE=(255,255,255)
DARKBLUE=(36,90,190)
LIGHTBLUE=(0,176,240)
RED=(255,0,0)
ORANGE=(255,100,0)
YELLOW=(255,255,0)

score=0
lives=3


'''
Step 3: open a new window
'''
# set window size
size=(800,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# Responding the keystroke events
paddleA=Paddle(WHITE,10,100)
paddleA.rect.x=20
paddleA.rect.y=200

paddleB=Paddle(WHITE,10,100)
paddleB.rect.x=670
paddleB.rect.y=200


# this will be a list that will contain all the sprites we intend
all_sprites_list=pygame.sprite.Group()

# Add thepaddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# Create the paddle 
paddle=Paddle(LIGHTBLUE,100,100)
paddle.rect.x=350
paddle.rect.y=560

# Create the ball sprite
ball=Ball(LIGHTBLUE,10,10)
ball.rect.x=345
ball.rect.y=195

all_bricks=pygame.sprite.Group()
for i in range(7):
    brick=Brick(RED,80,30)
    brick.rect.x=60+i*100
    brick.rect.y=100
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# add the paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)


'''
step 4: Main program loop
Capturing Events: Used to constantly “listen” to user inputs and react to these. It could be when the user use the keyboard or the mouse.
Implementing the Game Logic. What happens when the game is running? Are cars moving forward, aliens falling from the sky, ghosts chasing you, etc.
Refreshing the screen by redrawing the stage and the sprites.
'''
# the lopp will carry on until exit the game
carryOn=True

#the clock will be used to control how fast screen upload updates
clock=pygame.time.Clock()

#------------ Main program loop
while carryOn:
    # main event loop
    for event in pygame.event.get(): #user did something
        if event.type ==pygame.QUIT: # if user click close
            carryOn=False # Flag that we are done to exit
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn=False
    
    # Moving the paddle when the use uses the arrow key
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
        
    
    #-------- Game logic should go there
    all_sprites_list.update()
    
    # Check if the ball is bounhing against any of the 4 walls
    if ball.rect.x>=790:
        ball.velocity[0]= -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0]= -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1]= -ball.velocity[1]
        lives-=1
        if lives==0:
            # Display Game over for 3 seconds
            font=pygame.font.Font(None,74)
            text=font.render("GAME OVER",1,WHITE)
            screen.blit(text,(250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            # stop the game
            carryOn=False
            
    if ball.rect.y<40:
        ball.velocity[1]= -ball.velocity[1]
    
    
    # Detect collisions between the ball and paddles
    if pygame.sprite.collide_mask(ball,paddle):
        ball.rect.x -=ball.velocity[0]
        ball.rect.y -=ball.velocity[1]
        ball.bounce()
    
    # Check if there is a car collision
    brick_collision_list=pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
        ball.bounce()
        score +=1
        brick.kill()
        
        if len(all_bricks) ==0:
            # Display level complete 3 seconds
            font=pygame.font.Font(None,74)
            text=font.render("LEVEL COMPLETE",1,WHITE)
            screen.blit(text,(200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            # stop the Game
            carryOn=False
    
    #--- Drawing code should go here
    # First clear the screen to dark blue
    screen.fill(DARKBLUE)
    pygame.draw.line(screen,WHITE,[0,38],[800,38],2)
    
    # now lets draw all the sprites in one go
    all_sprites_list.draw(screen)
    
    # Display the score and the number of lives at the top of the window
    font=pygame.font.Font(None,34)
    text=font.render("Score: "+str(score),1,WHITE)
    screen.blit(text,(20,10))
    
    text=font.render("Lives: "+str(lives),1,WHITE)
    screen.blit(text,(650,10))
    
    # Go ahead and update the screen with we've drawn
    pygame.display.flip()
    # Limit to 60 frame per second
    clock.tick(60)
# Once we have exited the main program loop we can stop the game
pygame.quit()
    
    