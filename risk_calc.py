
from score_calc import calc_values
def pawn_risks(risks,rewrite):
    rewrite_slot = rewrite
    try:
        if risks[rewrite_slot + -11] in range(0,10):
            risks[rewrite_slot + -11] += 10
        if risks[rewrite_slot + -9] in range(0,10):
            risks[rewrite_slot + -9] += 10  
    except:
         KeyError
    return risks


def knight_risk(risks,rewrite):
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  
    rewrite_slot = rewrite

    try:
        if risks[rewrite_slot + -12] in range(0,10):
            risks[rewrite_slot + -12] += 10
        if risks[rewrite_slot + -21] in range(0,10):
            risks[rewrite_slot + -21] += 10
        if risks[rewrite_slot + -19] in range(0,10):
            risks[rewrite_slot + -19] += 10
        if risks[rewrite_slot + -8] in range(0,10):
            risks[rewrite_slot + -8] += 10
        if risks[rewrite_slot + 8] in range(0,10):
            risks[rewrite_slot + 8] += 10
        if risks[rewrite_slot + 19] in range(0,10):
            risks[rewrite_slot + 19] += 10
        if risks[rewrite_slot + 21] in range(0,10):
            risks[rewrite_slot + 21] += 10
        if risks[rewrite_slot + 12] in range(0,10):
            risks[rewrite_slot + 12] += 10
    except:
         KeyError
    return risks

def king_risk(risks,rewrite):
    rewrite_slot = rewrite
    try:
        if risks[rewrite_slot + -11] in range(0,10):
            risks[rewrite_slot + -11] += 10
    except: KeyError
    try:
        if risks[rewrite_slot + -10] in range(0,10):
            risks[rewrite_slot + -10] += 10
    except: KeyError
    try:
        if risks[rewrite_slot + -9] in range(0,10):
            risks[rewrite_slot + -9] += 10
    except: KeyError
    try:
        if risks[rewrite_slot + -1] in range(0,10):
            risks[rewrite_slot + -1] += 10
    except: KeyError
    try:
        if risks[rewrite_slot + 1] in range(0,10):
            risks[rewrite_slot + 1] += 10
    except: KeyError
    try:
        if risks[rewrite_slot + 9] in range(0,10):
            risks[rewrite_slot + 9] += 10
    except: KeyError
    try:
        if risks[rewrite_slot + 10] in range(0,10):
            risks[rewrite_slot + 10] += 10
    except: KeyError
    try:
        if risks[rewrite_slot + 11] in range(0,10):
            risks[rewrite_slot + 11] += 10
    except:KeyError
    return risks


def queen_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  

    rewrite_slot += 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    rewrite_slot -= 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break 
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    rewrite_slot += 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    rewrite_slot -= 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot -= 9
    rewrite_slot = rewrite

    rewrite_slot += 1
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    rewrite_slot -= 1
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    rewrite_slot += 10
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    rewrite_slot -= 10
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot -= 10

    return risks

def bishop_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  

    rewrite_slot += 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    rewrite_slot -= 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    rewrite_slot += 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    rewrite_slot -= 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot -= 9
    return risks


def rook_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  


    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot]["type"] in range(-9,0):
                risks[rewrite_slot]["risky"] = True
                break
        elif risks[rewrite_slot]["type"] in range(0,10) :
            risks[rewrite_slot]["risky"] = True
            if risks[rewrite_slot]["type"] not in range(0,11):
                 break
        rewrite_slot -= 10
    return risks



def if_risk(slots):
    risks = {}
    test_slot = 11
    while test_slot <= 88:
        risks[test_slot] = {}
        risks[test_slot]["risky"] = False
        if slots[f"{test_slot}"] == "  ":
           risks[test_slot]["type"] = 0
        elif slots[f"{test_slot}"] == "♖ ":
            risks[test_slot]["type"] = 3
            risks[test_slot]["self"] = True
        elif slots[f"{test_slot}"] == "♘ ":
            risks[test_slot]["type"] = 4
            risks[test_slot]["self"] = True
        elif slots[f"{test_slot}"] == "♗ ":
            risks[test_slot]["type"] = 5
            risks[test_slot]["self"] = True
        elif slots[f"{test_slot}"] == "♔ ":
            risks[test_slot]["type"] = 6
            risks[test_slot]["self"] = True
        elif slots[f"{test_slot}"] == "♕ ":
            risks[test_slot]["type"] = 7
            risks[test_slot]["self"] = True
        elif slots[f"{test_slot}"] == "♙ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            risks[test_slot]["type"] = 2 
            risks[test_slot]["self"] = True           #["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]
        elif slots[f"{test_slot}"] == "♜ ":
            risks[test_slot]["type"] = 3
            risks[test_slot]["self"] = False 
        elif slots[f"{test_slot}"] == "♞ ":
            risks[test_slot]["type"] = 4
            risks[test_slot]["self"] = False 
        elif slots[f"{test_slot}"] == "♝ ":
            risks[test_slot]["type"] = 5
            risks[test_slot]["self"] = False 
        elif slots[f"{test_slot}"] == "♚ ":
            risks[test_slot]["type"] = 7
            risks[test_slot]["self"] = False 
        elif slots[f"{test_slot}"] == "♛ ":
            risks[test_slot]["type"] = 6
            risks[test_slot]["self"] = False 
        elif slots[f"{test_slot}"] == "♟ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            risks[test_slot]["type"] = 2 
            risks[test_slot]["self"] = False      

        if test_slot in range(18,88,10):
            test_slot += 3
        else:
            test_slot += 1
    test_slot = 11
    while test_slot <= 88:
        rewrite_slot = test_slot

        if test_slot == 74:
             lel = 1
        match risks[test_slot]["type"]:
            case 3|13:
                 risks = rook_risk(risks,rewrite_slot)
            case 4|14:
                 risks = knight_risk(risks,rewrite_slot)
            case 5|15:
                 risks = bishop_risk(risks,rewrite_slot)
            case 6|16:
                 risks = queen_risk(risks,rewrite_slot)
            case 7|17:
                 risks = king_risk(risks,rewrite_slot)
            case 2|12:
                 risks = pawn_risks(risks,rewrite_slot)
        if test_slot in range(18,88,10):
            test_slot += 3
        else:
            test_slot += 1


    calc_values(risks,slots)
    