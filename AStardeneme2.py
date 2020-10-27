from CS461HW2 import shuffle

goal_state = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 5],
             [4, 5, 5, 0]]


class Node:
    global statesReached
    global queue
    global goal_state
    global upperBound

    def __init__( self, array, stepsTaken, lowerBound, path = []):
        self.current = array
        self.steps = stepsTaken
        self.path = path
        self.estimate = lowerBound

    def loopChecking (self):
        if self.current in self.path:
            return "pruned"
    
    def dynamicProgramming (self):
        for state in statesReached:
            if self.current == state.current:
                if state.steps < self.steps:
                    return "pruned"
    
    def worseThanUpperBound(self, upperBound):
        if self.estimate >= upperBound:
            return "pruned"
    
    def prune (self):
        if self.loopChecking() == "pruned" or self.dynamicProgramming() == "pruned" or self.worseThanUpperBound(upperBound) == "pruned":
            queue.remove(self)
            print(self, "is removed from queue")
            return False #salak yücenin kafası karıştı #yine
        return True
    
    def setStatesReached (self, statesReached):
        if self not in statesReached:
            statesReached.append(self)

    def setQueue (self,queue):
        if self.prune():
            queue.append(self)      
            queue.sort(key=lambda x: x.lowerBound, reverse=True)
    
    def setSteps (self):
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

    def setLowerBound (self):
        self.estimate = self.heuristic1(goal_state) + self.steps
        return self.estimate
    

    def generateChild (self):
        blank = -1
        i = 0

        while blank == -1:
            Lists = self.current[i]

            if 0 in Lists:
                blank = Lists.index(0)

            else:
                i = i+1

        if blank != 0: 
            child1array = self.current
            child1array[i][blank] = self.current[i][blank-1]
            child1array[i][blank-1] = self.current[i][blank]
            child1Step = self.steps +1
            child1Path = self.path
            child1Path.append(self.current)
            child1 = Node(child1array, child1Step, 0, child1Path)
            child1.setLowerBound()
            child1.setQueue(queue)
            child1.setStatesReached(statesReached)
            child1.prune()

        if blank != len(Lists) - 1: 
            child2array = self.current
            child2array[i][blank] = self.current[i][blank+1]
            child2array[i][blank+1] = self.current[i][blank]
            child2Step = self.steps +1
            child2Path = self.path
            child2Path.append(self.current)
            child2 = Node(child2array, child2Step, 0, child2Path)
            child2.setLowerBound()
            child2.setQueue(queue)
            child2.setStatesReached(statesReached)
            child2.prune()

        if i != len(self.current) - 1 : 
            child3array = self.current
            child3array[i][blank] = self.current[i+ 1][blank]
            child3array[i +1][blank] = self.current[i][blank]
            child3Step = self.steps +1
            child3Path = self.path
            child3Path.append(self.current)
            child3 = Node(child3array, child3Step, 0, child3Path)
            child3.setLowerBound()
            child3.setQueue(queue)
            child3.setStatesReached(statesReached)
            child3.prune()

        if i != 0 : 
            child4array = self.current
            child4array[i][blank] = self.current[i - 1][blank]
            child4array[i - 1][blank] = self.current[i][blank]
            child4Step = self.steps +1
            child4Path = self.path
            child4Path.append(self.current)
            child4 = Node(child4array, child4Step, 0, child4Path)
            child4.setLowerBound()
            child4.setQueue(queue)
            child4.setStatesReached(statesReached)
            child4.prune()
    
    def __repr__(self):
        return "\n current node: " + self.current +"\n steps Taken so far: " + self.steps + "\n path: " + self.path + "\n Lower Bound of current node: " + self.estimate


start = Node(shuffle(goal_state), 0, 0)
start.setLowerBound()

statesReached = [start]
queue = [start]
upperBound = 1000

def branchAndBound(upperBound):
    mostPromising = queue[0]
    if mostPromising.current != goal_state:
        mostPromising.generateChild()

        for node in queue:
            node.prune()
    
    elif upperBound > mostPromising.steps :
        upperBound = mostPromising.steps
        queue.remove(mostPromising)

    if queue != []:
        return branchAndBound(upperBound)
    
    else:
        return "best solution is found: " + str(upperBound)

branchAndBound(upperBound)