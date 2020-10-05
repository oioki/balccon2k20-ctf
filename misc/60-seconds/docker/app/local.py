#!/usr/bin/env python3

from game import Game


def play_one_game():
    game = Game()

    while True:
        result = game.check_game_over()
        if result:
            print(result)
            return

        print(game.state())

        pos = input('> ')
        column = ord(pos[0]) - ord('a')
        row = int(pos[1]) - 1
        game.move(row, column)


if __name__ == '__main__':
    play_one_game()
