import math
import random
import pygame
import time
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0

class Snake:
    def __init__(self, color, poss) -> None:
        self.turns = {}
        self.color = color
        self.head = Cube(poss)
        self.body = []
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                if keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                if keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                if keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

class Grid:
    def __init__(self, size = 500, rows = 20) -> None:
        self.screen = pygame.display.set_mode((size, size))
        self.rows = rows
        self.size = size
    
    def redraw_window(self):
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        pygame.display.update()
    
    def draw_grid(self):
        square_dim = self.size // self.rows
        x = 0
        y = 0

        for _ in range(self.rows):
            x += square_dim
            y += square_dim
            pygame.draw.line(self.screen, (255, 255, 255), (x, 0), (x, self.size))
            pygame.draw.line(self.screen, (255, 255, 255), (0, y), (self.size, y))

def main():
    screen = Grid()
    # snake = Snake((255, 0, 0), (10, 10))
    clock = pygame.time.Clock()
    flag = True

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        screen.redraw_window()

main()