class Board:

    def __init__(self, board_size=100, snakes={}, ladders={}, player_count=0):
        self.board_size = board_size
        self.snakes = snakes
        self.ladders = ladders
        self.player_count = player_count

    def is_winner(self, player):
        if player.pos == self.board_size:
            print(player.name + " wins the game")
            return True
        return False

    def add_snakes(self, snake_head, snake_tail):
        self.snakes[int(snake_head)] = int(snake_tail)

    def add_ladder(self, ladder_bottom, ladder_top):
        self.ladders[int(ladder_bottom)] = int(ladder_top)

    def check_snake(self, new_pos):
        if new_pos in self.snakes:
            return self.snakes[new_pos]
        return new_pos

    def check_ladder(self, new_pos):
        if new_pos in self.ladders:
            return self.ladders[new_pos]
        return new_pos

    def check_snakes_ladders(self, new_pos):
        flag = True
        while flag:
            temp_pos_snake = self.check_snake(new_pos)
            temp_pos_ladder = self.check_ladder(new_pos)
            if temp_pos_snake != new_pos:
                new_pos = temp_pos_snake
                flag = True
            elif temp_pos_ladder != new_pos:
                new_pos = temp_pos_ladder
                flag = True
            else:
                flag = False
        return new_pos

    def set_player_count(self, player_count=0):
        self.player_count = player_count
