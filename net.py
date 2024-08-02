import pygame
from pygame.locals import *
from constants import *
from vector import Vector2

class Net(object):
    def __init__(self, position):
        self.maxLength = 36
        self.active = False
        self.activationTime = None
        self.direction = None
        self.setSpeed(300)
        self.position = position
        print(self.position)
        self.centerConstantV = Vector2(12,0) # vertical const to get right-top position for net from guy position
        self.centerConstantH = Vector2(0,12) # horizontal const to get right-top position for net from guy position
        self.rect = Rect(self.position.asTuple(), (0, 0))
        self.characterWidth = 24 # TODO: change this and all references - rn this is stand in for character's width

    def activate(self, dt, looking):
        self.active = True
        self.activationTime = dt
        self.direction = looking

    def deactivate(self):
        self.rect.height = 0
        self.rect.width = 0
        self.active = False

    def setSpeed(self, speed):
        self.speed = speed * TILEWIDTH/32

    def isActive(self):
        return self.active
    
    def collide_circle(self, object):
        dx = self.rect.centerx 
        dy = self.rect.centery
        width = self.rect.width
        height = self.rect.height

        if dx > (width/2 + object.radius): return False
        if dy > (height/2 + object.radius): return False

        if dx <= width/2: return True
        if dy <= height/2: return True

        cornerDistance = (dx - width/2)**2 + (dy - height/2)**2
        return cornerDistance <= object.radius



    def update(self, dt, position):
        if self.active == True:
            if self.direction == DOWN:
                self.rect.update((position-self.centerConstantV).asTuple(),(self.rect.width, self.rect.height))
                self.rect.width = self.characterWidth
                if self.rect.height < self.maxLength:
                    self.rect.height += self.speed * dt
                else:
                    self.deactivate()
            elif self.direction == RIGHT:
                self.rect.update((position-self.centerConstantH).asTuple(),(self.rect.width, self.rect.height))
                self.rect.height = self.characterWidth
                if self.rect.width < self.maxLength:
                    self.rect.width += self.speed * dt
                else:
                    self.deactivate()
            elif self.direction == LEFT:
                if self.rect.width < self.maxLength:
                    dx = self.rect.width + (self.speed * dt)
                    p = position - self.centerConstantH + Vector2(-dx, 0)
                    self.rect.update(p.asTuple(), (dx, self.characterWidth))
                    self.rect.width = dx
                    self.rect.height = self.characterWidth
                else:
                    self.deactivate()
            elif self.direction == UP:
                if self.rect.height < self.maxLength:
                    dx = self.rect.height + (self.speed * dt)
                    p = position - self.centerConstantV + Vector2(0, -dx)
                    self.rect.update(p.asTuple(), (self.characterWidth, dx))
                    self.rect.height = dx
                    self.rect.width = self.characterWidth
                else:
                    self.deactivate()

                
    def render(self, screen):
        pygame.draw.rect(screen, RED, self.rect)