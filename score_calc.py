import operator
from moves import enemy_figue_choise

def calc_values(risks,slots): 
    point_map = {}

    for key,value in risks[value]["type"].items():

        if value != 1:
            value = "2" + value
        point_map[key] = 0
        try:
            if value == 2:
                point_map[key] = 10
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError
        
        try:
            if value in [3,4]:
                point_map[key] = 30
                if value < 0:
                    point_map[key] = -abs(point_map[key])

        except: TypeError

        try:
            if value == 5:
                point_map[key] = 50
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError

        try:
            if value == 6:

                point_map[key] = 90
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError

        try:
            if value == 7:
                point_map[key] = 900
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError
    overall_score(point_map)
    print(point_map)
    best_move = max(point_map.items(), key=operator.itemgetter(1))[0]
    f_slot,sucess = enemy_figue_choise(best_move,slots)
    if sucess == False:
        recalc(best_move,risks,slots)
        exit
    
    print("From: ",f_slot,"To: ",best_move)

    return point_map



# combines risks and the pointmap together


def overall_score(point_map):
    score = []
    for key,value in point_map.items():
        score.append(value)
    score = sum(score)
    print(score)

def figure(pieces):
    if len(pieces) == 0:
        return 0, True
    best_move = max(pieces)
    print(best_move)
    return best_move, True

# if no figure is ideal
def recalc(best_move,risks,slots):
    del risks[best_move]
    print("!!!")
    print(risks)
    calc_values(risks,slots)