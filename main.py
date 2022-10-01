import pygame


# def
def player():
    screen.blit(fighter, (fighterX, fighterY))


# init pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))

# title and icon of the game
pygame.display.set_caption("Space Fighters")
icon = pygame.image.load('icon_small.png')
pygame.display.set_icon(icon)

# fighter
fighter = pygame.image.load('fighter.png')
fighterX = 370
fighterY = 480

# checking if the game is running
running = True
while running:
    # background color
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # because I love dark mode, IDK how some people can live and look at bright screens everyday
    # I mean, just read the advantages of it here https://blog.weekdone.com/why-you-should-switch-on-dark-mode/
    player()
    pygame.display.update()

# Icon made by IYIKON [https://freeicons.io/profile/5876] from www.freeicons.io
# fighter design are made by ColourCreatype [https://freeicons.io/profile/5790] from www.freeicons.io
