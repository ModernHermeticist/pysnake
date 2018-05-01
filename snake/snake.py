import random
import math
import pygame
from pygame.locals import *
from constants import *
from snakeclass import *
from screenclass import *


def main():

    screen = Screen()
    screen.start_screen()

    while True:

        snake = Snake()

        while True:

            snake.get_input()

            if snake.gameregulator == 6:
                snake.prevent_backtracking()

                snake.new_direction()

                snake.make_apple()

                snake.update_snake()

            snake.play(screen)

            if snake.snake_dead(screen) == 0:
                break


main()
