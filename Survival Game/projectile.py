import pygame, math
class Projectile(object):
    def __init__(self, x, y, velocity, dir_x, dir_y, range):
        self.x = x
        self.y = y
        self.velocity = velocity

        self.dir_x = dir_x
        self.dir_y = dir_y
        self.angle = -(math.atan2(self.dir_y - self.y, self.dir_x - self.x))
        self.dx = math.cos(self.angle) * self.velocity
        self.dy = math.sin(self.angle) * self.velocity

        self.range = range
        self.sprite = pygame.image.load('bullet.png')
        self.hitbox = pygame.Rect(self.x - 3, self.y - 3, 6, 6)

    def __del__(self):
        return

    def shoot(self, window):
        self.x += self.dx
        self.y -= self.dy
        self.center = self.sprite.get_rect(center = (self.x, self.y))
        self.hitbox = pygame.Rect(self.x - 3, self.y - 3, 6, 6)
        window.blit(self.sprite, self.center)
        if self.range > 0:
            self.range -= 1