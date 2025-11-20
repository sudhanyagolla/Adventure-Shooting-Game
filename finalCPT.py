##
# ICS3U CPT: Create a game using given theme (Something Smells in Here)
#
# @ authors Lily Bai and Sudhanya Golla
# @ course ICS3UC
# @ date 2024/06/11 - LastModified
#
# Pygame base template for opening a window
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
# Explanation video: http://youtu.be/vRB_983kUMc
##

## Pygame setup
import pygame
import random
pygame.init()
size = (800, 450)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Stinky Game")

## MODEL - Data use in system
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (171,221,230)
LIGHTBROWN = (255,240,218)
SKYBLUE = (131, 217, 238)
PALEBROWN = (249, 203, 188)
YELLOW = (255, 238, 88)
BROWN = [120, 72, 0]
LIGHTGREY = (200, 200, 200)
PINK = (244, 143, 177)
BLUE = (0, 0, 255)

# Gather images
# Forest image found from https://www.amazon.ca/Customized-wallpaper-flowers-contracted-setting/dp/B09GW4ZLBN
forest = pygame.image.load("photosAndSounds/forest.png").convert()
forest = pygame.transform.scale(forest, [800, 450])

# Porch image found from https://www.shutterstock.com/search/cartoon-terrace-house
imageIntro = pygame.image.load("photosAndSounds/porch.png").convert()
imageIntro = pygame.transform.scale(imageIntro, [800, 450])
imageIntro.set_colorkey(BLACK)

# Chandelier image found from https://www.vectorstock.com/royalty-free-vector/chandelier-vector-988248
chandeleir = pygame.image.load("photosAndSounds/chandeleir.png").convert()
chandeleir = pygame.transform.scale(chandeleir, [123,210])
chandeleir.set_colorkey(WHITE)

# Dishwasher image found from https://www.stacksocial.com/sales/bosch-shem63w55n-300-series-44db-stainless-built-in-dishwasher
dishwasher = pygame.image.load("photosAndSounds/dishwasher.png").convert()
dishwasher = pygame.transform.scale(dishwasher, [110,125])
dishwasher.set_colorkey(WHITE)

# Bed image found from https://www.vecteezy.com/vector-art/513580-double-bed-furniture-vector-illustration
bed = pygame.image.load("photosAndSounds/bed.png").convert()
bed = pygame.transform.scale(bed, [300,233])
bed.set_colorkey(WHITE)

# Closet image found from https://www.amazon.com/Higher-Hangers-Slimline-Organizer-Increase/dp/B08H5RWJ3Z?th=1
closet = pygame.image.load("photosAndSounds/closet.png").convert()
closet = pygame.transform.scale(closet, [710, 356])

# Image found from https://www.freepik.com/premium-vector/pixel-art-male-character-holding-shotgun-isolated-white-background_33445347.htm
mainCharImg = pygame.image.load("photosAndSounds/mainCharacter.png").convert()
mainCharImg.set_colorkey(WHITE)

# Image found from https://www.pinterest.com/pin/618400592608554428/
scaredPersonImg=pygame.image.load("photosAndSounds/scaredSprite.png").convert()
scaredPersonImg = pygame.transform.scale(scaredPersonImg, [100, 154])
scaredPersonImg.set_colorkey(BLACK)

# Image found from https://www.vecteezy.com/free-png/cardboard-box
boxImg = pygame.image.load("photosAndSounds/mysteryBox.png").convert()
boxImg.set_colorkey(WHITE)

# Image found from https://www.freepik.com/free-vector/black-spider-cartoon-isolated_59994785.htm
spiderImg = pygame.image.load("photosAndSounds/spider.png").convert()
spiderImg.set_colorkey(WHITE)

# Image found from https://www.pixilart.com/art/the-animated-coin-40c77fce6fbb4c3
coinImg = pygame.image.load("photosAndSounds/coin.gif").convert()
coinImg = pygame.transform.scale(coinImg, [50, 50])
coinImg.set_colorkey(WHITE)
coinBigImg = pygame.transform.scale(coinImg, [100, 100])
coinBigImg.set_colorkey(WHITE)

# Image found from https://www.facebook.com/ChoreZombie/
zombieImg = pygame.image.load("photosAndSounds/zombie.png").convert()
zombieImg = pygame.transform.scale(zombieImg, [300, 300])
zombieImg.set_colorkey((254,254,254))

# Image found from https://the-grossery-gang-collector-cards.fandom.com/wiki/Ice_Scream
rottenFoodImg = pygame.image.load("photosAndSounds/rottenEgg.png").convert()
rottenFoodImg.set_colorkey((254,254,254))

# Image found from https://pixeljoint.com/pixelart/64699.htm
goblinImg = pygame.image.load("photosAndSounds/monsterSprite.png").convert()
goblinImg = pygame.transform.scale(goblinImg, [100, 100])
goblinImg.set_colorkey((254,254,255))

# Image found from https://en.wikipedia.org/wiki/Attic
bossFight1 = pygame.image.load("photosAndSounds/bossFightScene1.png").convert()
bossFight1 = pygame.transform.scale(bossFight1, [800, 533])

# Image found from https://www.pinterest.com/pin/id-like-to-see-about-replicating-this-look--71635450293922618/
bossFight2 = pygame.image.load("photosAndSounds/basement.png").convert()
bossFight2 = pygame.transform.scale(bossFight2, [800, 533])

# Image found from https://www.shutterstock.com/image-vector/skunk-vector-cartoon-illustration-262249616
skunkImg = pygame.image.load("photosAndSounds/skunk.png").convert()
skunkImg = pygame.transform.scale(skunkImg , [100, 100])
skunkImg.set_colorkey(WHITE)

# Sound effect from https://pixabay.com/ 
gunSound = pygame.mixer.Sound("photosAndSounds/blaster.ogg")

# Class to create and draw rooms
class Room():
    
    # Define characteristics
    def __init__(self):
        self.floorColour = []
        self.wallColour = []
        self.offset = 0 

    # Draw the room
    def draw(self, surface):
        pygame.draw.rect(surface, self.wallColour, [0,0,800,450])
        pygame.draw.rect(surface, self.floorColour, [0,floorHeight,800,200])

