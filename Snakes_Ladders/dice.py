import random

START_VAL = 1
END_VAL = 6


def random_int_generate():
    return random.randint(START_VAL, END_VAL)


class Dice:

    def __init__(self):
        pass

    def roll_dice(self):
        count = 0
        dice_roll_val = random_int_generate()
        while dice_roll_val == 6:
            if count >= 3:
                return 0
            count += 1
            dice_roll_val = random_int_generate()
        return 6 * count + dice_roll_val