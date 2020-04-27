from dice import Dice
from player import Player
from board import Board

DICE_COUNT = 1

if __name__ == '__main__':
    board = Board()
    player_list = []
    dice_list = []
    player_win = 0
    with open('input.txt', 'r') as f:
        snakes_count = int(f.readline())
        for i in range(snakes_count):
            snake_head, snake_tail = f.readline().strip().split(" ")
            board.add_snakes(snake_head = snake_head, snake_tail = snake_tail)
        ladders_count = int(f.readline())
        for i in range(ladders_count):
            ladder_bottom, ladder_top = f.readline().strip().split(" ")
            board.add_ladder(ladder_bottom = ladder_bottom, ladder_top = ladder_top)

        players_count = int(f.readline())
        board.set_player_count(players_count)
        for i in range(players_count):
            player_list.append(Player(name=str(f.readline()).strip()))

        for dice_number in range(DICE_COUNT):
            dice_list.append(Dice())

    while player_win < players_count-1:
        for player_turn in player_list:
            player_turn.play_dice(dice_list[0], board)
            if board.is_winner(player_turn):
                player_win += 1
                print(player_turn.name + " won the game at position: " + str(player_win))
                player_list.remove(player_turn)