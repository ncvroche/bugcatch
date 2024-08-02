import pygame 
import random
from pygame.locals import *
from constants import *
from entity import Entity
from vector import Vector2

class Bug(Entity):
    def __init__(self, position):
        Entity.__init__(self)
        self.position = position
        self.maxTime = 30
        self.minTime = 11
        self.changeInst = 0
        self.timeInterval = 0
        self.direction = STOP
        self.setSpeed(50)
        self.dt = 0

    def collect(self):
        self.visible 

    def update(self,dt):
        self.dt += dt
        if (self.dt - self.changeInst) > self.timeInterval:
            self.timeInterval = random.randint(self.minTime, self.maxTime) / 10.0
            self.direction = random.randint(-2,2)
            self.looking = self.direction
            self.dt = 0
        position = self.position + self.directions[self.direction]*self.speed*dt
        if self.outOfBounds(position):
            self.direction *= -1
        else:
            self.position += self.directions[self.direction]*self.speed*dt




class BugGroup(object):
    def __init__(self):
        self.bugs=[Bug(Vector2(SCREENWIDTH - random.randint(6, SCREENHEIGHT), SCREENHEIGHT - random.randint(6, SCREENHEIGHT))), 
                   Bug(Vector2(SCREENWIDTH - random.randint(6, SCREENHEIGHT), SCREENHEIGHT - random.randint(6, SCREENHEIGHT))),
                   Bug(Vector2(SCREENWIDTH - random.randint(6, SCREENHEIGHT), SCREENHEIGHT - random.randint(6, SCREENHEIGHT)))]

    def __iter__(self):
        return iter(self.bugs)
    
    def collect(self, bug):
        self.bugs.pop(self.bugs.index(bug))

    def update(self, dt):
        for bug in self:
            bug.update(dt)
        
    def render(self, screen):
        for bug in self:
            bug.render(screen)