# Class to create and draw entities
class Entities():
    
    # Define characteristics
    def __init__(self):
        self.faceRight = False
        self.xPos = 0
        self.yPos = 0
        self.changeX = 0
        self.changeY = 0
        self.colour = ()
        self.size = [0,0]
        self.active = False
        self.isAPlatform = False
    
    # Draw the entitity
    def drawEntity(self, img, surface):
        self.imageLeft = img
        self.imageRight = pygame.transform.flip(self.imageLeft, True, False)
        
        # Flip the image depending if character is facing right/left
        if self.faceRight == True:
            surface.blit(self.imageRight, [self.xPos,self.yPos])
        else:
            surface.blit(self.imageLeft, [self.xPos,self.yPos])
    
    # Check for collision between entities
    def checkCollision(self, other):
        collision = False
        
        # Determine whether object is within presence of specified object
        if other.yPos < self.yPos+self.size[1] and \
            other.yPos +other.size[1] > self.yPos and \
            other.xPos < self.xPos +self.size[0] and \
            other.xPos+other.size[0] > self.xPos:
            
                collision = True
                
                # Allow player to land on entity if it is considered a platform
                if other.isAPlatform and self.changeY > 0:
                    self.yPos = other.yPos - self.size[1]
                    self.changeY = 0
                    self.inAir = False
        
        return collision

    # Determine whether mouse is within presence of object
    def hover(self, mousePos):
        hover = False
        
        # Check if mouse is inside dimensions of the object
        if self.xPos < mousePos[0] < self.xPos + self.size[0] and \
            self.yPos < mousePos[1] < self.yPos + self.size[1]:
            hover = True
        
        return hover

# Class to create stink particles
class StinkParticles(Entities):
    
    # Define characteristics and inherit from entities
    def __init__(self, monster):
       super().__init__()
       self.xPos = random.randrange(monster.xPos-30, monster.xPos+
                                    monster.size[0]+30)
       self.yPos = random.randrange(monster.yPos-30, monster.yPos+
                                    monster.size[1])
       self.changeX = random.choice([-0.1,0, 0.1])
       self.changeY = random.choice([-0.1,0, 0.1])
       self.colour = GREEN
    
    # Draw each stink particle
    def draw(self, surface):
       pygame.draw.circle(surface, self.colour, [self.xPos,self.yPos], 3)
    
    # Move the stink particles 
    def move(self):
       self.xPos += self.changeX
       self.yPos += self.changeY

# Class to create and draw door that leads to next level
class Door(Entities):
    
    # Draw door and its handle
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, [self.xPos,
                                                self.yPos,self.size[0],
                                                self.size[1]])
        pygame.draw.circle(screen,YELLOW,[self.xPos+10,
                                          self.yPos+self.size[1]/2],5)
    
    # Print text for user over the door 
    def displayNextLevel(self, surface):
        textDoor = "Go to door to enter next level"
        font = pygame.font.SysFont('Calibri', 20, True, False)
        textDoor = font.render(textDoor, True, BLACK)
        surface.blit(textDoor, [self.xPos, self.yPos - 20])

    # Print text for user over the door 
    def displayFinalLevel(self, surface):
        textDoor = "Click door to enter final level"
        font = pygame.font.SysFont('Comic Sans', 20, True, False)
        textDoor = font.render(textDoor, True, BLACK)
        surface.blit(textDoor, [self.xPos, self.yPos - 50])
    
    # Print text for user over the door 
    def bossFight(self, surface):
        textDoor = "Click to see a surprise!"
        font = pygame.font.SysFont('Comic Sans', 20, True, False)
        textDoor = font.render(textDoor, True, WHITE)
        surface.blit(textDoor, [self.xPos, self.yPos - 50])

# Class to create and draw door that leads to previous level
class BackDoor(Door):
    
    # Define characteristics and inherit from Doors
    def __init__(self):
        super().__init__()
        self.size = [40, 125]
    
    # Show text instructions for user over door
    def displayPreviousLevel(self, surface, xOffset):
        textDoor = "Go to door to enter previous level"
        font = pygame.font.SysFont('Comic Sans', 20, True, False)
        textDoor = font.render(textDoor, True, BLACK)
        surface.blit(textDoor, [self.xPos + xOffset, self.yPos - 50])

# Class to create and draw window on screen
class Window(Entities):
    
    # Define characteristics and inherit from Entities
    def __init__(self):
        super().__init__()
        self.colour = [200,200,200]

    # Draw window with 4 panes
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, [self.xPos,self.yPos,
                                                self.size[0],self.size[1]])
        pygame.draw.rect(surface, WHITE, [self.xPos,self.yPos,
                                          self.size[0],self.size[1]],5)
        pygame.draw.line(surface, WHITE, [self.xPos+self.size[0]/2,
                                          self.yPos],
                            [self.xPos+self.size[0]/2,self.yPos+
                             self.size[1]],5)
        pygame.draw.line(surface, WHITE, [self.xPos, self.yPos+
                                          self.size[1]/2],
                         [self.xPos+self.size[0],self.yPos+self.size[1]/2],5)

# Class to create and draw Table on Screen
class Table(Entities):
    
    # Define characteristics and inherit from Entities
    def __init__(self):
        super().__init__()
        self.isAPlatform = True

    # Draw table with 2 legs
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, [self.xPos,self.yPos,
                                                self.size[0],20])
        pygame.draw.rect(surface, self.colour, [self.xPos+10,self.yPos,
                                                10,self.size[1]])
        pygame.draw.rect(surface, self.colour, [self.xPos+
                                                self.size[0]-20,
                                                self.yPos,10,self.size[1]])

