initial_state = {
    "board": [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    "pos": [0,0],
    "cost": 0
}

def checkPosition(position):
    #check all directions for a current queenz3
    #horizontal
    for i in range(5):
        if initial_state["board"][position[0]][i] == 1:
            return False

    for i in range(5):
        if initial_state["board"][i][position[1]] == 1:
            return False

    return True

checkPos = [0,2]

print(checkPosition(checkPos))