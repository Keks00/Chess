# chess board
def chess_board(slots):
    print("\t\t\t  Chess Board")    
    print("\t\t     a  b  c  d  e  f  g  h")
    print("\t\t8  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["81"],slots["82"],slots["83"],slots["84"],slots["85"],slots["86"],slots["87"],slots["88"]))
    print("\t\t7  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["71"],slots["72"],slots["73"],slots["74"],slots["75"],slots["76"],slots["77"],slots["78"]))
    print("\t\t6  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["61"],slots["62"],slots["63"],slots["64"],slots["65"],slots["66"],slots["67"],slots["68"]))
    print("\t\t5  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["51"],slots["52"],slots["53"],slots["54"],slots["55"],slots["56"],slots["57"],slots["58"]))
    print("\t\t4  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["41"],slots["42"],slots["43"],slots["44"],slots["45"],slots["46"],slots["47"],slots["48"]))
    print("\t\t3  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["31"],slots["32"],slots["33"],slots["34"],slots["35"],slots["36"],slots["37"],slots["38"]))
    print("\t\t2  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["21"],slots["22"],slots["23"],slots["24"],slots["25"],slots["26"],slots["27"],slots["28"]))
    print("\t\t1  |%s|%s|%s|%s|%s|%s|%s|%s|" % (slots["11"],slots["12"],slots["13"],slots["14"],slots["15"],slots["16"],slots["17"],slots["18"]))

#reset
def reset():
    slots = {
    "11": "♖ ",
    "12": "♘ ",
    "13": "♗ ",
    "14": "♕ ",
    "15": "♔ ",
    "16": "♗ ",
    "17": "♘ ",
    "18": "♖ ",
    "21": "♙ ",
    "22": "♙ ",
    "23": "♙ ",
    "24": "♙ ",
    "25": "♙ ",
    "26": "♙ ",
    "27": "♙ ",
    "28": "♙ ",
    "31": "  ",
    "32": "  ",
    "33": "  ",
    "34": "  ",  
    "35": "  ",
    "36": "  ",
    "37": "  ",
    "38": "  ",
    "41": "  ",
    "42": "  ",
    "43": "  ",
    "44": "  ",
    "45": "  ",
    "46": "  ",
    "47": "  ",
    "48": "  ",
    "51": "  ",
    "52": "  ",
    "53": "  ",
    "54": "  ",
    "55": "  ",
    "56": "  ",
    "57": "  ",
    "58": "  ",
    "61": "  ",
    "62": "  ",
    "63": "  ",
    "64": "  ",
    "65": "  ",
    "66": "  ",
    "67": "  ",
    "68": "  ",
    "71": "♟ ",
    "72": "♟ ",
    "73": "♟ ",
    "74": "♟ ",  
    "75": "♟ ",
    "76": "♟ ",
    "77": "♟ ",
    "78": "♟ ",
    "81": "♜ ",
    "82": "♞ ",
    "83": "♝ ",
    "84": "♛ ",
    "85": "♚ ",
    "86": "♝ ",
    "87": "♞ ",
    "88": "♜ ",
    }
    chess_board(slots)
    return slots

