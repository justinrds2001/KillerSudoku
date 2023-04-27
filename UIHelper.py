import pygame
import time
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
LIGHT_BLUE = (128, 194, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 50
HEIGHT = 50

# This sets the margin between each cell
MARGIN = 5

# Initialize pygame
pygame.init()
pygame.display.set_caption("Sudoku") 

font = pygame.font.SysFont('Arial', 36)
size = (630, 630)
screen = pygame.display.set_mode(size)
cell_size = 70
font = pygame.font.SysFont("calibri", 50)

clock = pygame.time.Clock()
FPS = 10
clock.tick(FPS)


def init_view(grid, cages):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, (0, 0, 0))
                x_pos = j * cell_size + (cell_size - text.get_width()) / 2
                y_pos = i * cell_size + (cell_size - text.get_height()) / 2
                screen.blit(text, (x_pos, y_pos))
    for cage in cages:
        # make a random color in each iteration
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for i, j in cage[1]:
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size), 5)
            text = font.render(str(cage[0][0]), True, (0, 0, 0))
            x_pos = j * cell_size + (cell_size - text.get_width()) / 2
            y_pos = i * cell_size + (cell_size - text.get_height()) / 2
            screen.blit(text, (x_pos, y_pos))


def update_view(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                screen.fill((255, 255, 255), (j * cell_size, i * cell_size, cell_size, cell_size))
            else:
                text = font.render(str(grid[i][j]), True, (0, 0, 0))
                x_pos = j * cell_size + (cell_size - text.get_width()) / 2
                y_pos = i * cell_size + (cell_size - text.get_height()) / 2
                screen.fill((255, 255, 255), (j * cell_size, i * cell_size, cell_size, cell_size))
                screen.blit(text, (x_pos, y_pos))
    time.sleep(0.05)
    pygame.display.update()