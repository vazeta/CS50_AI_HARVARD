"""
Tic Tac Toe Player
"""

import math
import copy
import random
X = "X"
O = "O"
EMPTY = None

class InvalidActionError(Exception):
    """Exception class"""
    pass


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_o = 0
    count_x = 0
    for l in board:
        for value in l:
            if(value == "X"):
                count_x+=1
            elif(value == "O"):
                count_o+=1
    
    if(count_x > count_o):
        return "O"
    elif(count_x == count_o):
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if(board[i][j] == None):
                possible_actions.add((i,j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise InvalidActionError(f"Invalid action: {action}")

    new_board = copy.deepcopy(board)
    cur_player = player(new_board)
    
    new_board[action[0]][action[1]] = cur_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontally
    for l in board:
        if (l.count("X") == 3):
            return "X"
        elif (l.count("O") == 3):
            return "O"
    
    # Vertically
    for j in range(0,len(board[0])):
        count_o = 0
        count_x = 0
        for i in range(0,len(board)):
            if(board[i][j] == "X"):
                count_x += 1
            elif(board[i][j] == "O"):
                count_o += 1

        if(count_x == 3):
            return "X"
        elif(count_o == 3):
            return "O"
    
    # Diagonally
    count_o = 0
    count_x = 0
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if(i == j):
                if(board[i][j] == "X"):
                    count_x += 1
                elif(board[i][j] == "O"):
                    count_o += 1
    
    if(count_x == 3):
        return "X"
    elif(count_o == 3):
        return "O"
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    
    for l in board:
        for value in l:
            if (value == None):
                return False
    
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == "X"):
        return 1
    elif(winner(board) == "O"):
        return -1
    else:
        return 0
    
def other_player(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"
    
def result_inverse(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise InvalidActionError(f"Invalid action: {action}")

    new_board = copy.deepcopy(board)
    cur_player = player(new_board)
    true_player = other_player(cur_player)
    
    new_board[action[0]][action[1]] = true_player

    return new_board
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    cur_player = player(board)
    print(cur_player)
    possible_actions = actions(board)
    for cur_action in possible_actions:
        current_board = result(board,cur_action)
        inverse_board = result_inverse(board,cur_action)
        print(f"{cur_action}->>>>{winner(current_board)}")
        if(winner(current_board) != None or winner(inverse_board) != None):
            return cur_action
    
    return random.choice(list(possible_actions))