import numpy as np
'''
initial_state = {
    "board": [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]
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

checkPos = [2,3]

#print(checkPosition(checkPos))

#check up and left

if(checkPos[1] > 0):
    for i in range(checkPos[1],-1,-1):
        print(initial_state["board"][checkPos[0]-i][checkPos[1]-i])

print(np.diagonal(initial_state["board"],checkPos[1]-checkPos[0]))
newCheckPos = [checkPos[0],(len(initial_state["board"])-1-checkPos[1])]
print(np.fliplr(initial_state["board"]).diagonal(offset=newCheckPos[1]-newCheckPos[0]))

for i in range(len(initial_state["board"])):
    print(initial_state["board"][i])
'''
a = [0,0,0,0]
b = [0,0,0,0]

if(1 in a or 1 in b):
    print("True")
else:
    print("False")