# Class to create and draw chair
class Chair(Entities):
    
    # Define characteristics and inherit from Entities
    def __init__(self):
        super().__init__()
        self.sizeLeg = []
        self.isAPlatform = True
    
    # Draw chair with 2 legs
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, [self.xPos,
                                                self.yPos, self.size[0],
                                                self.size[1]])
        pygame.draw.rect(surface, self.colour, [self.xPos + 15,
                                                self.yPos + 5, 
                                                self.sizeLeg[0],
                                                self.sizeLeg[1]])
        pygame.draw.rect(surface, self.colour, [self.xPos +self.size[0] -
                                                self.sizeLeg[0] - 
                                                15, self.yPos + 5,
                                                self.sizeLeg[0],
                                                self.sizeLeg[1]])
        pygame.draw.rect(surface, self.colour, [self.xPos +self.size[0] -
                                                self.sizeLeg[0] - 
                                                15, self.yPos - 60,
                                                self.sizeLeg[0] + 10,
                                                self.sizeLeg[1]])

# Class to create and draw wardrobe
class Wardrobe(Entities):

    # Define characteristics and inherit from Entities
    def __init__(self):
        super().__init__()
        self.colour2 = []
        self.colour3 = []

    # Draw a wardrobe
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour2, [self.xPos,
                                                 self.yPos, self.size[0],
                                                    self.size[1]])
        pygame.draw.ellipse(surface, self.colour3, [self.xPos,
                                                    self.yPos, self.size[0]
                                                    ,self.size[1]/3])
        pygame.draw.ellipse(surface, self.colour3, [self.xPos, self.yPos
                                                    + self.size[1]/3,
                                                    self.size[0]
                                                    ,self.size[1]/3])
        pygame.draw.ellipse(surface, self.colour3, [self.xPos, self.yPos
                                                    + self.size[1]*2/3,
                                                    self.size[0]
                                                    ,self.size[1]/3])
        pygame.draw.rect(surface, self.colour,
                            [self.xPos, self.yPos, self.size[0],
                             self.size[1]], 10)
        pygame.draw.line(surface, self.colour,
                            [self.xPos, self.yPos + self.size[1]/3],
                            [self.xPos + self.size[0], self.yPos +
                            self.size[1]/3], 10)
        pygame.draw.line(surface, self.colour,
                            [self.xPos, self.yPos + self.size[1]*2/3],
                            [self.xPos + self.size[0], self.yPos +
                            self.size[1]*2/3], 10)

# Class to create and draw anything considered a being within game
class LivingThings(Entities):
    
    # Define characteristics and inherit from Entities
    def __init__(self):
        super().__init__()
        self.inAir = False
        self.maxHealth = 100
        self.currentHealth = self.maxHealth
        self.alive = False

    # Allow the character to move and apply gravity
    def move(self):
        self.changeY += 0.4 
        self.xPos += self.changeX
        self.yPos += self.changeY

        # Ensure characters cannot go off the left/right side of screen
        if self.xPos < 0:
            self.xPos = 0
            self.changeX = self.changeX * -1
            self.faceRight = True
        elif self.xPos > 800-self.size[0]:
            self.xPos = 800-self.size[0]
            self.changeX = self.changeX * -1
            self.faceRight = False
        
        # Ensure characters don't fall through the floor
        if self.yPos > floorHeight - self.size[1]:
            self.changeY = 0 
            self.yPos = floorHeight - self.size[1] 
            self.inAir = False  

# Class to create and draw monsters
class Monsters(LivingThings):

    # Display health
    def drawHealthBar(self, surface):
        pygame.draw.rect(surface, RED, [self.xPos +
                                        self.size[0]// 2,
                                        self.yPos + 10,
                                        self.currentHealth,10])
        pygame.draw.rect(surface, BLACK, [self.xPos +
                                          self.size[0]// 2,
                                          self.yPos + 10,
                                          self.maxHealth, 10], 1)

# Class to create and draw main character onto screen
class Player(LivingThings):

    # Define characteristics and inherit from LivingThings
    def __init__(self):
        super().__init__()
        self.maxHealth = 200
        self.currentHealth = self.maxHealth
        self.speedX = 0

    # Allow player to jump up if not already in air
    def jump(self):
        if userControl and not self.inAir:
                self.changeY = -10
                self.inAir = True

    # For animations in intro
    def animateMove(self):
        self.xPos += self.speedX

    # Display health and change colour depending on health
    def drawHealthBar(self, surface):
        if self.currentHealth >= self.maxHealth*2/3:
            healthColour = GREEN
        elif self.currentHealth >= self.maxHealth*1/3:
            healthColour = YELLOW
        elif self.currentHealth < self.maxHealth*1/3:
            healthColour = RED
        pygame.draw.rect(surface, healthColour, [20, 20,self.currentHealth,20])
        pygame.draw.rect(surface, BLACK, [20, 20, self.maxHealth, 20], 2)

# Class to create and draw bullets
class Bullets(Entities):
    
    # Define characteristics and get parameters
    def __init__(self, x, y, speed):
        super().__init__()
        self.xPos = x
        self.yPos = y
        self.changeX = speed
        self.size = [10, 5]
        self.color = BLACK
        self.active = True

    # Move bullet
    def move(self, enemy):
        self.xPos += self.changeX

        # Check if bullet goes off screen
        if self.xPos < 0 or self.xPos > 800:
            self.active = False
        
        hit = self.checkCollision(enemy)
        
        # Check if bullet hits an enemy
        if hit and enemy.alive:
            self.active = False
            enemy.currentHealth -= 10

    # Draw bullets
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, [self.xPos, self.yPos], 2)

# Draws text for introduction
def displayDialogue(clickNum, surface):
    
    # Change dialogue based on number of clicks
    if clickNum == 0:
        text = "You were taking a stroll through the woods."
    elif clickNum == 1: 
        text = "Suddenly, you hear someone screaming."
    elif clickNum == 2:
        text = "You decide to move in the direction of the screaming."
    elif clickNum == 3:
        text = "Help! My house is so stinky I cannot even live in it!'"
    elif clickNum == 4:
        text = "You feel sorry for the person and decide to help them out"
    elif clickNum == 5:
        text = "You tell them to wait outside and enter on your own."
    elif clickNum == 6:
        text = "Move character towards door using left or right arrow"

    # Format and display text
    pygame.draw.rect(screen, PALEBROWN, [250, 370, 550, 40])
    font = pygame.font.SysFont('Calibri', 20, True, False)            
    text = font.render(text, True, WHITE)
    surface.blit(text, [250,380])

