import time
import numpy as np
import copy
import random

boardSize = 20
    #int(input("Board Size: "))

def evaluateCost(board):
    cost = 0

    #horizontal cost
    for i in range(boardSize):
        val = sum(board["board"][i])
        if(val > 1):
            cost+=val


    for i in range(boardSize):
        val = 0
        for j in range(boardSize):
            val+=board["board"][j][i]
        if val > 1: cost+=val

    offset = -boardSize + 1
    for i in range(boardSize*2):
        primary = (np.diagonal(board["board"],offset=offset))
        secondary = (np.fliplr(board["board"]).diagonal(offset=offset))
        offset+=1
        if(sum(primary) > 1):
            cost+=sum(primary)
        if(sum(secondary) > 1):
            cost+=sum(secondary)
        #print(primary,secondary)
    return cost

currentBoard = {
    "board": [],
    "cost": 0
}

currentBoard["board"] = [[0 for i in range(boardSize)] for j in range(boardSize)]
for i in range(boardSize):
    currentBoard["board"][i][i] = 1
random.shuffle(currentBoard["board"])
for i in range(boardSize):
    print(currentBoard["board"][i])
print(" ")



currentBoard["cost"] = evaluateCost(currentBoard)
bestBoard = currentBoard
counter = 0
while bestBoard["cost"]:
    if(counter >= 10):
        random.shuffle(bestBoard["board"])
        counter = 0
    succesor =  copy.deepcopy(bestBoard)
    a = random.randint(0,boardSize-1)
    b = random.randint(0,boardSize-1)
    while b == a:
        b = random.randint(0,boardSize-1)

    temp = succesor["board"][a]
    succesor["board"][a] = succesor["board"][b]
    succesor["board"][b] = temp
    succesor["cost"] = evaluateCost(succesor)
    counter+=1
    if succesor["cost"] < bestBoard["cost"]:
        bestBoard = succesor

for i in range(boardSize):
    print(bestBoard["board"][i])
print(" ")
print("Time taken (secs) = ", time.process_time())
