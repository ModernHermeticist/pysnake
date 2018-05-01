import random, math, pygame
from pygame.locals import *
from constants import *


class Screen(object):

    def __init__(self):

        self.showstartscreen = TRUE
        self.screen = None
        self.clock = CLOCK

        self.s = [[180,120],[180,100],[160,100],
                  [140,100],[120,100],[100,100],
                  [100,120],[100,140],[100,160],
                  [120,160],[140,160],[160,160],
                  [180,160],[180,180],[180,200],
                  [180,220],[160,220],[140,220],
                  [120,220],[100,220],[100,200]]
        self.apple = [100,200]





    def start_screen(self):
        pygame.init()

        self.screen = pygame.display.set_mode(WINSIZE)

        pygame.display.set_caption('SNAKE')
        self.screen.fill(BLACK)

        pygame.draw.rect(self.screen,GREEN,Rect(self.apple,BLOCKSIZE))
        pygame.display.flip()
        self.clock.tick(8)

        for e in self.s:
            pygame.draw.rect(self.screen,GREEN,Rect(e,BLOCKSIZE))
            pygame.display.flip()
            self.clock.tick(8)

        font = pygame.font.SysFont("arial", 64)
        text_surface = font.render("NAKE", True, GREEN)
        self.screen.blit(text_surface, (220,180))
        font = pygame.font.SysFont("arial", 24)
        text_surface = font.render("Move the snake with the arrow keys to eat the apples", True, GREEN)
        self.screen.blit(text_surface, (50,300))
        text_surface = font.render("Avoid the walls and yourself !", True, GREEN)
        self.screen.blit(text_surface, (50,350))
        text_surface = font.render("Press s to start a new game - Press q to quit at any time", True, GREEN)
        self.screen.blit(text_surface, (50,400))
        text_surface = font.render("Press p to pause r to resume at any time", True, GREEN)
        self.screen.blit(text_surface, (50,450))

        pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_q]: quit()
            if pressed_keys[K_s]: return
            self.clock.tick(10)