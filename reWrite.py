from queue import Queue
import copy

que = Queue()

initial_state = {
    "board": [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]],
    "numQueens": 0,
}

goal_state = {
    "numQueens": 8
}

def goal_test(state):
    return state["numQueens"] == goal_state["numQueens"]

def checkPosition(position):
    #check all directions for a current queenz3
    #horizontal
    for i in range(5):
        if current_board[position[0]][i] == 1:
            return False

    for i in range(5):
        if current_board[i][position[1]] == 1:
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

    for i in range(5):
        for j in range(5):
            if(checkPosition([i,j])):
                newBoard = copy.deepcopy(current_board)
                newBoard[i][j] = 1

                for x in range(5):
                    print(newBoard[x])
                print(" ")
                if str(newBoard) in visited:
                    continue
                else:
                    new_state = {
                        "board": newBoard,
                        "numQueens": current_cost + 1
                    }

                    if goal_test(new_state):
                        print("Goal State Reached")
                        exit()

                    que.put(new_state)