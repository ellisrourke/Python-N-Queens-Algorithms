import time
import numpy as np
import copy
import random

boardSize = int(input("Board Size: "))

#defining board data structure
currentBoard = {
    "board": [],
    "cost": 0}

#generate an initial state depending on specified board size
currentBoard["board"] = [[0 for i in range(boardSize)] for j in range(boardSize)]
for i in range(boardSize):
    currentBoard["board"][i][i] = 1

#shuffle rows of inital state so it is random
random.shuffle(currentBoard["board"])

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


    offset = -boardSize + 1
    #checks left to right diagonal for a queen from the current position
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



#set cost of current board
currentBoard["cost"] = evaluateCost(currentBoard)
bestBoard = currentBoard
#counter to track when to random restart
counter = 0
#until goalState is found...
while bestBoard["cost"]:
    #if counter ?= x: do random restart
    if(counter >= boardSize*2):
        random.shuffle(bestBoard["board"])
        counter = 0
    #generate new succesor board by swapping 2 random rows
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
    #check if successor is better than current best
    if succesor["cost"] < bestBoard["cost"]:
        bestBoard = succesor
#when goal state is found, print it
for i in range(boardSize):
    print(bestBoard["board"][i])
print(" ")

print("Time taken (secs) = ", time.process_time())