# Display text once boss is defeated
def displayVictory(clickNum, surface):

    # Change dialogue based on number of clicks
    if clickNum == 0:
        victoryText = "The scared person suddenly becomes happy. \
'You defeated the boss!' he screams."
    elif clickNum == 1:
        victoryText = "'Hopefully my house won't be smelly anymore.'"
    elif clickNum >= 2:
        victoryText = "You express your gratitude and go on your way. \
The end."

    # Format and display text on screen
    font = pygame.font.SysFont('Calibri', 20, True, False)
    victoryText = font.render(victoryText, True, WHITE)
    surface.blit(victoryText, [5, 420])

# Show user how many coins they have collected in game
def coinDisplay(surface):
    pygame.draw.rect(surface, WHITE, [600, 20, 185, 25])
    coinText = "Number of coins: " + str(coinCounter)
    font = pygame.font.SysFont('Calibri', 20, True, False)
    coinText = font.render(coinText, True, BLACK)
    surface.blit(coinText, [600, 25])

# Draw poster
def drawPoster(surface, xOffset):
    pygame.draw.rect(surface, PINK, [200+xOffset, 50, 60, 100])
    pygame.draw.circle(surface, BLUE, [230+xOffset, 83], 30)
    pygame.draw.circle(surface, BLUE, [230+xOffset, 116], 30)

# Set variables for later use
floorHeight = 353
clickNum = 0
scene = 1

# Create a main character
mainChar = Player()
mainChar.size = [80, 103]
mainChar.xPos = 10
mainChar.yPos = 250
userControl = False

# Create a door for introduction
door1 = Door()
door1.colour = RED
door1.size[0] = 100
door1.size[1] = 175
door1.xPos = 50
door1.yPos = 225

# Door in level 1 (allows to enter level 2)
door2 = Door()
door2.colour = WHITE
door2.size = [100, 175]
door2.xPos = 60
door2.yPos = floorHeight - door2.size[1]

# Store furniture in lists for use later on
furnitureRoom1 = []
furnitureRoom2 = []
furnitureRoom3 = []

# Door for Level 2 (Allows to enter level 3)
door4 = Door()
door4.colour = BLUE
door4.size = [125, 150]
door4.xPos = 50
door4.yPos = floorHeight - door4.size[1]
furnitureRoom2.append(door4)

# Door for Level 3 (Allows to enter closet)
door3 = Door()
door3.colour = WHITE
door3.size[0] = 120
door3.size[1] = 200
door3.xPos = 350
door3.yPos = 150

# Create doors for closet to lead into boss fight
door5 = Door()
door5.colour = GREEN
door5.size = [135, 190]
door5.xPos = 100
door5.yPos = floorHeight - door5.size[1]

door6 = Door()
door6.colour = GREEN
door6.size = [135, 190]
door6.xPos = 300
door6.yPos = floorHeight - door6.size[1]

# Create backdoor for level 2 (allow to re-enter level 1)
backDoorLevel2 = BackDoor()
backDoorLevel2.colour = BLACK
backDoorLevel2.xPos = 760
backDoorLevel2.yPos = 228

# Create backdoor for level 3 (allow to re-enter level 2)
backDoorLevel3 = BackDoor()
backDoorLevel3.colour = RED
backDoorLevel3.xPos = 760
backDoorLevel3.yPos = 253-25

# Draw room for level 1
room1 = Room()
room1.wallColour = LIGHTBLUE
room1.floorColour = LIGHTBROWN

# Draw room for level 2
room2 = Room()
room2.wallColour = WHITE
room2.floorColour = LIGHTBROWN

# Draw room for level 3
room3 = Room()
room3.wallColour = LIGHTGREY
room3.floorColour = BLACK

# Draw room for closet
room4 = Room()
room4.floorColour = LIGHTBROWN
room4.wallColour = BLACK

# Create windows for level 1
window = Window()
window.xPos = 600
window.yPos = 50
window.size = [100,200]
furnitureRoom1.append(window)

window1 = Window()
window1.xPos = 400
window1.yPos = 100
window1.size = [100,100]
furnitureRoom1.append(window1)

# Create windows for level 2
window2 = Window()
window2.colour = LIGHTBLUE
window2.xPos = 550
window2.yPos = 75
window2.size = [100, 125]
furnitureRoom2.append(window2)

window3 = Window()
window3.colour = LIGHTBLUE
window3.xPos = 100
window3.yPos = 75
window3.size = [190, 140]
furnitureRoom2.append(window3)

# Create window for level 3
window4 = Window()
window4.colour = RED
window4.xPos = 575
window4.yPos = 30
window4.size = [135, 135]

# Create wardrobes for closet
wardrobe5 = Wardrobe()
wardrobe5.colour = BROWN
wardrobe5.colour2 = WHITE
wardrobe5.colour3 = LIGHTBLUE
wardrobe5.size = [150, 250]
wardrobe5.xPos = 50
wardrobe5.yPos = 100

wardrobe6 = Wardrobe()
wardrobe6.colour = BROWN
wardrobe6.colour2 = WHITE
wardrobe6.colour3 = BLACK
wardrobe6.size = [150, 250]
wardrobe6.xPos = 600
wardrobe6.yPos = 100

# Create table for level 1
table1 = Table()
table1.colour = BROWN
table1.size = (150,80)
table1.xPos = 200
table1.yPos = floorHeight-table1.size[1]
furnitureRoom1.append(table1)

# Create table for level 2
table2 = Table()
table2.colour = (187, 191, 193)
table2.size = (200, 101)
table2.xPos = 75
table2.yPos = floorHeight-table2.size[1]
furnitureRoom2.append(table2)

# Create table for level 3
table3 = Table()
table3.colour = BROWN
table3.size = (200, 101)
table3.xPos = 525
table3.yPos = floorHeight-table3.size[1]
furnitureRoom3.append(table3)

# Room 2 chair
chair2 = Chair()
chair2.colour = BROWN
chair2.size = [100, 20]
chair2.sizeLeg = [10, 75]
chair2.xPos = 300
chair2.yPos = floorHeight - 80
furnitureRoom2.append(chair2)

