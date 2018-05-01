import random
import math
import pygame
from pygame.locals import *
from constants import *
from screenclass import *


class Snake(object):

    def __init__(self):

        self.snakexy = [300, 400]
        self.snakelist = [[300, 400], [280, 400], [260, 400]]
        self.direction = RIGHT  # 1=up,2=right,3=down,4=left
        self.clock = CLOCK
        self.score = 0

        self.snakedead = False

        self.newdirection = RIGHT

        self.gameregulator = 6

        self.gamepaused = 0

        self.appleonscreen = 0

        self.applexy = [0, 0]

        self.growsnake = 0
        self.snakegrowunit = 2

    def get_input(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            self.newdirection = LEFT
        if pressed_keys[K_d]:
            self.newdirection = RIGHT
        if pressed_keys[K_w]:
            self.newdirection = UP
        if pressed_keys[K_s]:
            self.newdirection = DOWN
        if pressed_keys[K_q]:
            self.snakedead = TRUE
        if pressed_keys[K_p]:
            self.gamepaused = 1

        # wait here if p key is pressed until p key is pressed again

        while self.gamepaused == 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_r]:
                self.gamepaused = 0
            self.clock.tick(10)

    def play(self, screen):

        screen.screen.fill(BLACK)
        # horizontals
        pygame.draw.line(screen.screen, GREEN, (0, 9), (799, 9), 20)
        pygame.draw.line(screen.screen, GREEN, (0, 590), (799, 590), 20)
        pygame.draw.line(screen.screen, GREEN, (0, 69), (799, 69), 20)
        # verticals
        pygame.draw.line(screen.screen, GREEN, (9, 0), (9, 599), 20)
        pygame.draw.line(screen.screen, GREEN, (789, 0), (789, 599), 20)

        # score
        font = pygame.font.SysFont("arial", 38)
        text_surface = font.render(
            "SNAKE          Score: " + str(self.score), True, GREEN)
        screen.screen.blit(text_surface, (50, 18))

        for element in self.snakelist:
            pygame.draw.rect(screen.screen, RED, Rect(element, BLOCKSIZE))
            pygame.draw.rect(screen.screen, WHITE, Rect(element, BLOCKSIZE), 1)

            # Draw the apple
        pygame.draw.rect(screen.screen, BLUE, Rect(self.applexy, BLOCKSIZE))

        # Flip the screen to display everything we just changed
        pygame.display.flip()

        self.gameregulator = self.gameregulator + 1

        self.clock.tick(75)

    def prevent_backtracking(self):

            # lets make sure we can't go back the reverse direction

        if self.newdirection == LEFT and not self.direction == RIGHT:
            self.direction = self.newdirection

        elif self.newdirection == RIGHT and not self.direction == LEFT:
            self.direction = self.newdirection

        elif self.newdirection == UP and not self.direction == DOWN:
            self.direction = self.newdirection

        elif self.newdirection == DOWN and not self.direction == UP:
            self.direction = self.newdirection

    def new_direction(self):

        if self.direction == RIGHT:
            self.snakexy[0] = self.snakexy[0] + SNAKESTEP
            if self.snakexy[0] > MAXX:
                self.snakedead = TRUE

        elif self.direction == LEFT:
            self.snakexy[0] = self.snakexy[0] - SNAKESTEP
            if self.snakexy[0] < MINX:
                self.snakedead = TRUE

        elif self.direction == UP:
            self.snakexy[1] = self.snakexy[1] - SNAKESTEP
            if self.snakexy[1] < MINY:
                self.snakedead = TRUE

        elif self.direction == DOWN:
            self.snakexy[1] = self.snakexy[1] + SNAKESTEP
            if self.snakexy[1] > MAXY:
                self.snakedead = TRUE

        if len(self.snakelist) > 3 and self.snakelist.count(self.snakexy) > 0:
            self.snakedead = TRUE

    def make_apple(self):

        if self.appleonscreen == 0:
            good = FALSE
            while good == FALSE:
                x = random.randrange(1, 39)
                y = random.randrange(5, 29)
                self.applexy = [int(x * SNAKESTEP), int(y * SNAKESTEP)]
                if self.snakelist.count(self.applexy) == 0:
                    good = TRUE
            self.appleonscreen = 1

    def update_snake(self):

        self.snakelist.insert(0, list(self.snakexy))
        if self.snakexy[0] == self.applexy[0] and self.snakexy[1] == self.applexy[1]:
            self.appleonscreen = 0
            self.score = self.score + 1
            self.growsnake = self.growsnake + 1
        elif self.growsnake > 0:
            self.growsnake = self.growsnake + 1
            if self.growsnake == self.snakegrowunit:
                self.growsnake = 0
        else:
            self.snakelist.pop()

        self.gameregulator = 0

    def snake_dead(self, screen):

        if self.snakedead == TRUE:
            screen.screen.fill(BLACK)
            font = pygame.font.SysFont("arial", 48)
            text_surface = font.render("GAME OVER", True, GREEN)
            screen.screen.blit(text_surface, (250, 200))
            text_surface = font.render(
                "Your Score: " + str(self.score), True, GREEN)
            screen.screen.blit(text_surface, (250, 300))
            font = pygame.font.SysFont("arial", 24)
            text_surface = font.render("Press q to quit", True, GREEN)
            screen.screen.blit(text_surface, (300, 400))
            text_surface = font.render("Press n to play again", True, GREEN)
            screen.screen.blit(text_surface, (275, 450))

            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]:
                    exit()
                if pressed_keys[K_n]:
                    return 0

                self.clock.tick(10)
