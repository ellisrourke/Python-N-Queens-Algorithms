from queue import Queue
import copy
import numpy as np
import time
boardSize = int(input("Board Size: "))

que = Queue()
goalStates = 0
exploredStates = 0

#defining board data structure
initial_state = {
    "board": [],
    "numQueens": 0,}

#define goal state
goal_state = {
    "numQueens": boardSize}

#generate an initial state depending on specified board size
initial_state["board"] = [[0 for i in range(boardSize)] for j in range(boardSize)]
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

#goal test function, checks in all queens are on board
def goal_test(state):
    return state["numQueens"] == goal_state["numQueens"]

#checks a given position to see if it is a valid move
def checkPosition(position):
    #checking horizontal row for any queens
    for i in range(boardSize):
        if current_board[position[0]][i] == 1:
            return False
    #checking vertical collumn for any queens
    for i in range(boardSize):
        if current_board[i][position[1]] == 1:
            return False

    #checks left to right diagonal for a queen from the current position
    newCheckPos = [position[0], (len(current_board) - 1 - position[1])]
    primary  = np.diagonal(current_board, position[1] - position[0])
    #secondary is the current board flipped on the vertical axis to check
    #for diagonals that run from right to left
    secondary = np.fliplr(current_board).diagonal(offset=newCheckPos[1] - newCheckPos[0])
    if(1 in primary or 1 in secondary):
        return False
    #if no queens found, return True
    return True

#push the initial state to the queue and mark it as visited
que.put(initial_state)
visited = {
    str(initial_state["board"]): True
}

while not que.empty():
    state = que.get()
    current_board = state["board"]
    current_cost = state["numQueens"]
    #tracks used collumns and rows (pruning)
    usedCols = []
    usedRows = []
    #check free positions on board for a valid position to place a queen
    for i in range(boardSize):
        if(i in usedRows):
            break
        for j in range(boardSize):
            if(j in usedCols):
                break
            exploredStates += 1
            #if it is a valid position, generate it as the new board
            if(checkPosition([i,j])):
                newBoard = copy.deepcopy(current_board)
                newBoard[i][j] = 1
                usedRows.append(j)
                usedCols.append(i)
                #break if board has been visited
                if str(newBoard) in visited:
                    break
                else:
                    new_state = {
                        "board": newBoard,
                        "numQueens": current_cost + 1
                    }
                    #if the state is a goal state, display if (n<=6) and push it to the que to be expanded
                    if goal_test(new_state):
                        if(boardSize <= 6):
                            for x in range(boardSize):
                                print(new_state["board"][x])
                            print(" ")
                        goalStates+=1
                    que.put(new_state)
                    visited[str(newBoard)] = True

#display results in console
print("")
print(goalStates,"goal states found")
print(exploredStates,"states explored")
print("")
print("Time taken (secs) = ", time.process_time())
print("")
