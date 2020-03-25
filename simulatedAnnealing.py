import time
import numpy as np
import copy
import random

#set initial parameters
boardSize = int(input("Board size: "))
t = 1000
c =  0.0000001

#calculates the cost of the current board based on how many queens can attack eachother
def evaluateCost(board):
    cost = 0

    #checking horizontal row for queens
    for i in range(boardSize):
        val = sum(board["board"][i])
        if(val > 1):
            cost+=val

    #checking vertical collumn for queens
    for i in range(boardSize):
        val = 0
        for j in range(boardSize):
            val+=board["board"][j][i]
        if val > 1: cost+=val

    #checks left to right diagonal for a queen from the current position
    offset = -boardSize + 1
    for i in range(boardSize*2):
        primary = (np.diagonal(board["board"],offset=offset))
        #secondary is the current board flipped on the vertical axis to check
        #for diagonals that run from right to left
        secondary = (np.fliplr(board["board"]).diagonal(offset=offset))
        offset+=1
        if(sum(primary) > 1):
            cost+=sum(primary)
        if(sum(secondary) > 1):
            cost+=sum(secondary)
    #return the number of queen collisions on the board
    return cost

#defining board data structure
currentBoard = {
    "board": [],
    "cost": 0
}

#generate an initial state depending on specified board size
currentBoard["board"] = [[0 for i in range(boardSize)] for j in range(boardSize)]
for i in range(boardSize):
    currentBoard["board"][i][i] = 1

#shuffle rows of inital state so it is random
random.shuffle(currentBoard["board"])



#set cost of current board
currentBoard["cost"] = evaluateCost(currentBoard)
bestBoard = currentBoard
#until problem reaches goal state
while t > 0:
    #decrement temperature by the cooling rate
    t *= c
    #generate a successor board and swap 2 random rows
    succesor =  copy.deepcopy(bestBoard)
    a = random.randint(0,boardSize-1)
    b = random.randint(0,boardSize-1)
    while b == a:
        b = random.randint(0,boardSize-1)
    temp = succesor["board"][a]
    succesor["board"][a] = succesor["board"][b]
    succesor["board"][b] = temp

    #evaluate the cost of the new board
    succesor["cost"] = evaluateCost(succesor)
    pval = 0
    #diff = the difference in cost between the current best board and the succesor
    diff = evaluateCost(succesor) - bestBoard["cost"]
    #if succesor is better than current best, make successor the new bestBoard
    #else based on some probability pval, sometime select the successor anyway
    if(diff < 0):
        bestBoard = succesor
    else:
        if(t>0):
            pval = np.exp(-diff/t )
            if random.random() <= pval:
                bestBoard = copy.deepcopy(succesor)
    #if goalState found, print and end program.
    if(bestBoard["cost"] == 0):
        for i in range(boardSize):
            print(bestBoard["board"][i])
        print(" ")
        break

print("Time taken (secs) = ", time.process_time())
