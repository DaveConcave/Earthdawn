
# Earthdawn-Würfel-Funktionen
# Je Würfel (W4, W6, W8, W10, W12, W20) eine Funktion
# Besonderheit: Wird die höchste Augenzahl gewürfelt,
# wird unbegrenzt oft erneut gewürfelt und die Augen hinzuaddiert.

import random

# W4-Würfel-Funktion
def dice_w4():
    result = 0
    max_w4 = 4
    while True:
        dice = random.randint(1,4)
        if dice != max_w4:
            result = result + dice
            return result
        else:
            result = result + max_w4

# W6-Würfel-Funktion
def dice_w6():
    result = 0
    max_w6 = 6
    while True:
        dice = random.randint(1,6)
        if dice != max_w6:
            result = result + dice
            return result
        else:
            result = result + max_w6

# W8-Würfel-Funktion
def dice_w8():
    result = 0
    max_w8 = 8
    while True:
        dice = random.randint(1,8)
        if dice != max_w8:
            result = result + dice
            return result
        else:
            result = result + max_w8

# W10-Würfel-Funktion
def dice_w10():
    result = 0
    max_w10 = 10
    while True:
        dice = random.randint(1,10)
        if dice != max_w10:
            result = result + dice
            return result
        else:
            result = result + max_w10

# W12-Würfel-Funktion
def dice_w12():
    result = 0
    max_w12 = 12
    while True:
        dice = random.randint(1,12)
        if dice != max_w12:
            result = result + dice
            return result
        else:
            result = result + max_w12

# W20-Würfel-Funktion
def dice_w20():
    result = 0
    max_w20 = 20
    while True:
        dice = random.randint(1,20)
        if dice != max_w20:
            result = result + dice
            return result
        else:
            result = result + max_w20
