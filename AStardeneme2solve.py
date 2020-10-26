import AStardeneme2


def branchAndBound(mostPromising):
    mostPromising = queue[0]
    if mostPromising.current != goal_state:
        mostPromising.generateChild()

        for node in queue:
            node.prune()
    
    elif bestSoFar.steps > mostPromising.steps :
        bestSoFar = mostPromising

    if queue != []:
        return branchAndBound(mostPromising)
    
    else:
        return "best solution is found: " + bestSoFar



