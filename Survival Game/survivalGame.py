import pygame, math, random
from player import Player
from enemy import Enemy
pygame.init()

# Set display size
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('background.png')

title = pygame.font.SysFont('impact', 130, False)
header = pygame.font.SysFont('bahnshrift', 40, True)
font = pygame.font.SysFont('consolas', 12, True)

def display_update():
    screen.blit(background, (0, 0))

    player.move(screen)
    for enemy in enemies:
        enemy.move(screen, font)
    for bullet in player.bullets:
        bullet.shoot(screen)
        if bullet.range <= 0:
            player.bullets.pop(player.bullets.index(bullet))

    info = header.render('Health: ' + str(player.health) + '    Kills: ' + str(player.kills)
                         + '    Wave: ' + str(wave) + '    Enemies: ' + str(len(enemies)), 1, (255, 255, 255))
    screen.blit(info, (360, 40))

    pygame.display.update()

# Game Rules
wave = 1
player = Player(640, 360, 'playerSMG.png', 5)
enemies = []
for i in range(5):
    zombie = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT), 'enemy.png', .8,
                   float(random.randint(1, 4 + wave)), player)
    enemies.append(zombie)

playing = True

# Play game
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        playing = False

    if player.health > 0:
        zombies_spawned = int(player.kills / 5) + 5
        if len(enemies) <= 0:
            for i in range(zombies_spawned):
                zombie = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT),
                               'enemy.png', .6, float(random.randint(1 + wave, 4 + wave)), player)
                enemies.append(zombie)
            wave += 1
            player.damage_boost += .2

        player.controls()
        player.fire(screen)
        player.regen()

        hitboxes = []
        for enemy in enemies:
            enemy.chase(player)
            enemy.collision(player.bullets, player)
            hitboxes.append(enemy.hitbox)
            if enemy.dead():
                enemies.pop(enemies.index(enemy))
                player.kills += 1
        player.collision(hitboxes)

        display_update()
    else:
        lose_text = title.render(" You Died ", 1, (100, 0, 0), (0, 0, 0))
        screen.blit(lose_text, (385, 285))
        pygame.display.update()

pygame.quit()