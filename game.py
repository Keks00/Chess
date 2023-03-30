
from display import chess_board
from legal import checklegal
from display import reset
from functions import user_input
from risk_calc import if_risk
import os

def game_loop():
    slots = reset()
    game = True
    while game == True:
        move, pos, type = user_input(slots)
        legal, pos = checklegal(type,pos,move,slots)
        if legal == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            slots.update({f"{move}": "  "})
            slots.update({f"{pos}": type})
            chess_board(slots)
        if_risk(slots)

        
game_loop()