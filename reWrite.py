from queue import Queue
import copy
import numpy as np
import time
boardSize = int(input("Board Size: "))

que = Queue()
goalStates = 0

initial_state = {
    "board": [],

        "numQueens": 0,
}

goal_state = {
    "numQueens": boardSize
}

nQueens = int(input("Number of Queens: "))

initial_state["board"] = [[0 for i in range(boardSize)] for j in range(boardSize)]

def goal_test(state):
    return state["numQueens"] == goal_state["numQueens"]

def checkPosition(position):
    #print(position[0],position[1])

    #check all directions for a current queenz3
    #horizontal
    for i in range(boardSize):
        if current_board[position[0]][i] == 1:
            return False
    #vertical
    for i in range(boardSize):
        if current_board[i][position[1]] == 1:
            return False

    #diagonal
    newCheckPos = [position[0], (len(current_board) - 1 - position[1])]
    primary  = np.diagonal(current_board, position[1] - position[0])
    secondary = np.fliplr(current_board).diagonal(offset=newCheckPos[1] - newCheckPos[0])
    #print(primary,secondary)
    if(1 in primary or 1 in secondary):
        return False

    return True

que.put(initial_state)
visited = {
    str(initial_state["board"]): True
}
while not que.empty():
    ##
    state = que.get()
    current_board = state["board"]
    current_cost = state["numQueens"]
    usedCols = []
    usedRows = []
    for i in range(boardSize):
        if(i in usedCols):
            break
        for j in range(boardSize):
            if(j in usedRows):
                break
            if(checkPosition([i,j])):
                newBoard = copy.deepcopy(current_board)
                newBoard[i][j] = 1
                usedRows.append(j)
                usedCols.append(i)

                if str(newBoard) in visited:
                    continue
                else:
                    new_state = {
                        "board": newBoard,
                        "numQueens": current_cost + 1
                    }

                    if goal_test(new_state):
                        #for x in range(boardSize):
                        #    print(new_state["board"][x])
                        #print(" ")
                        #print("Goal State Reached")
                        goalStates+=1

                    que.put(new_state)
                    visited[str(newBoard)] = True
print(goalStates,"goal states found")
print("Time taken (secs) = ", time.process_time())


