import numpy as np
from inputs import sudoku, harder_sudoku, killer_sudoku, cages
from UIHelper import init_view, update_view

def solve(grid, cages = []):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]
    if not empty_cells:
        print(np.matrix(grid))
        return True
    cell = min(empty_cells, key=lambda c: len(possible_values(c[0], c[1], grid, cages)))
    for value in possible_values(cell[0], cell[1], grid, cages):
        grid[cell[0]][cell[1]] = value
        update_view(grid)
        if solve(grid, cages):
            return True
        grid[cell[0]][cell[1]] = 0
    return False

def possible_values(y, x, grid, cages):
    impossible_values = set(grid[y][i] for i in range(9))
    impossible_values.update(grid[i][x] for i in range(9))
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3
    impossible_values.update(grid[i][j] for i in range(box_y, box_y+3) for j in range(box_x, box_x+3))

    # TODO: check cages contraint

    available_values = set(range(1, 10)) - impossible_values
    return available_values

def cage_is_full(cells, cell, grid):
    """
    check if all cells other than the provided one are empty
    """
    for c in cells:
        if c != cell and grid[c[0]][c[1]] == 0:
            return False
    return True

solve(harder_sudoku, cages)