# Store boxes for future use
boxListLevel1 = []
boxListLevel2 = []
boxListLevel3 = []

# Level 1 boxes
box1 = Entities()
box1.active = True
box1.size = [100,81]
box1.xPos = 400
box1.yPos = floorHeight-box1.size[1]
boxListLevel1.append(box1)

box2 = Entities()
box2.active = True
box2.size = [100,81]
box2.xPos =  200
box2.yPos = 193
boxListLevel1.append(box2)

box3 = Entities()
box3.active = True
box3.size = [100,81]
box3.xPos =  55
box3.yPos = floorHeight - door2.size[1] - box3.size[1]
boxListLevel1.append(box3)

# Level 2 Boxes
box4 = Entities()
box4.active = True
box4.size = [100,81]
box4.xPos = 120
box4.yPos = floorHeight - table2.size[1] - box4.size[1]
boxListLevel2.append(box4)

# Level 3 Boxes
box6 = Entities()
box6.size = [100,81]
box6.active = True
box6.xPos = 75
box6.yPos = floorHeight - 60 - box6.size[1]
boxListLevel3.append(box6)

box7 = Entities()
box7.size = [100,81]
box7.active = True
box7.xPos = 550
box7.yPos = floorHeight - 100 - box7.size[1]
boxListLevel3.append(box7)

# Store coin in each level based on type and level it is in
coinListLevel1 = []
coinListLevel2 = []
coinListLevel3 = []
coinListLevel4 = []
bigCoinLevel2 = []
bigCoinLevel3 = []

# Track player's currency throughout game
coinCounter = 0

# Create coins to be collected by player in level 1
coin1 = Entities()
coin1.size = [50,50]
coin1.xPos = box2.xPos
coin1.yPos = box2.yPos + 10
coinListLevel1.append(coin1)

coin2 = Entities()
coin2.size = [50,50]
coin2.xPos = box2.xPos + 50
coin2.yPos = box2.yPos + 10
coinListLevel1.append(coin2)

coin3 = Entities()
coin3.size = [50,50]
coin3.xPos = box2.xPos + 100
coin3.yPos = box2.yPos + 10
coinListLevel1.append(coin3)

coin4 = Entities()
coin4.size = [50,50]
coin4.xPos = box2.xPos + 150
coin4.yPos = box2.yPos + 10
coinListLevel1.append(coin4)

# Create coins to be collected by player in level 2
coin5 = Entities()
coin5.size = [50,50]
coin5.active = True
coin5.xPos = 400
coin5.yPos = floorHeight - 125 - box1.size[1]
coinListLevel2.append(coin5)

coin6 = Entities()
coin6.size = [50,50]
coin6.active = True
coin6.xPos = 450
coin6.yPos = floorHeight - 125 - box1.size[1]
coinListLevel2.append(coin6)

coin7 = Entities()
coin7.size = [50,50]
coin7.active = True
coin7.xPos = 500
coin7.yPos = floorHeight - 125 - box1.size[1]
coinListLevel2.append(coin7)

coin8 = Entities()
coin8.size = [50,50]
coin8.active = True
coin8.xPos = 550
coin8.yPos = floorHeight - 125 - box1.size[1]
coinListLevel2.append(coin8)

# Create larger coin for player to collect in level 2
bigCoin = Entities()
bigCoin.size = [100, 100]
bigCoin.active = True
bigCoin.xPos = box4.xPos + 75
bigCoin.yPos = floorHeight - 125 - box1.size[1]
bigCoinLevel2.append(bigCoin)

# Create coins to be collected by player in level 3
coin9 = Entities()
coin9.size = [50,50]
coin9.active = True
coin9.xPos = 50
coin9.yPos = floorHeight - coin9.size[1]
coinListLevel3.append(coin9)

coin10 = Entities()
coin10.size = [50,50]
coin10.active = True
coin10.xPos = 175
coin10.yPos = floorHeight - coin10.size[1]
coinListLevel3.append(coin10)

coin11 = Entities()
coin11.size = [50,50]
coin11.active = True
coin11.xPos = 450
coin11.yPos = floorHeight - coin11.size[1]
coinListLevel3.append(coin11)

coin12 = Entities()
coin12.size = [50,50]
coin12.active = True
coin12.xPos = 475
coin12.yPos = floorHeight - coin12.size[1]
coinListLevel3.append(coin12)

# Create larger coin for player to collect in level 3
bigCoin2 = Entities()
bigCoin2.size = [100, 100]
bigCoin2.xPos = box7.xPos
bigCoin2.yPos = floorHeight - table3.size[1] - box7.size[1]
bigCoinLevel3.append(bigCoin2)

# Create coins to be collected by player in closet
coin13 = Entities()
coin13.size = [50,50]
coin13.active = True
coin13.xPos = 50
coin13.yPos = floorHeight - coin13.size[1]
coinListLevel4.append(coin13)

coin14 = Entities()
coin14.size = [50,50]
coin14.active = True
coin14.xPos = 125
coin14.yPos = floorHeight - coin14.size[1]
coinListLevel4.append(coin14)

coin15 = Entities()
coin15.size = [50,50]
coin15.active = True
coin15.xPos = 725
coin15.yPos = floorHeight - coin15.size[1]
coinListLevel4.append(coin15)

# Create monsters and living beings
# Create list to store and draw monsters
monstersList = []

# Create monsters for level 1
spider = Monsters()
spider.size = [100,88]
spider.xPos = 400
spider.yPos = floorHeight-spider.size[1]
monstersList.append(spider)

skunk = Monsters()
skunk.alive = False
skunk.size = [100,100]
skunk.yPos = floorHeight - door2.size[1] - box3.size[1]
skunk.xPos = 55
monstersList.append(skunk)

# Create monsters for level 2
goblin1 = Monsters()
goblin1.alive = False
goblin1.size = [100,100]
goblin1.yPos = floorHeight-table2.size[1]-goblin1.size[1]
goblin1.xPos = 100
monstersList.append(goblin1)

