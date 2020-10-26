import random

def shuffle(array):
    j=0
    while j != 10:
        chance = random.randint(1,4)
        i = 0
        blank = -1

        while blank == -1:
            Lists = array[i]

            if 0 in Lists:
                blank = Lists.index(0)

            else:
                i = i+1

        if chance == 1 and blank != 0: 
            Lists[blank], Lists[blank - 1] = Lists[blank - 1], Lists[blank]
            j= j + 1

        elif chance == 2 and blank != len(Lists) - 1: 
            Lists[blank], Lists[blank + 1] = Lists[blank + 1], Lists[blank]
            j= j + 1

        elif chance == 3 and i != len(array) - 1 : 
            array[i][blank], array[i + 1][blank] = array[i+1][blank], array[i][blank]
            j= j + 1

        elif chance == 4 and i != 0 : 
            array[i][blank], array[i - 1][blank] = array[i-1][blank], array[i][blank]
            j= j + 1
            
        # print("", array [0] , "\n" , array [1] , "\n" , array [2] ,  "\n" , array [3], "\n" )
    return array
        
        
       

goal_state = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [3, 4, 5, 5],
             [4, 5, 5, 0]]

print(shuffle(goal_state))
