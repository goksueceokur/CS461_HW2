import AStardeneme2


def branchAndBound(mostPromising):
    if mostPromising.current != goal_state:
        mostPromising.generateChild()

        for node in queue:
            node.prune()
    
    else:
        bestSoFar = mostPromising

    if queue != []:
        mostPromising = queue[1]
        return branchAndBound(mostPromising)
    
    else:
        return "best solution is found: " + bestSoFar


mostPromising = queue[1]
