import pygame
from pygame.locals import *
from constants import *
from vector import Vector2
from entity import Entity
from net import Net

class Guy(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.radius = 12
        self.color = GREEN
        self.position = Vector2(SCREENWIDTH/2, SCREENHEIGHT/2)
        self.setSpeed(200)
        self.paused = False
        self.net = Net(self.position)
        self.eye = self.position.copy() + Vector2(0,5)
        self.looking = DOWN

    def getDirection(self,looking=0):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        if looking: return self.looking
        return STOP
    
    def spacebar(self):
        key_pressed = pygame.key.get_pressed()
        return key_pressed[K_SPACE]

    def getEyePosition(self):
        if self.looking == LEFT:
            self.eye = self.position.copy() + Vector2(-10, -5)
        elif self.looking == RIGHT:
            self.eye = self.position.copy() + Vector2(10, -5)
        elif self.looking == UP:
            self.eye = self.position.copy() + Vector2(0, -10)
        elif self.looking == DOWN:
            self.eye = self.position.copy() + Vector2(0, -5)

    def update(self, dt):
        if self.spacebar() and not self.net.isActive():
            self.net.activate(dt, self.looking)
        self.net.update(dt, self.position)
        self.direction = self.getDirection()
        self.looking = self.getDirection(1)
        position = self.position + self.directions[self.direction]*self.speed*dt
        if not self.outOfBounds(position):
            self.position += self.directions[self.direction]*self.speed*dt
        self.getEyePosition()


    def render(self, screen):
        if self.net.isActive():
            self.net.render(screen)
        p = self.position.asInt()
        eye = self.eye.asInt()
        pygame.draw.circle(screen, self.color, p, self.radius)
        if self.looking != UP: pygame.draw.circle(screen, WHITE, eye, 5)
        if self.looking != UP: pygame.draw.circle(screen, BLACK, eye, 2)
