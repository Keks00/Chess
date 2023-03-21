
from display import chess_board
from legal import checklegal
from display import reset
from functions import user_input

def game_loop():
    slots = reset()
    game = True
    while game == True:
        move, pos, type = user_input(slots)
        legal = checklegal(type,pos,move)
        if legal == True:
            slots.update({f"{pos}": type})
            slots.update({f"{move}": "  "})
            print("legal")
            chess_board(slots)
        else:
            print("illegal")
game_loop()