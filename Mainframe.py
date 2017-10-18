import sys


#
# 1   2  3  4
# 5   6  7  8
# 9  10 11 12
# 13 14 15 16 -- bottom of grid


def check_move_up(node):
    if node.positionHappyMan > 4:
        return True
    else:
        return False


def check_move_right(node):
    if node.positionHappyMan is not 4 and not 8 and not 12 and not 16:
        return True
    else:
        return False


def check_move_left(node):
    if node.positionHappyMan is not 1 and not 5 and not 9 and not 13:
        return True
    else:
        return False


def check_move_down(node):
    if node.positionHappyMan is not 13 and not 14 and not 15 and not 16:
        return True
    else:
        return False


# Will move right and swap 'positions' if the position its going to already has the block A,B,C on it
def move_right(node):
    updatedPositionA = node.positionA
    updatedPositionB = node.positionB
    updatedPositionC = node.positionC

    updatedPositionMan = node.positionHappyMan + 1

    if updatedPositionMan == updatedPositionA:
        updatedPositionA -= 1
    elif updatedPositionMan == updatedPositionB:
        updatedPositionB -= 1
    elif updatedPositionMan == updatedPositionC:
        updatedPositionC -= 1

    return [updatedPositionA, updatedPositionB, updatedPositionC, updatedPositionMan]


def move_left(node):
    updatedPositionA = node.positionA
    updatedPositionB = node.positionB
    updatedPositionC = node.positionC

    updatedPositionMan = node.positionHappyMan - 1

    if updatedPositionMan == updatedPositionA:
        updatedPositionA += 1
    elif updatedPositionMan == updatedPositionB:
        updatedPositionB += 1
    elif updatedPositionMan == updatedPositionC:
        updatedPositionC += 1

    return [updatedPositionA, updatedPositionB, updatedPositionC, updatedPositionMan]


def move_up(node):
    updatedPositionA = node.positionA
    updatedPositionB = node.positionB
    updatedPositionC = node.positionC

    updatedPositionMan = node.positionHappyMan - 4

    if updatedPositionMan == updatedPositionA:
        updatedPositionA + 4
    elif updatedPositionMan == updatedPositionB:
        updatedPositionB + 4
    elif updatedPositionMan == updatedPositionC:
        updatedPositionC + 4

    return [updatedPositionA, updatedPositionB, updatedPositionC, updatedPositionMan]


def move_down(node):
    updatedPositionA = node.positionA
    updatedPositionB = node.positionB
    updatedPositionC = node.positionC
    updatedPositionMan = node.positionHappyMan + 4

    if updatedPositionMan == updatedPositionA:
        updatedPositionA - 4
    elif updatedPositionMan == updatedPositionB:
        updatedPositionB - 4
    elif updatedPositionMan == updatedPositionC:
        updatedPositionC - 4

    return [updatedPositionA, updatedPositionB, updatedPositionC, updatedPositionMan]


def reached_goal():
    global positionHappyMan
    global positionA
    global positionB
    global positionC

    if positionA == 6 and positionB == 10 and positionC == 14 and positionHappyMan == 16:
        return True
        print("Goal Reached")
        # print("Total nodes expanded: " + )
        # print("Time taken: " + )
        # sys.exit()

    else:
        return False


def set_node_cords(list):
    current_node.positionA = list[0]
    current_node.positionB = list[1]
    current_node.positionC = list[2]
    current_node.positionHappyMan = list[3]


#  will move to node class + implementation of state system with storing of states being done in the object
#  class instead of hard coded global variables


class Node(object):
    # node acts as state object, stores the state of the board at that node

    def __int__(self):
        self.parent = None
        self.positionHappyMan = None
        self.positionA = None
        self.positionB = None
        self.positionC = None

    def get_legal_moves(node):
        legalMoves = []

        if check_move_right(node):
            legalMoves.append("Move Right")
        if check_move_down(node):
            legalMoves.append("Move Down")
        if check_move_left(node):
            legalMoves.append("Move Left")
        if check_move_up(node):
            legalMoves.append("Move Up")

        return legalMoves


def construct_node(move):
    global current_node
    new_cords = []
    parent = current_node
    if move == "Move Up":
        new_cords = move_up(current_node)
    elif move == "Move Down":
        new_cords = move_down(current_node)
    elif move == "Move Left":
        new_cords = move_left(current_node)
    elif move == "Move Right":
        new_cords = move_right(current_node)

    current_node = Node()
    current_node.parent = parent
    current_node.positionA = new_cords[0]
    current_node.positionB = new_cords[1]
    current_node.positionC = new_cords[2]
    current_node.positionHappyMan = new_cords[3]


def dfs():


current_node = Node()
set_node_cords([13, 14, 15, 16])
print(current_node.positionHappyMan)
print(current_node.positionC)
print("")
construct_node("Move Left")
print("")
print(current_node.positionHappyMan)
print(current_node.positionC)
print("")
print(current_node.parent.positionHappyMan)
print(current_node.parent.positionC)
