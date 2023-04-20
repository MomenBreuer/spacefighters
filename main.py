import pygame
import math
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
background = pygame.image.load('background.jpeg')

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
enemies = []
num_enemies = 6

for i in range(num_enemies):
    enemy = pygame.image.load('enemy.png')
    enemyX = random.randint(0, 736)
    enemyY = random.randint(50, 150)
    enemyX_change = 0.2
    enemyY_change = 40
    enemies.append((enemy, enemyX, enemyY, enemyX_change, enemyY_change))

def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy[0], (enemy[1], enemy[2]))
# bullet
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 450
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


# creating font object
font = pygame.font.Font(None, 32)

# setting initial score to 0
score = 0

# game over font
game_over_font = pygame.font.Font(None, 64)

# game over loop flag
game_over = False

# checking if the game is running
running = True
while running:

    # background color
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))
    # because I love dark mode, IDK how some people can live and look at bright screens everyday
    # I mean, just read the advantages of it here https://blog.weekdone.com/why-you-should-switch-on-dark-mode/

    # render score text onto a surface
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))

    # blit score text onto screen
    screen.blit(score_text, (650, 10))
    # check for collision between player and enemy
    distance = math.sqrt((fighterX - enemyX)**2 + (fighterY - enemyY)**2)
    if distance < 27:
        is_collision = True
        game_over = True
        break  # exit the game loop if there is a collision


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighterX_change = -1.0
            if event.key == pygame.K_RIGHT:
                fighterX_change = 1.0
            if event.key == pygame.K_SPACE:
                print("space pressed")
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
        enemyX_change = 0.8
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.8
        enemyY += enemyY_change

    player(fighterX, fighterY)
    invader(enemyX, enemyY)

    # bullet movement
    if bullet_state == "fire":
        screen.blit(bullet, (fighterX + 16, bulletY))
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        # check for collision with enemy
        distance = math.sqrt((fighterX - enemyX) ** 2 + (bulletY - enemyY) ** 2)

        if distance < 27:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print("Hit!")
            enemyX = random.randint(0, 800)
            enemyY = random.randint(50, 150)

    pygame.display.update()
# after the game loop, display the game over screen
while game_over:

    # game over message
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(400, 300))

    # display the game over message
    screen.blit(game_over_text, game_over_rect)

    # display final score and keep the game over screen open


    final_score_text = font.render("Final Score: " + str(score), True, (255, 255, 255))
    final_score_rect = final_score_text.get_rect(center=(400, 350))
    screen.blit(final_score_text, final_score_rect)
    
    
    # update the screen
    pygame.display.update()

    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False  # exit the game over loop
    

# quit pygame
pygame.quit()
####################################################################
# game icon made by IYIKON [https://freeicons.io/profile/5876] from www.freeicons.io
# fighter design is made by ColourCreatype [https://freeicons.io/profile/5790] from www.freeicons.io
# enemy design is made by www.wishforge.games [https://freeicons.io/profile/2257] from www.freeicons.io

