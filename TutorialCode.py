#import the pygame mod
import pygame

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#Loads up all the images into a list.

pygame.init #Boots up pygame

#creates our windows and gives it width
win = pygame.display.set_mode((480, 500)) #Doesn't work with single brackets idk why yet.

#Names the windows if on winodws idk bout linux.
pygame.display.set_caption("Tutorial pygame")

Ssceenwdith = 500
clock = pygame.time.Clock()


class em(object):

    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkcount = 0
        self.vel  = 3
        self.path = [self.x, self.end] #array
        self.goblin = True
        self.hitbox  = (self.x + 20, self.y, 28, 60)

    def draw(self, win):#allows us to use win
        if self.goblin == True:
            self.move()
            if self.walkcount + 1 > 33:
                self.walkcount = 0

            if self.vel > 0:#if we are moving
                win.blit(self.walkRight[self.walkcount //3], (self.x, self.y))
                self.walkcount += 1
            else:
                win.blit(self.walkLeft[self.walkcount //3], (self.x, self.y))
                self.walkcount +=1
            self.hitbox  = (self.x + 20, self.y, 28, 60)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    
    def hit(self):
        self.goblin = False
        print("hit!")



    def move(self):#
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel #Easy stuff
            else:
                self.vel = self.vel * -1
                self.walkcount = 0


        




class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        self.hitbox  = (self.x + 20, self.y, 28, 60)

    
    def draw(self, win):
        if self.walkcount + 1  >=27: #Each frame for 3 secounds 27 /3 is 9 and we have 9 images
            self.walkcount = 0
        
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkcount//3], (self.x,self.y)) #Takes image and cords .blit does.
                self.walkcount += 1 
            elif self.right:
                win.blit(walkRight[self.walkcount//3], (self.x,self.y))
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox  = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(win, (255,0,0), self.hitbox,2)


class projectile(object):
    def __init__(self, x, y, radius, colour,facing):
        self.x = x 
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x,self.y), self.radius)



def drawGame(): #Error here -- ERROR HERE --
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)

    for bullet in bullets:
        bullet.draw(win) #takes blueprints from list and runs .draw on them

    pygame.display.update()






#All of this is for keeping track of which image to show.
#Starting the main loop this thing checks for events / crap happening.

run = True #While the program is alive
man = player(300, 410, 64, 64)
bullets = []
goblin = em(100,410, 64, 64, 450 )
shootloop = 0
while run:


    
    clock.tick(27)
    if shootloop > 0:
        shootloop +=1
    if shootloop > 3:
        shootloop = 0

    for event in pygame.event.get(): #LIST of events
        if event.type == pygame.QUIT: # Check if the user pressed quit / not a gamer move. #Not sure why but you have to use QUIT for the event otherwise you get function
            run = False #breaks loop
 
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))



    #PYGAME LOGIC NOTE: CORDS are from the top left and + is right 

    KEYSPRESSED = pygame.key.get_pressed()
    if KEYSPRESSED[pygame.K_SPACE] and shootloop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0),facing)) #Creates blueprint for bullet in the list
        shootloop = 1

    if KEYSPRESSED[pygame.K_LEFT] and man.x > man.vel: #If pygame.K_KEFT = True in KEYSPRESSED DO: #And And x > vel: Its not lower than 5. We have to do this because pygame takes from top left
        man.x -= man.vel #Take from the x takes you left.
        #Left goes - So 5 / vel stops it from going pass 5 
        man.left = True
        man.right = False
        man.standing = False

    elif KEYSPRESSED[pygame.K_RIGHT] and man.x < Ssceenwdith  - man.width: #Its cords cant be over 500, Taking width stops it from being off the screen and taking vel checks it wont be
        man.x+= man.vel #Adding takes you right.
        #Right is posstive so SW tops it from going pass 500, We take val to check if its going to be off the screen, take width to check that the whole charcter is on the Screen
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkcount = 0 #Rests like the image run
    if not(man.jump): #if jumping = False
        if KEYSPRESSED[pygame.K_UP]: #If I press space:
            man.jump = True #Is jumping is true so we don't come back to this loop because if not above instead we run the count in else
            man.standing = True

        #if x or y > width or height: #Idea for fixing off the screen glitch without tutorial
        # x -= 10 
             #y -= 10
    else:
        if man.jumpcount >= -10: #If jumpcount greater than -10, because it goes up 10 and down to -10
            neg = 1 
            if man.jumpcount < 0:
                neg = -1 
            #y -= etc Go up the amount:
            man.y -= (man.jumpcount ** 2) * 0.5 * neg #Do the amount of jumps in jumpcount squared etc, As jump count lower the y acceleteration rate slows because the numbers are smaller
            man.jumpcount -= 1 # Keep slowing the jump after launch

        else:
            man.jump = False
            man.jumpcount = 10
    drawGame()
            
    

        


 

#once loop is broken do:
pygame.display.quit()
pygame.quit()

