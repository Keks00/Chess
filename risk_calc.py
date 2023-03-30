
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
        if risks[rewrite_slot + -10] in range(0,10):
            risks[rewrite_slot + -10] += 10
        if risks[rewrite_slot + -9] in range(0,10):
            risks[rewrite_slot + -9] += 10
        if risks[rewrite_slot + -1] in range(0,10):
            risks[rewrite_slot + -1] += 10
        if risks[rewrite_slot + 1] in range(0,10):
            risks[rewrite_slot + 1] += 10
        if risks[rewrite_slot + 9] in range(0,10):
            risks[rewrite_slot + 9] += 10
        if risks[rewrite_slot + 10] in range(0,10):
            risks[rewrite_slot + 10] += 10
        if risks[rewrite_slot + 11] in range(0,10):
            risks[rewrite_slot + 11] += 10
    except:
        KeyError
    return risks


def queen_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  

    rewrite_slot += 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    rewrite_slot -= 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break 
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    rewrite_slot += 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    rewrite_slot -= 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 9
    rewrite_slot = rewrite

    rewrite_slot += 1
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    rewrite_slot -= 1
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    rewrite_slot += 10
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    rewrite_slot -= 10
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 10

    return risks

def bishop_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  

    rewrite_slot += 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 11
    rewrite_slot = rewrite
    
    rewrite_slot -= 11
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 11
    rewrite_slot = rewrite
    
    rewrite_slot += 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 9
    rewrite_slot = rewrite
    
    rewrite_slot -= 9
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 9
    return risks


def rook_risk(risks,rewrite):
    rewrite_slot = rewrite
    out_of_range = [19,29,39,49,59,69,79,10,20,30,40,50,60,70,80]  


    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 1
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot += 10
    rewrite_slot = rewrite
    
    
    while rewrite_slot in range(11,89) and rewrite_slot not in out_of_range:
        if risks[rewrite_slot] in range(-9,0):
                risks[rewrite_slot] -= -10
                break
        elif risks[rewrite_slot] in range(0,10) :
            risks[rewrite_slot] += 10
            if risks[rewrite_slot] not in range(0,11):
                 break
        rewrite_slot -= 10
    return risks



def if_risk(slots):
    risks = {}
    test_slot = 11
    while test_slot <= 88:
        if slots[f"{test_slot}"] == "  ":
           risks[test_slot] = 0
        elif slots[f"{test_slot}"] == "♖ ":
            risks[test_slot] = 3
        elif slots[f"{test_slot}"] == "♘ ":
            risks[test_slot] = 4
        elif slots[f"{test_slot}"] == "♗ ":
            risks[test_slot] = 5
        elif slots[f"{test_slot}"] == "♔ ":
            risks[test_slot] = 6
        elif slots[f"{test_slot}"] == "♕ ":
            risks[test_slot] = 7
        elif slots[f"{test_slot}"] == "♙ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            risks[test_slot] = 2            #["♜ ","♞ ","♝ ","♚ ","♛ ","♟ "]
        elif slots[f"{test_slot}"] == "♜ ":
            risks[test_slot] = -3
        elif slots[f"{test_slot}"] == "♞ ":
            risks[test_slot] = -4
        elif slots[f"{test_slot}"] == "♝ ":
            risks[test_slot] = -5
        elif slots[f"{test_slot}"] == "♚ ":
            risks[test_slot] = -6
        elif slots[f"{test_slot}"] == "♛ ":
            risks[test_slot] = -7
        elif slots[f"{test_slot}"] == "♟ ":#["♖ ","♘ ","♗ ","♕ ","♔ ","♙ "]
            risks[test_slot] = -2      

        if test_slot in range(18,88,10):
            test_slot += 3
        else:
            test_slot += 1
    test_slot = 11
    while test_slot <= 88:
        rewrite_slot = test_slot


        match risks[test_slot]:
            case 3:
                 risks = rook_risk(risks,rewrite_slot)
            case 4:
                 risks = knight_risk(risks,rewrite_slot)
            case 5:
                 risks = bishop_risk(risks,rewrite_slot)
            case 6:
                 risks = queen_risk(risks,rewrite_slot)
            case 7:
                 risks = king_risk(risks,rewrite_slot)
            case 2:
                 risks = pawn_risks(risks,rewrite_slot)

        if test_slot in range(18,88,10):
            test_slot += 3
        else:
            test_slot += 1

    calc_values(risks,slots)
    