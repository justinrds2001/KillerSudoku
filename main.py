import numpy as np
from inputs import cages, grid, killer_grid

grid = grid
cage_index = {box: cage for cage in cages for box in cage[1]}
# cage_index = {} # uncomment this line to use the killer_grid

# sets the cage_index to None for all boxes that are not in a cage
for y in range(9):
    for x in range(9):
        if (y, x) not in cage_index:
            cage_index[(y, x)] = None


def solve():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n, grid, cage_index):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    inverted_grid = grid
    print(np.matrix(inverted_grid), end="\r")
    input("Press for enter to continue searching ...")


def is_duplicate_in_row(y, n, grid):
    for i in range(0, 9):
        if grid[y][i] == n:
            return True
    return False


def is_duplicate_in_column(x, n, grid):
    for i in range(0, 9):
        if grid[i][x] == n:
            return True
    return False


def is_duplicate_in_square(y, x, n, grid):
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return True
    return False


def is_cage_rule_correct(y, x, n, grid, cage_index):
    current_cage = cage_index[(y, x)]
    cage_values = []

    if not current_cage:
        return True

    for box_y, box_x in current_cage[1]:
        if box_y == y and box_x == x:
            cage_values.append(n)
        else:
            cage_values.append(grid[box_y][box_x])

    current_sum = sum(cage_values)
    if current_sum > current_cage[0]:
        return False

    all_valued = all(cage_values)
    if all_valued:
        # checks if the sum of the cage is correct
        if current_sum != current_cage[0]:
            return False
        # checks if there are duplicate values in the cage
        double_values = len(cage_values) != len(set(cage_values))
        if double_values:
            return False

    return True


def possible(y, x, n, grid, cage_index):
    if is_duplicate_in_row(y, n, grid):
        return False

    if is_duplicate_in_column(x, n, grid):
        return False

    if is_duplicate_in_square(y, x, n, grid):
        return False

    if not is_cage_rule_correct(y, x, n, grid, cage_index):
        return False

    return True


def invert_grid(grid):
    # inverts x and y axis
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]


solve()
