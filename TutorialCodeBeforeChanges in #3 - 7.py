#import the pygame mod
import pygame

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

pygame.init #Boots up pygame

#creates our windows and gives it width
win = pygame.display.set_mode((500, 500)) #Doesn't work with single brackets idk why yet.

#Names the windows if on winodws idk bout linux.
pygame.display.set_caption("Tutorial pygame")

Ssceenwdith = 500

x = 200
y = 200

width = 40
height = 60
vel = 5
clock = 100
isJumping = False
jumpcount = 10



#Starting the main loop this thing checks for events / crap happening.

run = True #While the program is alive
while run:
    pygame.time.delay(clock) #Like a clock sets the pace that the loop is excuted at, clock is miliseconds

    for event in pygame.event.get(): #LIST of events
        if event.type == pygame.QUIT: # Check if the user pressed quit / not a gamer move. #Not sure why but you have to use QUIT for the event otherwise you get function
            run = False #breaks loop

    #PYGAME LOGIC NOTE: CORDS are from the top left and + is right 

    KEYSPRESSED = pygame.key.get_pressed()

    if KEYSPRESSED[pygame.K_LEFT] and x > vel: #If pygame.K_KEFT = True in KEYSPRESSED DO: #And And x > vel: Its not lower than 5. We have to do this because pygame takes from top left
        x -= vel #Take from the x takes you left.
        #Left goes - So 5 / vel stops it from going pass 5 

    if KEYSPRESSED[pygame.K_RIGHT] and x < Ssceenwdith  - width: #Its cords cant be over 500, Taking width stops it from being off the screen and taking vel checks it wont be
        x+= vel #Adding takes you right.
        #Right is posstive so SW tops it from going pass 500, We take val to check if its going to be off the screen, take width to check that the whole charcter is on the Screen
    if not(isJumping): #if jumping = False
        if KEYSPRESSED[pygame.K_UP] and y > vel:
            y -= vel #-From the y takes you up

        if KEYSPRESSED[pygame.K_DOWN] and  y < Ssceenwdith - height:
            y += vel #+ to the y takes you down
        
        if KEYSPRESSED[pygame.K_SPACE]: #If I press space:
            isJumping = True #Is jumping is true so we don't come back to this loop because if not above instead we run the count in else
        
        #if x or y > width or height: #Idea for fixing off the screen glitch without tutorial
        # x -= 10 
             #y -= 10
    else:
        if jumpcount >= -10: #If jumpcount greater than -10, because it goes up 10 and down to -10
            neg = 1 
            if jumpcount < 0:
                neg = -1 
            #y -= etc Go up the amount:
            y -= (jumpcount ** 2) * 0.5 * neg #Do the amount of jumps in jumpcount squared etc, As jump count lower the y acceleteration rate slows because the numbers are smaller
            jumpcount -= 1 # Keep slowing the jump after launch

        else:
            isJumping = False
            jumpcount = 10
            
    

        


    win.fill((0,0,0)) #Fills the surface otherwise you got lot of red lads. / Rectangle, every run of loop fills the screen
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) #rect gives you a rect #Win / The windows is our surface, Then Hex colour, Then cords for where it should be and its height and width at those cords
    pygame.display.update()

#once loop is broken do:
pygame.display.quit()
pygame.quit()

