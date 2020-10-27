from CS461HW2 import shuffle

goal_state = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 5],
             [4, 5, 5, 0]]


class Node:

    def __init__( self, array, stepsTaken, path = []):
        self.current = array
        self.steps = stepsTaken
        self.path = path
        self.estimation = self.estimate()

    def loop_check (self):
        if self.current in self.path:
            return True
    
    def steps_taken (self):
        self.steps = len(self.path)

    def heuristic1 (self, goal_state):
        i = 0
        j = 0
        
        while j != 4:
            k = 0 
            while k != 4:
                if self.current[j][k] != goal_state[j][k]:
                    i += 1
                k += 1
            j += 1
        return i

    def estimate (self):
        self.estimation = self.heuristic1(goal_state) + self.steps
        return self.estimation
    

    def generate_children(self):
        for i, row in enumerate(self.current):
            if 0 in row:
                blank_x, blank_y = i, row.index(0) # coordinates of the 0
        
        children = []
        for i in range(1, 5):
            new_array = [row[:] for row in self.current]
            if self.move(new_array, blank_x, blank_y, i):
                new_path = self.path[:]
                new_path.append(self)
                new_node = Node(new_array, self.steps + 1, new_path)
                children.append(new_node)
        return children
            
    def move(self, array, blank_x, blank_y, direction): # 0: left, 1: right, 2: up, 3: down
        if direction == 1: # move blank left
            if blank_x == 0:
                return False
            array[blank_x][blank_y], array[blank_x - 1][blank_y] = array[blank_x - 1][blank_y], array[blank_x][blank_y]
            blank_x -= 1
            return True
        elif direction == 2: # move blank right
            if blank_x == 3:
                return False
            array[blank_x][blank_y], array[blank_x + 1][blank_y] = array[blank_x + 1][blank_y], array[blank_x][blank_y]
            blank_x += 1
            return True
        elif direction == 3: # move blank up
            if blank_y == 0:
                return False
            array[blank_x][blank_y], array[blank_x][blank_y - 1] = array[blank_x][blank_y - 1], array[blank_x][blank_y]
            blank_y -= 1
            return True
        elif direction == 4: # move blank down
            if blank_y == 3:
                return False
            array[blank_x][blank_y], array[blank_x][blank_y + 1] = array[blank_x][blank_y + 1], array[blank_x][blank_y]
            blank_y += 1
            return True
    
    def __eq__(self, other): # TODO
        return

    def print_path(self):
        res = ''
        for node in self.path:
            ar = node.current
            for row in ar:
                for x in row:
                    cur += (str(x) + ' ')
                cur += '\n'
        print(res)
    def __repr__(self):
        cur = ''
        for row in self.current:
            for x in row:
                cur += (str(x) + ' ')
            cur += '\n'
        return "\ncurrent node: \n" + cur +"\nsteps Taken so far: " + str(self.steps) + "\nLower Bound of current node: " + str(self.estimation)
