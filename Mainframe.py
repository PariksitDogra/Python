import sys
import random


#
# 1   2  3  4
# 5   6  7  8
# 9  10 11 12
# 13 14 15 16 -- bottom of grid


def check_move_up(node):
    if node.positionHappyMan not in [1, 2, 3, 4]:
        return True
    else:
        return False


def check_move_right(node):
    if node.positionHappyMan not in [4, 8, 12, 16]:
        return True
    else:
        return False


def check_move_left(node):
    if node.positionHappyMan not in [1, 5, 9, 13]:
        return True
    else:
        return False


def check_move_down(node):
    if node.positionHappyMan not in [13, 14, 15, 16]:
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
        updatedPositionA += 4
    elif updatedPositionMan == updatedPositionB:
        updatedPositionB += 4
    elif updatedPositionMan == updatedPositionC:
        updatedPositionC += 4

    return [updatedPositionA, updatedPositionB, updatedPositionC, updatedPositionMan]


def move_down(node):
    updatedPositionA = node.positionA
    updatedPositionB = node.positionB
    updatedPositionC = node.positionC
    updatedPositionMan = node.positionHappyMan + 4

    if updatedPositionMan == updatedPositionA:
        updatedPositionA -= 4
    elif updatedPositionMan == updatedPositionB:
        updatedPositionB -= 4
    elif updatedPositionMan == updatedPositionC:
        updatedPositionC -= 4

    return [updatedPositionA, updatedPositionB, updatedPositionC, updatedPositionMan]


def reached_goal(node):
    if node.positionA == 6 and node.positionB == 10 and node.positionC == 14:
        # if node.positionB == 10:
        print("Goal Reached")
        return True
        # print("Total nodes expanded: " + )
        # print("Time taken: " + )
        # sys.exit()

    else:
        # print("Computer says no")

        return False


def set_node_cords(node, list):
    node.positionA = list[0]
    node.positionB = list[1]
    node.positionC = list[2]
    node.positionHappyMan = list[3]


    #  will move to node class + implementation of state system with storing of states being done in the object
    #  class instead of hard coded global variables


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


class Node(object):
    # node  has state object, stores the state of the board at that node

    def __init__(self):
        self.parent = None
        self.action = None
        self.positionHappyMan = None
        self.positionA = None
        self.positionB = None
        self.positionC = None
        self.depth = None
        self.nodes_have_expanded = None
        self.moves_to_do = None


def construct_node(node, move):
    new_cords = []
    parent = node
    if move == "Move Up":
        new_cords = move_up(node)
    elif move == "Move Down":
        new_cords = move_down(node)
    elif move == "Move Left":
        new_cords = move_left(node)
    elif move == "Move Right":
        new_cords = move_right(node)

    constructed_node = Node()
    constructed_node.parent = parent
    constructed_node.depth = parent.depth + 1
    constructed_node.positionA = new_cords[0]
    constructed_node.positionB = new_cords[1]
    constructed_node.positionC = new_cords[2]
    constructed_node.positionHappyMan = new_cords[3]
    constructed_node.action = move
    constructed_node.moves_to_do = get_legal_moves(constructed_node)
    constructed_node.nodes_have_expanded = []
    return constructed_node


def dfs():
    root_node = Node()
    root_node.depth = 0

    root_node.positionHappyMan = 16
    root_node.positionA = 13
    root_node.positionB = 14
    root_node.positionC = 15
    total_expanded = -1
    root_node.action = "No action"  # Change action

    stack = [root_node]

    while True:
        current_node = stack.pop()

        total_expanded += 1
        print("Nodes expanded: " + str(total_expanded))
        print("Current Node depth: " + str(current_node.depth) + " Action done: " + current_node.action)

        if reached_goal(current_node):
            print("Algorithm complete")
            break

        shuffled_moves = get_legal_moves(current_node)
        random.shuffle(shuffled_moves)

        for i in shuffled_moves:
            stack.append(construct_node(current_node, i))


def dfs_limited_search(max_depth=15):
    root_node = Node()
    root_node.depth = 0

    root_node.positionHappyMan = 16
    root_node.positionA = 13
    root_node.positionB = 14
    root_node.positionC = 15
    total_expanded = -1
    root_node.action = "No action"  # Change action

    stack = [root_node]

    while True:
        current_node = stack.pop()

        total_expanded += 1
        print("Nodes expanded: " + str(total_expanded))
        print("Current Node depth: " + str(current_node.depth) + " Action done: " + current_node.action)

        if reached_goal(current_node):
            print("Algorithm complete")
            break

        shuffled_moves = get_legal_moves(current_node)
        random.shuffle(shuffled_moves)
        if (current_node.depth < max_depth):
            for i in shuffled_moves:
                stack.append(construct_node(current_node, i))








def bfs():
    # set the root node here
    root_node = Node()
    root_node.depth = 0

    root_node.positionHappyMan = 16
    root_node.positionA = 13
    root_node.positionB = 14
    root_node.positionC = 15
    tree_expanded = []

    last_node_index = 0
    root_node.nodes_have_expanded = []
    root_node.moves_to_do = get_legal_moves(root_node)
    tree_expanded.append(root_node)

    # while not reached_goal(nodes_expanded[-1]):
    while True:
        for i in range(last_node_index, len(tree_expanded)):
            if len(tree_expanded[i].nodes_have_expanded) < len(tree_expanded[i].moves_to_do):
                # new node is expanded here
                # actions = list(set(tree_expanded[i].moves_to_do) - set(tree_expanded[i].nodes_have_expanded))
                if "Move Up" in tree_expanded[i].moves_to_do and "Move Up" not in tree_expanded[i].nodes_have_expanded:
                    move_done = "Move Up"
                elif "Move Down" in tree_expanded[i].moves_to_do and "Move Down" not in tree_expanded[
                    i].nodes_have_expanded:
                    move_done = "Move Down"
                elif "Move Left" in tree_expanded[i].moves_to_do and "Move Left" not in tree_expanded[
                    i].nodes_have_expanded:
                    move_done = "Move Left"
                elif "Move Right" in tree_expanded[i].moves_to_do and "Move Right" not in tree_expanded[
                    i].nodes_have_expanded:
                    move_done = "Move Right"
                # tree_expanded.append(construct_node(tree_expanded[i], actions[0]))
                tree_expanded.append(construct_node(tree_expanded[i], move_done))

                # tree_expanded[i].nodes_have_expanded.append(actions[0])
                tree_expanded[i].nodes_have_expanded.append(move_done)
                last_node_index = i
                break

        print("Nodes expanded: " + str(len(tree_expanded)))
        print("Current Node depth: " + str(tree_expanded[-1].depth) + " Action done: " + tree_expanded[-1].action)
        if reached_goal(tree_expanded[-1]):
            print("Algorithm complete")
            break


dfs()
