import pygame, math
class Enemy(object):
    def __init__(self, x, y, image, velocity, health, target):
        self.x = x
        self.y = y
        self.x_dist = self.x - target.x
        self.y_dist = -(self.y - target.y)
        self.image = pygame.image.load(image)
        self.velocity = velocity
        self.health = health
        self.iframe = 0
        self.rotate = 0
        self.sprite = self.image
        self.hitbox = pygame.Rect(self.x - 31, self.y - 31, 63, 63)

    def __del__(self):
        return

    def chase(self, target):
        if target.y < self.y:
            self.y -= self.velocity
        if target.y > self.y:
            self.y += self.velocity
        if target.x < self.x:
            self.x -= self.velocity
        if target.x > self.x:
            self.x += self.velocity

        self.x_dist = self.x - target.x
        self.y_dist = -(self.y - target.y)

    def move(self, window, font):
        self.center = self.sprite.get_rect(center = (self.x, self.y))
        self.healthbar = font.render(' Health: ' + str(self.health)[:3], 1, (150, 0, 0), (0, 0, 0))
        window.blit(self.healthbar, (self.x - 30, self.y - 48))
        # pygame.draw.rect(window, (255, 0, 0), (self.hitbox))
        self.hitbox = pygame.Rect(self.x - 31, self.y - 31, 63, 63)
        self.rotate = math.degrees(math.atan2(self.y_dist, self.x_dist))
        self.sprite = pygame.transform.rotate(self.image, self.rotate)
        window.blit(self.sprite, self.center)

    def collision(self, bullets, player):
        for bullet in bullets:
            if self.hitbox.colliderect(bullet.hitbox) and self.iframe <= 0:
                if player.penetrate:
                    bullet.range -= 3
                    self.iframe = 50
                else:
                    bullets.pop(bullets.index(bullet))
                self.health -= player.damage

        self.iframe -= 1

    def dead(self):
        if self.health <= 0:
            return True