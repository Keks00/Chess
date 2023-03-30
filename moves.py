
def if_board(slots,move):
    board = {}
    test_slot = 11
    while test_slot <= 88:
        if slots[f"{test_slot}"] == "  ":
           board[test_slot] = 0
        elif slots[f"{test_slot}"] == "♖ ":
            board[test_slot] = 3
        elif slots[f"{test_slot}"] == "♘ ":
            board[test_slot] = 4
        elif slots[f"{test_slot}"] == "♗ ":
            board[test_slot] = 5
        elif slots[f"{test_slot}"] == "♔ ":
            board[test_slot] = 6
        elif slots[f"{test_slot}"] == "♕ ":
            board[test_slot] = 7
        elif slots[f"{test_slot}"] == "♙ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            board[test_slot] = 2            #["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]
        elif slots[f"{test_slot}"] == "♜ ":
            board[test_slot] = -3
        elif slots[f"{test_slot}"] == "♞ ":
            board[test_slot] = -4
        elif slots[f"{test_slot}"] == "♝ ":
            board[test_slot] = -5
        elif slots[f"{test_slot}"] == "♚ ":
            board[test_slot] = -6
        elif slots[f"{test_slot}"] == "♛ ":
            board[test_slot] = -7
        elif slots[f"{test_slot}"] == "♟ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            board[test_slot] = -2      

        if test_slot in range(18,88,10):
            test_slot += 3
        else:
            test_slot += 1
    board[74] = 
    test_slot = 11
    while test_slot <= 88:
        rewrite_slot = test_slot


        match board[test_slot]:
            case 3:
                 board = rook_board(board,move)
            case 4:
                 board = knight_board(board,move)
            case 5:
                 board = bishop_board(board,move)
            case 6:
                 board = queen_board(board,move)
            case 7:
                 board = king_board(board,move)
            case 2:
                 board = pawn_board(board,move)
        if test_slot in range(18,88,10):
            test_slot += 3
        else:
            test_slot += 1
        return board







def pawn_board(board,rewrite):
    rewrite_slot = rewrite
    try:
        if board[rewrite_slot + -11] in range(0,10):
            board[rewrite_slot + -11] += 10
        if board[rewrite_slot + -9] in range(0,10):
            board[rewrite_slot + -9] += 10  
    except:
         KeyError
    return board


def knight_board(board,rewrite):
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  
    rewrite_slot = rewrite

    try:
        if board[rewrite_slot + -12] in range(0,10):
            board[rewrite_slot + -12] += 10
        if board[rewrite_slot + -21] in range(0,10):
            board[rewrite_slot + -21] += 10
        if board[rewrite_slot + -19] in range(0,10):
            board[rewrite_slot + -19] += 10
        if board[rewrite_slot + -8] in range(0,10):
            board[rewrite_slot + -8] += 10
        if board[rewrite_slot + 8] in range(0,10):
            board[rewrite_slot + 8] += 10
        if board[rewrite_slot + 19] in range(0,10):
            board[rewrite_slot + 19] += 10
        if board[rewrite_slot + 21] in range(0,10):
            board[rewrite_slot + 21] += 10
        if board[rewrite_slot + 12] in range(0,10):
            board[rewrite_slot + 12] += 10
    except:
         KeyError
    return board

def king_board(board,rewrite):
    rewrite_slot = rewrite
    try:
        if board[rewrite_slot + -11] in range(0,10):
            board[rewrite_slot + -11] += 10
        if board[rewrite_slot + -10] in range(0,10):
            board[rewrite_slot + -10] += 10
        if board[rewrite_slot + -9] in range(0,10):
            board[rewrite_slot + -9] += 10
        if board[rewrite_slot + -1] in range(0,10):
            board[rewrite_slot + -1] += 10
        if board[rewrite_slot + 1] in range(0,10):
            board[rewrite_slot + 1] += 10
        if board[rewrite_slot + 9] in range(0,10):
            board[rewrite_slot + 9] += 10
        if board[rewrite_slot + 10] in range(0,10):
            board[rewrite_slot + 10] += 10
        if board[rewrite_slot + 11] in range(0,10):
            board[rewrite_slot + 11] += 10
    except:
        KeyError
    return board


def queen_board(board,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  


    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 9


    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 5:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 10

    return board

def bishop_board(board,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  


    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 4:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 4:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 4:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 4:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 9

    return board


def rook_board(board,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  


    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 2:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 2:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 2:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if board[rewrite_slot] in range(-9,0):
                break
        elif board[rewrite_slot] in range(0,10) and board[rewrite_slot] != 2:
            board[rewrite_slot] += 30
            if board[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 10

    return board

def enemy_figue_choise(best_move,slots):
    test = if_board(slots,best_move)
    print(test)