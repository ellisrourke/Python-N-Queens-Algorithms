from queue import Queue
import copy

que = Queue()
goalStates = 0
initial_state = {
    "board": [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],

        "numQueens": 0,
}

goal_state = {
    "numQueens": 4
}

def goal_test(state):
    return state["numQueens"] == goal_state["numQueens"]

def checkPosition(position):
    #check all directions for a current queenz3
    #horizontal
    for i in range(4):
        if current_board[position[0]][i] == 1:
            return False
    #vertical
    for i in range(4):
        if current_board[i][position[1]] == 1:
            return False

    #diagonal
    
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

    for i in range(4):
        for j in range(4):
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
                        #for x in range(8):
                        #    print(new_state["board"][x])
                        #print(" ")
                        print("Goal State Reached")
                        goalStates+=1
                        #exit()

                    que.put(new_state)
                    visited[str(newBoard)] = True
print(goalStates,"goal states found")



