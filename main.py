from queue import Queue
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = Queue()


initial_state = {
    "board": [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0 ,1 ,0],
        [0, 0, 0, 0, 1],

    ],
    "pos": [0,0],
    "cost": 0
}

goal_state = {
    "board": [
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],

    ],
    "pos": []
}

n = int(input("input problem dimesion: "))
#initial_state["board"] = [[0]*n]*n #collumn,row

def checkPosition(position):
    #check all directions for a current queen
    #check horizontal
    for i in range(n):
        if current_board[position[0]][i] == 1:
            #print(current_board[position[0]][i])
            return False

    #check vertical
    for i in range(n):
        if current_board[i][position[1]] == 1:
            return False

    #check diagonal


    #position is allowed
    return True


def goalTest(board):
    return board["board"] == goal_state["board"]

q.put(initial_state)
visited = {
    str(initial_state["board"]): True
}

while not q.empty():
    state = q.get()
    current_board = state["board"]
    current_position = state["pos"]
    current_cost = state["cost"]
    x, y = current_position

    for i in range(4):

        newX = x + dx[i]
        newY = y + dy[i]

        if checkPosition([newX,newY]):
            print("pos found")
            newBoard = copy.deepcopy(current_board)
            #newBoard[newX][newY] = newBoard[x][y]
            #newBoard[x][y] = newBoard[newX][newY]
            newBoard[newX][newY] = 1

            for j in range(5):
                print(newBoard[j])

            if str(newBoard) in visited:
                continue
            else:
                new_state = {
                    "board": newBoard,
                    "pos": [newX, newY],
                    "cost": current_cost + 1
                }

                if goalTest(new_state):
                    print("Goal State Reached")