# Create monsters for level 3
goblin2 = Monsters()
goblin2.alive = False
goblin2.size = [100,100]
goblin2.yPos = 60
goblin2.xPos = 75
goblin2.changeX = -2
monstersList.append(goblin2)

# Create final monsters for boss fight
zombie = Monsters()
zombie.alive = True
zombie.size = [300, 300]
zombie.xPos = 65
zombie.yPos = floorHeight-zombie.size[1]
monstersList.append(zombie)

rottenFood = Monsters()
rottenFood.alive = True
rottenFood.size = [250, 309]
rottenFood.xPos = 65
rottenFood.yPos = floorHeight-rottenFood.size[1]
monstersList.append(rottenFood)

# Create the scared person
scaredPerson = LivingThings()
scaredPerson.size = [100,154]
scaredPerson.yPos = floorHeight-scaredPerson.size[1]
scaredPerson.changeX = 3

# Store stink particles around selected monsters
stinkParticlesSkunk = []
stinkParticlesZombie = []
stinkParticlesRottenFood = []

# Store bullets to draw later on
bulletsList = []

# Create 50 stink particles around the skunk 
for i in range(50):
    stink = StinkParticles(skunk)
    stinkParticlesSkunk.append(stink)

# Create 200 stink particles around the zombie
for i in range(200):
    stink = StinkParticles(zombie)
    stinkParticlesZombie.append(stink)

# Create 200 sitnk particles around the rotten egg
for i in range(200):
    stink = StinkParticles(rottenFood)
    stinkParticlesRottenFood.append(stink)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## Main Program Loop
