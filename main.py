import pygame
import random


# def
def player(x, y):
    screen.blit(fighter, (x, y))


def invader(x, y):
    screen.blit(enemy, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))


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
enemyX_change = 0.2
enemyY_change = 40

# bullet
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

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

        # keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighterX_change = -0.3
            if event.key == pygame.K_RIGHT:
                fighterX_change = 0.3
            if event.key == pygame.K_SPACE:
                fire_bullet(fighterX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighterX_change = 0

    # boundaries
    fighterX += fighterX_change
    if fighterX <= 0:
        fighterX = 0
    elif fighterX >= 736:
        fighterX = 736

    # enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    player(fighterX, fighterY)
    invader(enemyX, enemyY)
    pygame.display.update()

    # bullet movement
    if bullet_state is "fire":
        fire_bullet(fighterX, bulletY)
        bulletY -= bulletY_change

####################################################################
# game icon made by IYIKON [https://freeicons.io/profile/5876] from www.freeicons.io
# fighter design is made by ColourCreatype [https://freeicons.io/profile/5790] from www.freeicons.io
# enemy design is made by www.wishforge.games [https://freeicons.io/profile/2257] from www.freeicons.io
