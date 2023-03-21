from functions import type_conversion
def checklegal(type_symbol,move,pos):
    type = type_conversion(type_symbol)
    legal = False
    #defines x and y for the position the move and the relative coordinate change
    px = int(str(pos)[1:])
    py = int(str(pos)[:1])
    mx = int(str(move)[1:])
    my = int(str(move)[:1])
    relx = mx - px
    rely = my - py

    #check for type
    if type == "rook":
        legal = check_rook(px,py,relx,rely,legal)
    elif type == "pawn":
        legal = check_pawn(px,py,relx,rely,legal)
    elif type == "bishop":
        legal = check_bishop(px,py,relx,rely,legal)
    elif type == "knight":
        legal = check_knight(px,py,relx,rely,legal)
    elif type == "queen":
        legal = check_queen(px,py,relx,rely,legal)
    elif type == "king":
        legal = check_king(px,py,relx,rely,legal)
    return legal


#check if the pos change from the pawn is legal
def check_pawn(px,py,relx,rely,legal):
    if rely == 1 and relx == 0:
        #!!! If enemy diagonal then relx == 1 and rely == 1/-1 is fine 
        #!!! First move pawn can move relx 2
        legal = checkboard(px,py,relx,rely,legal)
    return legal

#check if the pos change from the rook is legal
def check_rook(px,py,relx,rely,legal):
    if relx in range(-8,8) and rely == 0 or rely in range(-8,8) and relx == 0:
            legal = checkboard(px,py,relx,rely,legal)
    return legal

#check if the pos change from the bishop is legal 
def check_bishop(px,py,relx,rely,legal):
    if relx in range(-8,8) and rely == relx:
        legal = checkboard(px,py,relx,rely,legal)
    return legal

#check if the pos change from the knight is legal
def check_knight(px,py,relx,rely,legal):
    if relx in[-1,1] and rely in [-2,2] or relx in [-2,2] and rely in [-1,1]:
     legal = checkboard(px,py,relx,rely,legal)
    return legal

#check if the pos change from the queen is legal
def check_queen(px,py,relx,rely,legal):
    if relx in range(-8,8) and abs(rely) == abs(relx) or rely in range(-8,8) and relx == 0:
        legal = checkboard(px,py,relx,rely,legal)
    return legal

#check if the pos change from the king is legal
def check_king(px,py,relx,rely,legal):
    if relx in [-1,0,1] and rely in [-1,1]:
        legal = checkboard(px,py,relx,rely,legal)
    return legal


#check if the move is on the board
def checkboard(px,py,relx,rely,legal):
    if (px + relx) in range(1,9):
        if (py + rely) in range(1,9):
            return True 