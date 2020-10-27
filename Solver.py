'''
CS 461 - Artificial Intelligence - Fall 2020 - Homework 2
Professor: Varol Akman
Group Name: PROMINI
Group Members:
    -Hakkı Burak Okumuş
    -Göksu Ece Okur
    -Yüce Hasan Kılıç

Solver class represents the solver mechanism for E-15 Puzzle.
Uses A* algorithm to solve the problem.
Program creates an initially solved puzzle and shuffles it.
Then, it creates all valid children (next states) from the first element of the queue and adds them to a queue in each step.

Redundant paths are pruned.
Pruning conditions:
    1. Estimated distance is longer than upper bound.
    2. State causes a loop.
    3. State is already reached from a shorter path. 

The queue is sorted based on estimated total path length of each state on each step.
Tree data structure is used to represent paths and find a solution (the shortest one).
Tries to reach the goal state from first element of the queue.
'''

from Node import Node

# Array representation of the goal state
goal_state = [ [1, 2, 3, 4],
               [2, 3, 4, 5],
               [3, 4, 5, 5],
               [4, 5, 5, 0] ]

class Solver:
    def __init__(self):
        self.queue = []
        root_node = Node( [row[:] for row in goal_state], 0) # Pass the goal state to create an initial puzzle
        root_node.shuffle() # Shuffle the puzzle
        self.queue.append(root_node) # Form one element queue consisting of a zero-length path containing only the root node
        self.states_reached = [] # Dynamic programming
        self.upper_bound = 1000 # Sufficiently big number
        self.max_queue_size = 1 

    # Sorts the entire queue by the sum of path length and a lower-bound estimate of the cost remaining, with least cost paths in front
    def sort_queue(self):
        self.queue.sort(key=lambda x: x.estimation, reverse=False)

    # Removes redundant paths from the queue on conditions discussed in the header
    def prune (self):
        for node in self.queue:
            if node.loop_check() or self.already_reached(node) or self.worse_than_upper_bound(node):
                self.queue.remove(node)

    # Checks if the state is already reached with fewer steps (Dynamic Programming)
    def already_reached (self, newState):
        for state in self.states_reached:
            if newState.current == state.current:
                if state.steps < self.upper_bound:
                    return True
                else:
                    state = newState
        return False

    # Checks if the path containing the state is estimated longer than current upper bound.
    def worse_than_upper_bound(self, node):
        return node.estimation > self.upper_bound

    # Implementation of A* algorithm using Branch and Bound and heuristics
    def solve(self):

        # Until the first path in the queue terminates at the goal node or the queue is empty,
        while(len(self.queue) != 0):
            #Remove the first path in the queue
            most_promising = self.queue.pop(0)

            # If the first path in the queue terminates at the goal node, announce success
            if most_promising.current == goal_state:
                most_promising.print_path()
                print("Maximum size of queue", self.max_queue_size)
                return True 
            
            # Create new paths by extending the first path to all the neighbors of the terminal node
            children = most_promising.generate_children()

            # Add new paths to the queue 
            for child in children:
                self.queue.append(child)

                # Update the current upper bound if goal node is reached
                if child.current == goal_state:
                    self.upper_bound = child.estimation

            # Reject loops and remove redundant paths
            self.prune()

            if(len(self.queue) > self.max_queue_size):
                self.max_queue_size = len(self.queue)

            # Sort the entire queue by the sum of path length and a lower bound estimate of the cost remaining, with least cost paths in front
            self.sort_queue()

        # If the queue is empty and gal node is not found, announce failure
        return False 

if __name__ == "__main__":
    puzzle = Solver()    
    print("Solution for puzzle")
    result = puzzle.solve()