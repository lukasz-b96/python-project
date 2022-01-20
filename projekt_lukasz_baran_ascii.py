#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Autor: Łukasz Baran


import sys
import getopt
import random


class Cell:

    def __init__(self, x: int, y: int):
        # coordinates of this cell
        self.x = x
        self.y = y

        # visited status of this cell
        self.visited = False

        # adjacent walls of this cell
        self.walls = {"left": True, "right": True, "up": True, "down": True}

        # just for easier loops each direction
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # checks if the cell has any unvisited and possible neighbors cells
    # grid is the 2d array of cells
    def get_possible_adjacent_cells(self, given_grid: list):

        # directions in tuple, first value of tuple is a second index

        # array to return of possible_neighbors to walk
        possible_neighbors = []

        # for each directions
        for x, y in self.directions:

            # checks if that direction is on the grid (index out of range or negative value)
            if self.x + x in [len(given_grid), -1] or self.y + y in [-1, len(given_grid)]:
                continue

            # neighbor represents one cell
            neighbor = given_grid[self.y + y][self.x + x]

            # check if the cell was visited
            if neighbor.visited:
                continue

            # if the cell was not visited add it to an array of possible_neighbors
            possible_neighbors.append(neighbor)

        # return possible_neighbors
        return possible_neighbors


class CreateMazeDFS:

    def __init__(self):

        # size of the grid
        self.size = self.set_size()

        # generate grid of cells
        self.grid = [[Cell(x, y) for x in range(self.size)]
                     for y in range(self.size)]

        # start the algorithm during the initialization
        self.start_algorithm()

    def set_size(self):
        # setting a size that we want to generate
        size = 1
        print('(True size is: chosen "x" * 2 + 1)\n')
        while 1:
            try:
                size = int(input("Choose the size: "))
            except ValueError:
                print("That's not an int!")
                continue

            if size > 30:
                print("Choose number smaller than 30 (<= 30)")
                continue
            if size <= 1:
                print("Choose number bigger than 1 (> 1)")
                continue
            break
        print("\nGENERATED MAZE:")
        return size

    # removes wall between current cell and neighbor cell
    def remove_wall_between_cells(self,  current: Cell, selected: Cell):

        if (selected.x > current.x):  # selected is on the right, and current is on the left
            selected.walls["left"] = False  # selected left wall is deleted
            current.walls["right"] = False  # current right wall is deleted
        elif selected.x < current.x:  # REVERSE scenario X
            selected.walls["right"] = False  # REVERSE scenario X
            current.walls["left"] = False  # REVERSE scenario X
        elif selected.y > current.y:  # selected is under current
            selected.walls["up"] = False  # selected up wall is deleted
            current.walls["down"] = False  # current down wall is deleted
        else:  # REVERSE scenario Y
            selected.walls["down"] = False  # REVERSE scenario Y
            current.walls["up"] = False  # REVERSE scenario Y

    def start_algorithm(self):

        # set the starting point
        current = self.grid[0][0]

        # initialize a stack for dfs algorithm
        stack = []

        while True:

            # set the cell as visited
            current.visited = True

            # possible cells to visit
            neighbors_array = current.get_possible_adjacent_cells(self.grid)

            # check if neighbors_array is not empty
            # it means if the cell has possible adjecent cells
            if neighbors_array:

                # randomly choose on of the neighbor
                selected = random.choice(neighbors_array)

                # selected mark as visited
                selected.visited = True

                # add to stack current cell
                stack.append(current)

                # remove walls between those two cells
                self.remove_wall_between_cells(current, selected)

                # set this selected cell as a current
                current = selected

            # check if stack is not empty
            elif stack:
                # backtrack
                current = stack.pop()
            # end the algorithm
            else:
                break

    def draw(self):
        final = []
        final_size = self.size * 2 + 1
       # fill diagonal corners
       #        # #
       #
       #        # #
        for row in range(final_size):

            if row % 2 == 0:
                # even rows are: black white black white ....
                final.append(
                    ["  " if cell % 2 != 0 else "# " for cell in range(final_size)])
            else:
                # odd rows are all white
                final.append(["  "] * final_size)

        # generates maze: for size * 2 + 1
        for yindex, y in enumerate(self.grid):
            for xindex, x in enumerate(y):
                if x.walls['left']:
                    final[yindex * 2 + 1][xindex * 2] = "# "
                if x.walls['right']:
                    final[yindex * 2 + 1][xindex * 2 + 2] = "# "
                if x.walls['up']:
                    final[yindex * 2][xindex * 2 + 1] = "# "
                if x.walls['down']:
                    final[yindex * 2 + 2][xindex * 2 + 1] = "# "
        print("\n".join(["".join(x) for x in final]))
        return final, final_size


