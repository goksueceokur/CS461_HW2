from Node import Node

goal_state = [ [1, 2, 3, 4],
               [2, 3, 4, 5],
               [3, 4, 5, 5],
               [4, 5, 5, 0] ]

class Solver:
    def __init__(self):
        self.queue = []
        root_node = Node( [row[:] for row in goal_state], 0)
        root_node.shuffle() 
        self.queue.append(root_node) # Form one element queue consisting of a zero-length path containing only the root node
        self.states_reached = []
        self.upper_bound = 1000 # Sufficiently big number

    #Sorts the entire queue by the sum of path length and a lower-bound estimate of the cost remaining, with least cost paths in front
    def sort_queue(self):
        self.queue.sort(key=lambda x: x.estimation, reverse=False)

    def prune (self):
        for node in self.queue:
            if node.loop_check() or self.already_reached(node) or self.worse_than_upper_bound(node):
                self.queue.remove(node)

    def already_reached (self, newState):
        for state in self.states_reached:
            if newState.current == state.current:
                if state.steps < self.upper_bound:
                    return True
                else:
                    state = newState
        return False

    def worse_than_upper_bound(self, node):
        return node.estimation > self.upper_bound

    #CHANGE
    def solve(self):

        # Until the first path in the queue terminates at the goal node or the queue is empty,
        while(len(self.queue) != 0):
            #Remove the first path in the queue
            most_promising = self.queue.pop(0)

            # If the first path in the queue terminates at the goal node, announce success
            if most_promising.current == goal_state:
                most_promising.print_path()
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

            # Sort the entire queue by the sum of path length and a lower bound estimate of the cost remaining, with least cost paths in front
            self.sort_queue()

        # If the queue is empty and gal node is not found, announce failure
        return False 

if __name__ == "__main__":

    solver = Solver()
    result = solver.solve()
    if(result):
        print("Problem solved")
    else:
        print("Problem cannot be solved")