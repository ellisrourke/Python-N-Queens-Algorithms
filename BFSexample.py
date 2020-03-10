from queue import Queue
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = Queue()

start_state = {
    "board": [
        [2, 8, 3],
        [1, 6, 4],
        [7, -1, 5]
    ],
    "pos": [2, 1],
    "cost": 0
}
goal_state = {
    "board": [
        [1, 2, 3],
        [8, -1, 4],
        [7, 6, 5]
    ],
    "pos": [1, 1]
}


def goal_test(s):
    return s["board"] == goal_state["board"]


def check_position(pos):
    return 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2


q.put(start_state)
visited = {
    str(start_state["board"]): True
}

while not q.empty():
    state = q.get()
    cur_board = state["board"]
    cur_pos = state["pos"]
    cur_cost = state["cost"]
    x, y = cur_pos

    for i in range(4):
        new_x, new_y = [x + dx[i], y + dy[i]]
        print(new_x,new_y)
        if check_position([new_x, new_y]):
            new_board = copy.deepcopy(cur_board)
            new_board[new_x][new_y], new_board[x][y] = new_board[x][y], new_board[new_x][new_y]

            if str(new_board) in visited:
                continue
            else:
                new_state = {
                    "board": new_board,
                    "pos": [new_x, new_y],
                    "cost": cur_cost + 1
                }

                if goal_test(new_state):
                    print("Reach goal state!")
                    print("Cost:", new_state["cost"])
                    exit()

                q.put(new_state)
                visited[str(new_board)] = True