class Setup:
    def __init__(self, maze: list, size: int):
        self.maze = maze
        self.size = size

        # just for easier loops each direction
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.start = self.check_setup("starting")
        self.end = self.check_setup("ending")

    def check_setup(self, position):
        # check the correctness of the input
        x, y = 0, 0
        while 1:
            try:

                x = int(input("\nChoose " + position + " row: "))
            except ValueError:
                print("That's not an int!")
                continue

            if x >= self.size or x < 0:
                print("Choose again - Row out of range of this maze: ")
                continue

            try:

                y = int(input("Choose " + position + " column: "))
            except ValueError:
                print("That's not an int!")
                continue

            if y >= self.size or y < 0:
                print("Choose again - Column out of range of this maze: ")
                continue

            # check if the chosen position has at least one possible path " "
            possible = False
            if not x == self.size - 1:
                if self.maze[x+1][y] == "  ":
                    possible = True
            if not y == self.size - 1:
                if self.maze[x][y+1] == "  ":
                    possible = True
            if not x == 0:
                if self.maze[x-1][y] == "  ":
                    possible = True
            if not y == 0:
                if self.maze[x][y-1] == "  ":
                    possible = True

            if possible:
                return x, y
            else:
                print("Chosen "+position +
                      " position does not have path to get in\n")

    def get_positions(self):
        while 1:
            # check if chosen start is not the same as the chosen end
            if self.start == self.end:
                print(
                    "Ending positon is the same as the starting, Please choose different ending position")
            else:
                break
            self.end = self.check_set("ending")
        return self.start, self.end


class SolveMazeDFS:

    def __init__(self, maze: list, size: int, start: tuple, end: tuple, backtrack: bool, follow: bool):
        # correct the size (border + starting point)
        self.size = size

        # get the grid
        self.maze = maze

        # just for easier loops each direction
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # copy starting and ending points
        self.start = start
        self.end = end

        # flags for printing
        self.backtrack = backtrack
        self.follow = follow

    def printSolution(self, maze):
        print("\n".join(["".join(x) for x in maze]))

    def solve_maze_recursion(self, maze, x, y):

        # CHECK IF WE GOT THE GOAL
        if x == self.end[0] and y == self.end[1] and maze[x][y] == "  ":
            return True

        # Check if the current position is possible
        if x not in [self.size, -1] and y not in [-1, self.size] and maze[x][y] == "  ":

            # Check if the path is already visited
            if maze[x][y] == "+ ":
                return False

            # Add this position to current solution
            maze[x][y] = "+ "

            # Flags for printing steps
            if self.follow:
                self.printSolution(maze)
                print("")

            # DFS recursion for each direction
            for new_x, new_y in self.directions:
                if self.solve_maze_recursion(maze, x + new_x, y+new_y) == True:
                    return True

            # BACKTRACK
            maze[x][y] = "B "

            # Flags for printing backtrack
            if self.backtrack:
                print("BACKTRACK")
                self.printSolution(maze)
                print("")

            return False

    def solve_maze(self):

        # reference to self.grid
        maze = self.maze

        # setup starting and ending points
        maze[self.start[0]][self.start[1]] = "  "
        maze[self.end[0]][self.end[1]] = "  "

        # start the recursive function with given starting point
        if self.solve_maze_recursion(maze, self.start[0], self.start[1]) == False:
            print("Solution doesn't exist")
            self.printSolution(maze)
            return False

        # mark the starting end ending positions
        maze[self.start[0]][self.start[1]] = "S "
        maze[self.end[0]][self.end[1]] = "F "
        print("\nSOLUTION OF THE MAZE:")
        self.printSolution(maze)
        return True


if __name__ == "__main__":
    backtrack = False
    follow = False
    opt = ""

    print("Input the starting and the ending point to make this program work")
    opt = input("Do you want to print the backtracking? Type: 'y': ")
    if opt == "y":
        backtrack = True
    opt = input("Do you want to print all steps? Type 'y': ")
    if opt == "y":
        follow = True

    created_maze = CreateMazeDFS()
    final, final_size = created_maze.draw()

    sth = Setup(final, final_size)
    start, end = sth.get_positions()

    to_solve = SolveMazeDFS(final, final_size, start, end, backtrack, follow)
    to_solve.solve_maze()
