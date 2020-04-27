class Player:

    def __init__(self, pos=0, name=""):
        self.pos = pos
        self.name = name

    def play_dice(self, dice, board):
        dice_val = dice.roll_dice()
        next_pos = dice_val + self.pos
        old_pos = self.pos
        if next_pos <= 100:
            self.pos = board.check_snakes_ladders(next_pos)
        print(self.name + " rolled a " + str(dice_val) + " and moved from " + str(old_pos) + " to " + str(self.pos))
        return self.pos