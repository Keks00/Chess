import operator


def if_board(slots,move):
    board = {}
    test_slot = 11
    while test_slot <= 88:
        match slots[f"{test_slot}"]:
            case "  ":
                board[test_slot] = 0
            case "♖ ":
                board[test_slot] = -3
            case "♘ ":
                board[test_slot] = -4
            case "♗ ":
                board[test_slot] = -5
            case "♔ ":
                board[test_slot] = -6
            case "♕ ":
                board[test_slot] = -7
            case "♙ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
                board[test_slot] = -2            #["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]
            case "♜ ":
                board[test_slot] = 3
            case "♞ ":
                board[test_slot] = 4
            case "♝ ":
                board[test_slot] = 5
            case "♚ ":
                board[test_slot] = 6
            case "♛ ":
                board[test_slot] = 7
            case "♟ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
                board[test_slot] = 2      

        if test_slot in range(18,88,10):
            test_slot += 3
        else:
            test_slot += 1
    moves = test_all(board,move)
    return moves


def test_all(board,best_move):
    possible_moves = {}
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]

#testing for a Queen or Rook in a good position
    runs = 1
    while runs <= 4:
        match runs:
            case 1:
                rel_pos_change = 1
            case 2:
                rel_pos_change = -1
            case 3:
                rel_pos_change = 10
            case 4:
                rel_pos_change = -10

        test_slot = best_move + rel_pos_change
        while test_slot in range(11,89) and test_slot not in out_of_range:
            last_slot = str(board[test_slot])[1:]
            if board[test_slot]["type"] in range(0,99):
                    break
            elif board[test_slot] in range(-9,0) and last_slot in ["3","7"]:
                 possible_moves[test_slot] = last_slot
            test_slot += rel_pos_change
        runs += 1

#testing for a Queen or bishop in a good position
    runs = 1
    test_slot = best_move
    while runs <= 4:
        match runs:
            case 1:
                rel_pos_change = 9
            case 2:
                rel_pos_change = -9
            case 3:
                rel_pos_change =  11
            case 4:
                rel_pos_change = -11

        test_slot = best_move + rel_pos_change
        while test_slot in range(11,89) and test_slot not in out_of_range:
            last_slot = str(board[test_slot])[1:]
            if board[test_slot] in range(0,99):
                    break
            elif board[test_slot] in range(-9,0) and last_slot in ["5","7"]:
                 possible_moves[test_slot] = last_slot
            test_slot += rel_pos_change
        runs += 1
#test in a 3x3 area around the best position in terms of points || King and pawn

    runs = 1
    test_slot = best_move
    while runs <= 8:
        match runs:
            case 1:
                test_slot = best_move + 9
            case 2:
                test_slot = best_move + -9
            case 3:
                test_slot = best_move + 11
            case 4:
                test_slot = best_move + -11
            case 5:
                test_slot = best_move + 1
            case 6:
                test_slot = best_move + -1
            case 7:
                test_slot = best_move + 10
            case 8:
                test_slot = best_move + -10
        try:
            last_slot = str(board[test_slot])[1:]        
            if board[test_slot] in range(-9,0) and last_slot == "6" or test_slot in [-9,-11] and last_slot == "2":
                possible_moves[test_slot] = last_slot
        except: ValueError
        runs += 1
# Checks for a Knight in reach
    runs = 1
    test_slot = best_move
    while runs <= 8:
        match runs:
            case 1:
                test_slot = best_move + 21
            case 2:
                test_slot = best_move + -21
            case 3:
                test_slot = best_move + 19
            case 4:
                test_slot = best_move + -19
            case 5:
                test_slot = best_move + 12
            case 6:
                test_slot = best_move + -12
            case 7:
                test_slot = best_move + 8
            case 8:
                test_slot = best_move + -8
        try:
            last_slot = str(board[test_slot])[1:]        
            if board[test_slot] in [range(-9,1),10] and last_slot == "4":
                possible_moves[test_slot] = last_slot
        except: ValueError
        runs += 1
    return possible_moves

def enemy_figue_choise(best_move,slots):
    moves = if_board(slots,best_move)
    if moves == {}:
        return moves,False
    for key,value in moves.items():
        match value:
            case "2":
                moves[key] = 10
            case "3":
                moves[key] = 50
            case "4": 
                moves[key] = 30
            case "5":
                moves[key] = 30
            case "6": 
                moves[key] = 900
            case "7":
                moves[key] = 90
    move = max(moves.items(), key=operator.itemgetter(1))[0]
    return move,True