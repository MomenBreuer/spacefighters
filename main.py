import pygame
import random

# def
def player(x, y):
    screen.blit(fighter, (x, y))


def invader(x, y):
    screen.blit(enemy, (x, y))


# init pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.jpg')

# title and icon of the game
pygame.display.set_caption("Space Fighters")
icon = pygame.image.load('icon_small.png')
pygame.display.set_icon(icon)

# fighter
fighter = pygame.image.load('fighter.png')
fighterX = 370
fighterY = 480
fighterX_change = 0

# enemy
enemy = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0

# checking if the game is running
running = True
while running:
    # background color
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    # because I love dark mode, IDK how some people can live and look at bright screens everyday
    # I mean, just read the advantages of it here https://blog.weekdone.com/why-you-should-switch-on-dark-mode/
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighterX_change = -0.3
            if event.key == pygame.K_RIGHT:
                fighterX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighterX_change = 0

    fighterX += fighterX_change
    if fighterX <= 0:
        fighterX = 0
    elif fighterX >= 736:
        fighterX = 736
    player(fighterX, fighterY)
    invader(enemyX, enemyY)
    pygame.display.update()

####################################################################
# Icon made by IYIKON [https://freeicons.io/profile/5876] from www.freeicons.io
# fighter design is made by ColourCreatype [https://freeicons.io/profile/5790] from www.freeicons.io
# enemy design is made by www.wishforge.games [https://freeicons.io/profile/2257] from www.freeicons.io
