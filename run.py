import pygame
from pygame.locals import *
from constants import *
from guy import Guy
from bug import BugGroup

class GameController(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0)
        self.background = None
        self.clock = pygame.time.Clock()

    def startGame(self):
        self.setBackground()
        self.guy = Guy()
        self.bugs = BugGroup()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def checkBugEvents(self):
        for bug in self.bugs:
            if bug.collide_rect(self.guy.net):
                print('hiiii')
                self.bugs.collect(bug)
        
    def update(self):
        dt = self.clock.tick(30) / 1000.0 
        self.checkBugEvents()
        self.checkEvents()
        self.guy.update(dt)
        self.bugs.update(dt)
        self.render()

    def render(self):
        self.screen.blit(self.background, (0,0))
        self.guy.render(self.screen)
        self.bugs.render(self.screen)
        pygame.display.update()

if __name__ == "__main__":
    game = GameController()
    game.startGame()
    while True:
        game.update()