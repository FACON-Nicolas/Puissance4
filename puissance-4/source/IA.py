from player import *
import random, pygame, doctest

class AI(player):
    """ creation of the AI classe """
    def __init__(self,value):
        """"""
        super().__init__(value)

    def copy_game(self, platform):
        """"""
        return [i.copy() for i in platform]

    def random_place(self, array):
        """"""
        return random.choice(array)

    def get_all_columns(self, platform):
        return [i for i in range(0,700,100) if self.detect_position(platform, i) != -1]

    def detect_position(self, platform, column):
        """"""
        i = 0
        if platform[i][column] != 0: return -1
        while (platform[i][column] == 0 and i < len(platform)): 
            i += 1
            if i not in range(len(platform)): break
        return i

    def remove_columns(self, platform, places):
        return [i for i in places if self.detect_position(platform, i//100) != -1]

    def count_coin_dir(self, platform, direction, col):
        """ 
        >>> count_coin_dir([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,2,0,0,0],[0,0,0,2,0,0,0]], (-1,0), 3)
        2
        >>> count_coin_dir([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[1,2,2,1,2,1,1],[1,2,1,1,2,1,2]], (1,-1), 2)
        3
        """
        comp, i, row = 1,1, self.detect_position(platform, col)
        if row != -1:
            value = platform[row][col]
            row_d, col_d = direction
            if value == 0: return 0
            while (comp < 4):
                row_pos, col_pos = row+(row_d*i), col+(col_d*i)
                in_range = row_pos in range(len(platform)) and col_pos in range(len(platform[0]))
                if in_range: in_range = platform[row_pos][col_pos] == value
                if in_range: comp, i = comp + 1, i + 1
                else:
                    if (row_d, col_d) == direction: 
                        row_d, col_d, i = row_d*-1, col_d*-1, 1
                    else: break
            return comp
        return 0

    def count_coin(self, platform):
        """"""
        comp = 0
        for row_dir in range(-1,2):
            for col_dir in range(-1,2):
                if (row_dir, col_dir) != (0,0):
                    count = self.count_coin_dir(platform, (row_dir, col_dir), self.x // 100)
                    if comp < count: comp = count
        return comp

    def get_best_sequence(self, platform):
        """"""
        places, max = [], 0
        for horizontalPosition in range(0,601,100):
            copy = self.copy_game(platform)
            self.x = horizontalPosition
            self.place_coin(copy)
            coins = self.count_coin(copy)
            if max <= coins:
                if max < coins: 
                    max = coins
                    places = []
                places.append(self.x)
        return places, max

    def get_best_sequence_index(self, platform):
        """"""
        places, max = self.get_best_sequence(platform)
        return self.remove_columns(platform, places) if self.remove_columns(platform, places) != [] else self.get_all_columns(platform)

    def get_best_sequence_max(self, platform):
        """"""
        places, max = self.get_best_sequence_max(platform)
        return max

    def intersection(self, L1, L2):
        """
        >>> intersection([2,3,4,6],[0,3])
        [3]
        """
        return [i for i in L2 if i in L1]

    def AI_gameplay(self, game, platform):
        """"""
        if not game.canPlay and not game.win():
            pygame.time.wait(1000)
            places = self.get_best_sequence_index(platform)
            self.x = self.random_place(places)
            self.place_coin(platform)
            game.canPlay = True