while not done:
    
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        
        # Check if key/mouse was lifted up or down
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            # If user clicks the mouse in a scene:
            if scene == 1:
                clickNum += 1
            elif scene == 2:
                
                # If user clicks on box, erase box and display spider
                if box1.hover(mousePos) == True and box1.active == True:
                    spider.alive = True
                    box1.active = False
                
                # If user clicks on box, erase box and display coins 
                if box2.hover(mousePos) == True and box2.active == True:
                    
                    # User now has the ability to collect coins in the box
                    for coin in coinListLevel1:
                        coin.active = True

                    box2.active = False
                
                # If user clicks on box, erase box and display spider
                if box3.hover(mousePos) == True and box3.active == True:
                    skunk.alive = True
                    box3.active = False
            
            elif scene == 3:

                # If user clicks on box, erase box and display goblin
                if box4.hover(mousePos) == True and box4.active == True:
                    goblin1.alive = True
                    box4.active = False

            elif scene == 4:
                
                # If user clicks on box, erase box and display whats inside
                if box6.hover(mousePos) == True and box6.active == True:
                    goblin2.alive = True
                    box6.active = False

                elif box7.hover(mousePos) == True and box7.active == True:
                    bigCoin2.active = True
                    box7.active = False
                
                # If user clicks on door, reset player to next level
                if door3.hover(mousePos) == True:
                    scene = 5
                    mainChar.xPos = 450

            elif scene == 5:
                
                # Bring user to a different level depending on door clicked
                if door5.hover(mousePos) == True:
                    scene = 6
                    mainChar.xPos = 700 
                    scaredPerson.xPos = -50
                    clickNum = 0
                elif door6.hover(mousePos) == True:
                    scene = 7
                    mainChar.xPos = 700
                    scaredPerson.xPos = -50
                    clickNum = 0
            
            elif scene == 6 and not zombie.alive:
                clickNum += 1
            elif scene == 7 and not rottenFood.alive:
                clickNum += 1

        elif event.type == pygame.KEYDOWN:
            
            # Player moves left/right when arrow key is pressed
            if event.key == pygame.K_LEFT:
                mainChar.changeX = -3
                mainChar.faceRight = False

            elif event.key == pygame.K_RIGHT:
                mainChar.changeX = 3
                mainChar.faceRight = True
                
            elif event.key == pygame.K_UP:
                mainChar.jump()
            
            elif event.key == pygame.K_SPACE:
                
                # Bullet moves the direction the player is facing
                if mainChar.faceRight == True:
                    bullet = Bullets(mainChar.xPos+80, mainChar.yPos+38, 5)
                else:
                    bullet = Bullets(mainChar.xPos, mainChar.yPos+38, -5)

                # Store bullet for future use and play sound effect
                bulletsList.append(bullet)
                gunSound.play()
                
        elif event.type == pygame.KEYUP:
            
            # Stop moving if player lets go of arrow key
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mainChar.changeX = 0
                
    ## Game logic
    # Gather mouse position
    mousePos = pygame.mouse.get_pos()
    
    # Control user-based movements based on each scene
    if scene == 1:
        
        # Flip direction character is facing in the intro
        # Based on number of clicks
        if clickNum < 3:
            mainChar.faceRight = True
        elif clickNum < 6:
            mainChar.faceRight = False
        
        # Animate character based on number of clicks
        # Character automatically moves across the screen in the intro
        if clickNum == 0:
            mainChar.speedX = 3
            
            # Stop moving in the middle of the screen
            if mainChar.xPos > 200:
                mainChar.speedX = 0
                
        elif clickNum == 2:
            mainChar.speedX = 3
            
            # Stop moving once character is off screen
            if mainChar.xPos > 900:
                mainChar.speedX = 0
        
        elif clickNum == 3:
            mainChar.speedX = -3
            scaredPerson.xPos = 250

            # Stop moving in the middle of the screen
            if mainChar.xPos < 600:
                mainChar.speedX = 0
                
        elif clickNum >= 6:
            userControl = True
            
            # If character walks through door, go to next scene
            if mainChar.checkCollision(door1) == True:
                scene = 2
                clickNum = 0
                mainChar.xPos = 700
                
    elif scene == 2:
        
        # Allow character to jump onto the table if they collide with it
        mainChar.checkCollision(table1)
        
        # Make spider jitter 
        if spider.alive:
            spider.changeX = random.randrange(-4,5)
            spider.move()
        
        # Make skunk jitter
        if skunk.alive:
            skunk.changeX = random.randrange(-4,5)
            skunk.move()
        
        # Make the skunk smelly by moving stink particles around the skunk
        for particle in stinkParticlesSkunk:
            particle.move()
            
            # Player takes damage if they walk into any of its stink particles
            if mainChar.checkCollision(particle):
                   mainChar.currentHealth -= 1
                   stinkParticlesSkunk.remove(particle)
        
        # Move bullets across screen and check if they hit any enemies
        for bullet in bulletsList:
            bullet.move(spider)
            bullet.move(skunk)
            
            # If the bullet hits an enemy or goes off screen, remove it 
            if not bullet.active:
                bulletsList.remove(bullet)

        # Check if any of the coins in level 1 have already been collected
        for coin in coinListLevel1:
            
            # Allow player to collect coin if not collected
            if mainChar.checkCollision(coin) == True and coin.active == True:
                    coin.active = False
                    coinCounter += 10

        # If user walks into door, go to next scene
        if mainChar.checkCollision(door2) == True:
                scene = 3
                mainChar.xPos = 650
        
    elif scene == 3:
        
        # Allow character to jump onto the furniture if they collide with it
        mainChar.checkCollision(table2)
        mainChar.checkCollision(chair2)
        
        # If user walks into back door, go to previous scene
        if mainChar.checkCollision(backDoorLevel2) == True:
                scene = 2
                mainChar.xPos = 200
        
        # If user walks into the other door, go to next scene
        elif mainChar.checkCollision(door4) == True:
                scene = 4
                mainChar.xPos = 650

        # Make the goblin jitter around if it is alive
        if goblin1.alive:
            goblin1.changeX = random.randrange(-3,3)
            goblin1.move()
        
        # Move bullets across screen and check if they hit the goblin
        for bullet in bulletsList:
            bullet.move(goblin1)
            
            # If the bullet hits the goblin or goes off screen, remove it 
            if not bullet.active:
                bulletsList.remove(bullet)

        # Check if any of the coins have been collected in level 2
        for coin in coinListLevel2:
            
            # Allow player to collect coin if not collected before
            if mainChar.checkCollision(coin) == True and coin.active == True:
                coin.active = False
                coinCounter += 10

        # Allow player to collect big coin if not collected before
        if mainChar.checkCollision(bigCoin) == True and \
            bigCoin.active == True:
            bigCoin.active = False
            coinCounter += 50
        
    elif scene == 4:

        # Allow character to jump onto the table if they collide with it
        mainChar.checkCollision(table3)
        
        # If user walks into back door, go to previous scene
        if mainChar.checkCollision(backDoorLevel3) == True:
            scene = 3
            mainChar.xPos = 200
        
        # Make the goblin move if it is alive
        if goblin2.alive:
            goblin2.move()
            
            # Player takes damage if they walk into goblin
            if mainChar.checkCollision(goblin2):
                mainChar.currentHealth -= 0.5
        
        # Move bullets across screen and check if they hit the goblin
        for bullet in bulletsList:
            bullet.move(goblin2)
            
            # If the bullet hits the goblin or goes off screen, remove it 
            if not bullet.active:
                bulletsList.remove(bullet)

        # Check if any of the coins have been collected in level 3
        for coin in coinListLevel3:
            
            # Allow player to collect coin if not collected before
            if mainChar.checkCollision(coin) == True and coin.active == True:
                coin.active = False                    
                coinCounter += 10
                
        # Allow player to collect big coin if not collected before
        if mainChar.checkCollision(bigCoin2) == True and \
            bigCoin2.active == True:
            bigCoin2.active = False
            coinCounter += 50
    
    elif scene == 5:
        
        # Check if any of the coins have been collected in level 4
        for coin in coinListLevel4:
            
            # Allow player to collect coin if not collected before
            if mainChar.checkCollision(coin) == True and coin.active == True:
                coin.active = False
                coinCounter += 10
        
        # Move bullets across screen and check if they hit goblin within level
        for bullet in bulletsList:
            bullet.move(goblin2)
            
            # Remove bullet if it hits the goblin or goes off screen
            if not bullet.active:
                bulletsList.remove(bullet)
    
    elif scene == 6:
        
        # Move the zombie and have the scared person return when its dead
        if zombie.alive:
            zombie.changeX = random.randrange(-3, 3)
            zombie.move()
        else:
            scaredPerson.move()

            # Stop the scared person moving in the middle of the screen
            if scaredPerson.xPos >= 200:
                scaredPerson.changeX = 0
        
        # Make zombie smelly by moving stink particles around it
        for particle in stinkParticlesZombie:
            particle.move()
            
            # Player takes damage if they walk into any of its stink particles
            if mainChar.checkCollision(particle):
                   mainChar.currentHealth -= 5
                   stinkParticlesZombie.remove(particle)
        
        # Move bullets across screen and check if they hit the zombie
        for bullet in bulletsList:
            bullet.move(zombie)
            
            # If the bullet hits the zombie or goes off screen, remove it 
            if not bullet.active:
                bulletsList.remove(bullet)
    
    elif scene == 7:
        
        # Move the rotten food and have the scared person return when its dead
        if rottenFood.alive:
            rottenFood.changeX = random.randrange(-3, 4)
            rottenFood.move()
        else:
            scaredPerson.move()
            
            # Stop the scared person moving in the middle of the screen
            if scaredPerson.xPos >= 200:
                scaredPerson.changeX = 0
        
        # Make rotten food smelly by moving stink particles around it
        for particle in stinkParticlesRottenFood:
            particle.move()
            
            # Player takes damage if they walk into any of its stink particles
            if mainChar.checkCollision(particle):
                   mainChar.currentHealth -= 5
                   stinkParticlesRottenFood.remove(particle)
        
        # Move bullets across screen and check if they hit rotten egg
        for bullet in bulletsList:
            bullet.move(rottenFood)
            
            # If the bullet hits rotten food or goes off screen, remove it
            if not bullet.active:
                bulletsList.remove(bullet)
    
    # Check each monster
    for monster in monstersList:
        
        # Monster is dead if it has no health
        if monster.currentHealth <= 0:
            monster.alive = False

    # User can only move when animation scene is over
    if userControl == True:
        mainChar.move()
    else:
        mainChar.animateMove()

    ## VIEW
    # Clear screen
    screen.fill(WHITE)
    
    # Draw
    # Draw each scene and its components based on scene number
    if scene == 1:
        
        # Draw backgrounds based on user clicks
        if clickNum <= 2:
            screen.blit(forest, [0,0])
        elif clickNum > 2:
            screen.blit(imageIntro, [0,0])
        
        # Draw scared person in front of house
        if clickNum >= 3:
            door1.draw(screen)
            scaredPerson.drawEntity(scaredPersonImg, screen)
        
        # Show dialogue
        if 0 <= clickNum <= 6:
            displayDialogue(clickNum, screen)
    
    elif scene == 2:
        room1.draw(screen)
        door2.draw(screen)
        
        # Draw each piece of furniture
        for furniture in furnitureRoom1:
            furniture.draw(screen)
        
        # Check for each mystery box
        for box in boxListLevel1:
            
            # Draw boxes
            if box.active:
                box.drawEntity(boxImg, screen)

        # Draw spider and its health bar
        if spider.alive:
            spider.drawEntity(spiderImg, screen)
            spider.drawHealthBar(screen)
        
        # Draw skunk and its health bar
        if skunk.alive:
            skunk.drawEntity(skunkImg, screen)
            skunk.drawHealthBar(screen)
        
        # Gather all coins stored
        for coin in coinListLevel1: 
              
            # Draw coin
            if coin.active == True:
                coin.drawEntity(coinImg, screen)
        
        # Draw text when mouse hovers over door 
        if door2.hover(mousePos) ==True:
            door2.displayNextLevel(screen)
        
        # Draw stink particles around skunk
        for particle in stinkParticlesSkunk:
               particle.draw(screen)

    # Kitchen
    elif scene == 3:
        room2.draw(screen)
        pygame.draw.rect(screen, LIGHTGREY, [0, floorHeight-125, 800,125])
        backDoorLevel2.draw(screen)
        screen.blit(dishwasher, [500,floorHeight- 125])
        screen.blit(chandeleir, [350, 0])

        # Draw furniture
        for furniture in furnitureRoom2:
            furniture.draw(screen)
        
        # Check mystery boxes 
        for box in boxListLevel2:
            
            # Draw boxes
            if box.active:
                box.drawEntity(boxImg, screen)
                
        # Show text when mouse hovers over door
        if backDoorLevel2.hover(mousePos) == True:
            backDoorLevel2.displayPreviousLevel(screen, -300)
        elif door4.hover(mousePos) == True:
            door4.displayNextLevel(screen)
        
        # Draw goblin and its health bar
        if goblin1.alive == True:
            goblin1.drawEntity(goblinImg, screen)
            goblin1.drawHealthBar(screen)
        
        # Check all coins
        for coin in coinListLevel2:

            # Draw coins
            if coin.active == True:
                coin.drawEntity(coinImg, screen)
        
        # Draw big coin
        if bigCoin.active == True:
            bigCoin.drawEntity(coinBigImg, screen)

    elif scene == 4:
        room3.draw(screen)
        drawPoster(screen, -70)
        drawPoster(screen, 0)
        backDoorLevel3.draw(screen)
        door3.draw(screen)
        table3.draw(screen)
        window4.draw(screen)
        screen.blit(bed, [30,floorHeight- 187.5])
        
        # Check mystery boxes
        for box in boxListLevel3:
            
            # Draw boxes
            if box.active:
                box.drawEntity(boxImg, screen)
        
        # Show text when mouse hovers over door
        if backDoorLevel3.hover(mousePos) == True:
            backDoorLevel3.displayPreviousLevel(screen, -300)
        elif door3.hover(mousePos) == True:
            door3.displayFinalLevel(screen)

        # Draw goblin and its health bar
        if goblin2.alive == True:
            goblin2.drawEntity(goblinImg, screen)
            goblin2.drawHealthBar(screen)
        
        # Check all coins
        for coin in coinListLevel3:
            
            # Draw coin
            if coin.active:
                coin.drawEntity(coinImg, screen)
        
        # Draw big coin
        if bigCoin2.active:
            bigCoin2.drawEntity(coinBigImg, screen)

    elif scene == 5:
        room4.draw(screen)
        screen.blit(closet, [45,0])
        wardrobe5.draw(screen)
        wardrobe6.draw(screen)
        door5.draw(screen)
        door6.draw(screen)
        
        # Show text if mouse hovers over door
        if door5.hover(mousePos) == True:
            door5.bossFight(screen)
        elif door6.hover(mousePos) == True:
            door6.bossFight(screen)
        
        # Check each coin
        for coin in coinListLevel4:
            
            # Draw coins
            if coin.active:
                coin.drawEntity(coinImg, screen)
        
    elif scene == 6:
        screen.blit(bossFight1, [0, 0])
        pygame.draw.rect(screen, BLUE, [0,350,800,100])
        
        # Draw zombie and celebrate when its dead
        if zombie.alive == True:
            zombie.drawEntity(zombieImg, screen)
            zombie.drawHealthBar(screen)
        else:
            displayVictory(clickNum, screen)
            scaredPerson.drawEntity(scaredPersonImg, screen)
        
        # Draw each stink particle around zombie
        for particle in stinkParticlesZombie:
            particle.draw(screen)
    
    elif scene == 7:
        screen.blit(bossFight2, [0,0])
        pygame.draw.rect(screen, LIGHTGREY, [0,350,800,100])

        # Draw zombie and celebrate when it is dead
        if rottenFood.alive == True:
            rottenFood.drawEntity(rottenFoodImg, screen)
            rottenFood.drawHealthBar(screen)
        else:
            displayVictory(clickNum, screen)
            scaredPerson.drawEntity(scaredPersonImg, screen)
        
        # Draw each stink particle around rotten egg
        for particle in stinkParticlesRottenFood:
            particle.draw(screen)

    # After intro scene, show coin & health bar
    if scene >= 2:
        coinDisplay(screen)
        mainChar.drawHealthBar(screen)

    # Draw bullets shot
    for bullet in bulletsList:
        bullet.draw(screen)
    
    mainChar.drawEntity(mainCharImg, screen)

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()