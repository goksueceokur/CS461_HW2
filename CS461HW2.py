import random

NUM_OF_MOVES = 100000

def shuffle(array):
    for i, row in enumerate(array):
        if 0 in row:
            blank_x, blank_y = i, row.index(0) # coordinates of the 0
    
    for j in range(NUM_OF_MOVES):
        chance = random.randint(1,4)

        if chance == 1 and blank_x != 0: # move blank left
            array[blank_x][blank_y], array[blank_x - 1][blank_y] = array[blank_x - 1][blank_y], array[blank_x][blank_y]
            blank_x -= 1
        elif chance == 2 and blank_x != 3: # move blank right
            array[blank_x][blank_y], array[blank_x + 1][blank_y] = array[blank_x + 1][blank_y], array[blank_x][blank_y]
            blank_x += 1
        elif chance == 3 and blank_y != 0: # move blank up
            array[blank_x][blank_y], array[blank_x][blank_y - 1] = array[blank_x][blank_y - 1], array[blank_x][blank_y]
        elif chance == 4 and blank_y != 3: # move blank down
            array[blank_x][blank_y], array[blank_x][blank_y + 1] = array[blank_x][blank_y + 1], array[blank_x][blank_y]
    return array
        
        
       

goal_state = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 5],
             [4, 5, 5, 0]]

shuffled = shuffle(goal_state)
for row in shuffled:
    for i in row:
        print(i, end='   ')

    print()