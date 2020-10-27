import random
goal_state = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 5],
             [4, 5, 5, 0]]

NUM_OF_MOVES = 38


class Node:

    def __init__( self, array, stepsTaken, path = []):
        self.current = [row[:] for row in array]
        self.steps = stepsTaken
        self.path = path
        self.estimation = self.estimate()

    def loop_check (self):
        if self.current in self.path:
            return True
    
    def shuffle(self):
        j = 0
        while j < NUM_OF_MOVES: # move(self, array, blank_x, blank_y, direction)
            chance = random.randint(1,4)

            if self.move(chance):
                j += 1

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
        children = []
        for i in range(1, 5):
            new_path = self.path[:]
            new_path.append(self)
            new_node = Node(self.current, self.steps + 1, new_path)
            if new_node.move(i):
                children.append(new_node)
        return children
            
    def move(self, direction): # 1: left, 2: right, 3: up, 4: down
        for i, row in enumerate(self.current):
            if 0 in row:
                blank_x, blank_y = i, row.index(0) # coordinates of the 0
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
    
    def __eq__(self, other): # TODO
        return

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


    def __repr__(self):
        cur = ''
        for row in self.current:
            for x in row:
                cur += (str(x) + ' ')
            cur += '\n'
        return "\ncurrent node: \n" + cur +"\nsteps Taken so far: " + str(self.steps) + "\nLower Bound of current node: " + str(self.estimation)