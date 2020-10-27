'''
CS 461 - Artificial Intelligence - Fall 2020 - Homework 2
Professor: Varol Akman
Group Name: PROMINI
Group Members:
    -Hakkı Burak Okumuş
    -Göksu Ece Okur
    -Yüce Hasan Kılıç

Node class represents a state for E-15 Puzzle.
A state keeps current grid as a 5x5 matrix.
A state keeps the previous states that leads to that state as a path.
A state keeps an estimated total distance of the shortest path including that state.

Formula for estimated total distance:
    Estimated total distance = Steps taken so far + Estimated number of steps remaining

Estimating is done using heuristics.
Heuristic formula:
    Underestimated number of remaining moves: number of misplaced tiles

It is an admissible heuristic for the 15-puzzle, since every tile that is out of position
must be moved at least once. In the best case, blank tile is moved towards the bottom-right corner without making loops
and each move places one tile in its correct position. In other words, each misplaced tile is apart from its correct position
by one position.

Constraint for moving the blank tile
    1. If blank tile is on the edge of a side, it cannot be moved towards that side.
'''

import random

# Array representation of the goal state
goal_state = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 5],
             [4, 5, 5, 0]]

# Number of moves to shuffle the path initially
NUM_OF_MOVES = 10 

class Node:
    def __init__( self, array, stepsTaken, path = []):
        self.current = [row[:] for row in array]
        self.steps = stepsTaken
        self.path = path
        self.estimation = self.estimate()

    # Check whether state is in its path i.e path contains a loop
    def loop_check (self):
        if self.current in self.path:
            return True
    
    # Shuffle the puzzle by making NUM_OF_MOVES random moves
    def shuffle(self):
        j = 0
        while j < NUM_OF_MOVES:
            chance = random.randint(1,4)

            # If move is valid, increase count; skip, otherwise
            if self.move(chance):
                j += 1 
        # Update the estimated length of path after the shuffle
        self.estimate()

    # Estimates the total length of the path using heuristic formula discussed in the header
    def heuristic1 (self, goal_state):
        i = 0
        j = 0
        
        # For each tile, compare it to the goal state and increment if it is misplaced.
        while j != 4:
            k = 0 
            while k != 4:
                if self.current[j][k] != goal_state[j][k]:
                    i += 1
                k += 1
            j += 1
            
        return i

    # Updates the estimation value of the state
    def estimate (self):
        self.estimation = self.heuristic1(goal_state) + self.steps
        return self.estimation
    
    # Generate next possible states by moving the blank tile in possible directions.
    # Returns list of generated children
    def generate_children(self):
        children = []
        for i in range(1, 5):
            new_path = self.path[:]
            new_path.append(self)
            new_node = Node(self.current, self.steps + 1, new_path)
            if new_node.move(i):
                children.append(new_node)
        return children
            
    # Moves the blank tile in given direction and updates the grid
    # Directions => 1: left, 2: right, 3: up, 4: down
    def move(self, direction): 
        for i, row in enumerate(self.current):
            if 0 in row:
                blank_x, blank_y = i, row.index(0) # coordinates of the blank tile
        if direction == 1: # move blank left
            if blank_x == 0:
                return False
            self.current[blank_x][blank_y], self.current[blank_x - 1][blank_y] = self.current[blank_x - 1][blank_y], self.current[blank_x][blank_y]
            blank_x -= 1
            return True
        elif direction == 2: # move blank right
            if blank_x == 3:
                return False
            self.current[blank_x][blank_y], self.current[blank_x + 1][blank_y] = self.current[blank_x + 1][blank_y], self.current[blank_x][blank_y]
            blank_x += 1
            return True
        elif direction == 3: # move blank up
            if blank_y == 0:
                return False
            self.current[blank_x][blank_y], self.current[blank_x][blank_y - 1] = self.current[blank_x][blank_y - 1], self.current[blank_x][blank_y]
            blank_y -= 1
            return True
        elif direction == 4: # move blank down
            if blank_y == 3:
                return False
            self.current[blank_x][blank_y], self.current[blank_x][blank_y + 1] = self.current[blank_x][blank_y + 1], self.current[blank_x][blank_y]
            blank_y += 1
            return True

    # Prints the states in the path and node itself at the end
    def print_path(self):
        res = ''
        for node in self.path:
            ar = node.current
            for row in ar:
                for x in row:
                    res += (str(x) + ' ')
                res += '\n'
            res += '------------\n'
        for row in self.current:
            for x in row:
                res += (str(x) + ' ')
            res += '\n'
        res += '------------\n'
        print(res)

    # Print the details of a single node
    # Used for debugging purposes
    def __repr__(self):
        cur = ''
        for row in self.current:
            for x in row:
                cur += (str(x) + ' ')
            cur += '\n'
        return "\n" + cur +"\nsteps Taken so far: " + str(self.steps) + "\nLower Bound of current node: " + str(self.estimation)