from queue import Queue
import copy
import numpy as np

que = Queue()
goalStates = 0

initial_state = {
    "board": [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]],

        "numQueens": 0,
}

goal_state = {
    "numQueens": 8
}
'''
boardSize = int(input("Board Size: "))
nQueens = int(input("Number of Queens: "))

initial_state["board"] = [[0]*boardSize]*boardSize #collumn,row
goal_state["numQueens"] = nQueens
'''


def goal_test(state):
    return state["numQueens"] == goal_state["numQueens"]

def checkPosition(position):
    #print(position[0],position[1])

    #check all directions for a current queenz3
    #horizontal
    for i in range(8):
        if current_board[position[0]][i] == 1:
            return False
    #vertical
    for i in range(8):
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

    for i in range(8):
        for j in range(8):
            if(checkPosition([i,j])):
                newBoard = copy.deepcopy(current_board)
                newBoard[i][j] = 1

                if str(newBoard) in visited:
                    continue
                else:
                    new_state = {
                        "board": newBoard,
                        "numQueens": current_cost + 1
                    }

                    if goal_test(new_state):
                        for x in range(8):
                            print(new_state["board"][x])
                        print(" ")
                        #print("Goal State Reached")
                        goalStates+=1

                    que.put(new_state)
                    visited[str(newBoard)] = True
print(goalStates,"goal states found")


