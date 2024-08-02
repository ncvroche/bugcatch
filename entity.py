import pygame
from pygame.locals import *
from constants import *
from vector import Vector2

class Entity(object):
    def __init__(self):
        self.direction = STOP
        self.looking = DOWN
        self.radius = 10
        self.color = WHITE
        self.directions = {STOP:Vector2(), UP:Vector2(0, -1), DOWN:Vector2(0, 1), 
                           LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        self.position = Vector2(1, 1)
        self.setSpeed(100)

    def setSpeed(self, speed):
        self.speed = speed * TILEWIDTH/32

    def update(self, dt):
        self.position += self.directions[self.direction]*self.speed*dt

    def outOfBounds(self, position = None):
        if not position:
            position = self.position
        edge = position + self.directions[self.looking] * self.radius
        if edge.x <= 0 or edge.y <= 0 or edge.x >= SCREENWIDTH or edge.y >= SCREENHEIGHT:
            return True
        return False

    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)

    def collide_circle(self, object):
        distance = (self.position - object.position).magnitude()
        collideRadius = self.radius + object.radius 
        if collideRadius >= distance:
            return True
        return False
    
    def collide_rect(self, object):
        dx = abs(object.rect.centerx - self.position.x)
        dy = abs(object.rect.centery - self.position.y)
        width = object.rect.width
        height = object.rect.height

        if dx > (width/2 + self.radius): return False
        if dy > (height/2 + self.radius): return False

        if dx <= width/2: return True
        if dy <= height/2: return True

        cornerDistance = (dx - width/2)**2 + (dy - height/2)**2
        return cornerDistance <= self.radius**2
