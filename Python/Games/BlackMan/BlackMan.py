# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_RETURN,
    K_p,
    KEYDOWN,
    QUIT,
)

pause = False

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    largeText = pygame.font.SysFont("Times",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
                
        gameDisplay.fill(white)
        

        Button("Continue",150,450,100,50,green,bright_green,unpause)
        Button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)  


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("Python/Games/runningMan-removebg-preview.png").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                random.randint(0, SCREEN_HEIGHT),
                random.randint(0, SCREEN_WIDTH),
            )
        )

    # Move the sprite based on user keypresses
    def update(self, pressed_keys, i):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -i)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, i)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-i, 0)
            self.image = pygame.transform.flip(self.image, True, False)
            pygame.display.update()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(i, 0)
            self.image = pygame.transform.flip(self.image, True, False)
            pygame.display.update()

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    #weapon function
    def attack(self):
        if pressed_keys[K_SPACE]:
            pass

class David(pygame.sprite.Sprite):
    def __init__(self):
        super(David, self).__init__()
        self.image = pygame.image.load("Python/Games/davidduke.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                random.randint(0, SCREEN_HEIGHT + 100),
                random.randint(0, 100),
            )
        )
        self.speed = random.randint(0, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, self.speed) #-self.speed
        self.speed
        if self.rect.right < 0:
            self.kill()

class KKK(pygame.sprite.Sprite):
    def __init__(self):
        super(KKK, self).__init__()
        self.image = pygame.image.load("Python/Games/kkk.jpg").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(0, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        self.speed
        if self.rect.right < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("Python/Games/ghost.jpg").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                random.randint(0, SCREEN_HEIGHT + 100),
                random.randint(0, 100),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, self.speed) #-self.speed
        self.speed
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load("Python/Games/cloud.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.image.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH + 20), #width
                random.randint(0, 100), #How tall the clouds start
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, 5) #Second number goes down
        if self.rect.right < 0:
            self.kill()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super(PowerUp, self).__init__()
        self.image = pygame.image.load("Python/Games/mlk.png").convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.image.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH + 20), #width
                random.randint(0, 100), #How tall the clouds start
            )
        )
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT / 2)

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, 5) #Second number goes down
        if self.rect.right < 0:
            self.kill()

# Setup for sounds. Defaults are good.
pygame.mixer.init()

pygame.init()

display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Khallid Konnections: Black Man')
clock = pygame.time.Clock()

# Define constants for the screen width and height
myfont = pygame.font.SysFont("Arial", 20)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 2000)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
ADDDAVID = pygame.USEREVENT + 3
pygame.time.set_timer(ADDDAVID, 3500)
ADDKKK = pygame.USEREVENT + 4
pygame.time.set_timer(ADDKKK, 5000)
ADDPowerUp = pygame.USEREVENT + 5
pygame.time.set_timer(ADDPowerUp, 7500)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
davids = pygame.sprite.Group()
kkk = pygame.sprite.Group()
powerup = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

pygame.mixer.music.load("/Users/khallidwilliams/Downloads/005 prod x dj 6ix4.mp3")
pygame.mixer.music.play(loops=-1)

end_it=False
while (end_it==False):
    screen.fill(black)
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("Welcome To Black Man", 1, (255, 0, 255))
    nlabel1=myfont.render("Press any key to start!", 2, (255, 255, 255))
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            end_it=True
    screen.blit(nlabel,(SCREEN_WIDTH/3,SCREEN_WIDTH/3))
    screen.blit(nlabel1,(SCREEN_WIDTH/3,SCREEN_WIDTH/2.3))
    pygame.display.flip()



# Main loop
count = 0
highScore = 0
while running:
    count += 1

    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

            if event.key == K_p:
                paused = True
                paused()
        
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        #Add a new david duke?
        elif event.type == ADDDAVID:
            # Create the new david and add it to sprite groups
            new_david = David()
            davids.add(new_david)
            all_sprites.add(new_david)

        #Add a new kkk?
        elif event.type == ADDKKK:
            # Create the new david and add it to sprite groups
            new_kkk = KKK()
            kkk.add(new_kkk)
            all_sprites.add(new_kkk)

        elif event.type == ADDPowerUp:
            # Create the new david and add it to sprite groups
            new_powerup = PowerUp()
            powerup.add(new_powerup)
            all_sprites.add(new_powerup)


    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys, 5)

    # Update enemy position
    enemies.update()
    clouds.update()
    davids.update()
    kkk.update()
    powerup.update()

    # Fill the background with purple
    #screen.fill((135, 206, 250))
    screen.fill((black))

    counttext = myfont.render("Score {0}".format(count+12), 1, (255,255,255))
    screen.blit(counttext, (200, 10))

    highScore = myfont.render("High Score {0}".format(count+12), 1, (255,255,255))
    screen.blit(highScore, (500, 10))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False
        messagebox.showinfo ('Exit Application','Your score is ' + str(count) + ' points',icon = 'info') 

    if pygame.sprite.spritecollideany(player, davids):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False
        messagebox.showinfo ('Exit Application','Your score is ' + str(count) + ' points',icon = 'info') 

    if pygame.sprite.spritecollideany(player, kkk):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False
        messagebox.showinfo ('Exit Application','Your score is ' + str(count) + ' points',icon = 'info')

    if pygame.sprite.spritecollideany(player, powerup):
        print('Power Up')
        powerup.remove()
        player.update(pressed_keys, 10)

#

    # Draw image at the new coordinates
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
    
# Done! Time to quit.
pygame.quit()