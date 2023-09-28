import pygame, math
from projectile import Projectile

class Player(object):
    def __init__(self, x, y, image, health):
        self.x = x
        self.y = y
        self.speed = 1.2
        self.velocity = self.speed
        self.rotate = 0
        self.mouse = pygame.mouse.get_pos()
        self.x_dist = self.mouse[0] - self.x
        self.y_dist = -(self.mouse[1] - self.y)

        self.up = pygame.K_w
        self.down = pygame.K_s
        self.left = pygame.K_a
        self.right = pygame.K_d
        self.sprint = pygame.K_SPACE

        self.image = pygame.image.load(image)
        self.sprite = self.image
        self.center = self.sprite.get_rect(center = (self.x, self.y))

        self.damage_boost = 1
        self.attacking = True
        self.bullets = []
        self.swings = []
        self.weapon(9, 10, 30, .65, 1.5, False, 'playerSMG.png', 50, 18)
        self.reload = self.fire_rate
        self.barrel = math.radians(self.rotate + math.degrees(-math.atan2(self.weapon_length, self.weapon_width)))
        self.barrelx = self.x + math.cos(self.barrel) * 53.14
        self.barrely = self.y - math.sin(self.barrel) * 53.14

        self.kills = 0
        self.regen_time = 390
        self.health = health
        self.iframe = 120
        self.hitbox = pygame.Rect(self.x - 31, self.y - 31, 63, 63)

    def controls(self):
        self.mouse = pygame.mouse.get_pos()
        self.x_dist = self.mouse[0] - self.x
        self.y_dist = -(self.mouse[1] - self.y)
        keys = pygame.key.get_pressed()

        # Movement Controls
        if keys[self.up]:
            self.y -= self.velocity
        if keys[self.down]:
            self.y += self.velocity
        if keys[self.left]:
            self.x -= self.velocity
        if keys[self.right]:
            self.x += self.velocity

        # Change weapons
        if keys[pygame.K_1]:
            self.weapon(9, 10, 30, .65,1.5,  False, 'playerSMG.png', 50, 18)
        if keys[pygame.K_2]:
            self.weapon(80, 20, 1280, 6.25, .6, False, 'playerSniper.png', 68, 20)
        if keys[pygame.K_3]:
            self.weapon(100, 30, 50, 2, 1, True, 'playerRevolver.png', 55, 20)
        if keys[pygame.K_4]:
            self.weapon(15, 30, 60, 1.1, 1.2, False, 'playerRifle.png', 59, 21)
        if keys[pygame.K_f]:
            self.weapon(5, 30, 600, 10, 2, True, 'playerRifle.png', 59, 21)

        if keys[self.sprint]:
            self.velocity = self.speed * 1.5
            self.attacking = False
        else:
            self.velocity = self.speed
            self.attacking = True

    # Define weapon attributes
    def weapon(self, fire_rate, bullet_vel, range, damage, mobility, penetrate, image, width, length):
        self.fire_rate = fire_rate
        self.reload = self.fire_rate
        self.bullet_vel = bullet_vel
        self.range = range
        self.damage = damage * self.damage_boost
        self.speed = mobility
        self.penetrate = penetrate
        self.image = pygame.image.load(image)

        self.weapon_width = width
        self.weapon_length = length
        self.barrel_dist = math.sqrt((self.weapon_width * self.weapon_width)
                                     + (self.weapon_length * self.weapon_length))
        # self.fire_sound = pygame.mixer.Sound(sound)

    def fire(self, window):
        self.barrel = math.radians(self.rotate) - math.atan2(self.weapon_length, self.weapon_width)
        self.barrelx = self.x + math.cos(self.barrel) * self.barrel_dist
        self.barrely = self.y - math.sin(self.barrel) * self.barrel_dist

        if self.attacking and self.reload <= 0:
            bullet = Projectile(self.barrelx, self.barrely, self.bullet_vel, self.mouse[0], self.mouse[1], self.range)
            self.bullets.append(bullet)
            self.reload = self.fire_rate
            # pygame.mixer.Sound.play(self.fire_sound)
        elif self.reload > 0:
            self.reload -= 1

    def regen(self):
        if self.health < 5 and self.regen_time <= 0:
            self.health += 1
            self.regen_time = 390
        elif self.health != 5 and self.regen_time > 0:
            self.regen_time -= 1

    def move(self, window):
        self.center = self.sprite.get_rect(center = (self.x, self.y))
        self.hitbox = pygame.Rect(self.x - 31, self.y - 31, 63, 63)
        self.rotate = math.degrees(math.atan2(self.y_dist, self.x_dist))
        self.sprite = pygame.transform.rotate(self.image, self.rotate)
        # pygame.draw.rect(window, (255, 0, 0), (self.hitbox))
        window.blit(self.sprite, self.center)

    def collision(self, enemies):
        if self.hitbox.collidelist(enemies) >= 0 >= self.iframe:
            self.health -= 1
            self.iframe = 90
        if self.iframe > 0:
            self.iframe -= 1