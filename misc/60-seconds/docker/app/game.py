import random
import time

from flag import FLAG


N = 8
MOVE_DELAY = 0.400
MOVES_LIMIT = 100  # some boards might be impossible to solve in less than 100 moves; check out max_moves.py
TIME_LIMIT = int(MOVES_LIMIT * MOVE_DELAY * 1.5)  # 60 seconds


class Game:

    def __init__(self):
        self.moves = 0
        self.time_start = time.time()

        while True:
            self.a = []
            for i in range(N):
                self.a.append([])
                for _ in range(N):
                    elem = random.randint(0, 1)
                    self.a[i].append(elem)

            # make the puzzle reasonably hard
            ones = self.count_ones()
            if ones > N*N//2:
                break


    def show(self):
        for i in range(N):
            for j in range(N):
                print(self.a[i][j], end='')
            print()
        print()


    def state(self):
        # header
        output = '   '
        for j in range(N):
            output += ' {} '.format(chr(ord('a') + j))
        output += '\n'

        for i in range(N):
            output += ' {} '.format(i+1)
            for j in range(N):
                output += ' {} '.format(self.a[i][j])
            output += '\n'

        return output


    def count_ones(self):
        # check for solution
        ones = 0
        for i in range(N):
            for j in range(N):
                if self.a[i][j] == 1:
                    ones += 1

        return ones


    def invert(self, i, j):
        self.a[i][j] = (self.a[i][j] + 1) % 2


    def move(self, si, sj):
        # print('Move at ({},{})'.format(si, sj))

        # invert row
        for j in [*range(0, sj), *range(sj+1, N)]:
            self.invert(si, j)

        # invert column
        for i in range(0, N):
            self.invert(i, sj)

        time.sleep(MOVE_DELAY)
        self.moves += 1


    def check_game_over(self):
        dt = time.time() - self.time_start
        if dt > TIME_LIMIT:
            return 'BOOM! (x_x) Too slow...'

        if self.count_ones() == 0:
            return self.state() + 'You made it in {} moves and {} seconds! Here is your reward: {}'.format(self.moves, round(dt, 3), FLAG)

        if self.moves >= MOVES_LIMIT:
            return 'BOOM! (x_x) Too much movement...'

        return None
