import operator
from moves import enemy_figue_choise

def calc_values(risks,slots): 
    point_map = {}
    for key,value in risks.items():
        value_str = (str(value)).strip("-")
        if value_str[:1] != "1":
            value_str = "2" + value_str
        point_map[key] = 0
        try:
            if value_str[1:] == "2":
                point_map[key] = 10
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError
        
        try:
            if value_str[1:] in ["3","4"]:
                point_map[key] = 30
                if value < 0:
                    point_map[key] = -abs(point_map[key])

        except: TypeError

        try:
            if value_str[1:] == "5":
                point_map[key] = 50
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError

        try:
            if value_str[1:] == "6":
                point_map[key] = 90
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError

        try:
            if value_str[1:] == "7":
                point_map[key] = 900
                if value < 0:
                    point_map[key] = -abs(point_map[key])
        except: TypeError
    overall_score(point_map)
    best_move = max(point_map.items(), key=operator.itemgetter(1))
    enemy_figue_choise(best_move,slots)
    return point_map



# combines risks and the pointmap together
def point_map(point_map,risks):
    True
def overall_score(point_map):
    score = []
    for key,value in point_map.items():
        score.append(value)
    score = sum(score)
