from typing import List
from player import *
import random, pygame, doctest

class AI(player):
    """ creation of the AI classe """
    def __init__(self,value: int):
        """"""
        super().__init__(value)

    def copy_game(self, platform: List[List[int]]):
        """ get the copy of the game's platform
        :param platform : game's platform 
        :type platform : List[List[int]] 
        :return : the game's platform 
        :rtype : List[List[int]]
        :examples:
        
        >>> copy_game([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[1,2,2,1,2,1,1],[1,2,1,1,2,1,2]])
        [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[1,2,2,1,2,1,1],[1,2,1,1,2,1,2]]

        >>> copy_game([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,1,1,2,1,2,1],[2,1,2,2,1,2,1],[1,2,2,1,2,1,1]])
        [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,1,1,2,1,2,1],[2,1,2,2,1,2,1],[1,2,2,1,2,1,1]] 
        
        """
        return [i.copy() for i in platform]

    def random_place(self, array : List[int]):
        """ choice a random index of the list 
        :param array : cases availables 
        :type array : List[int]
        :return : one of the cases availables 
        :rtype : int """
        return random.choice(array)

    def get_all_columns(self, platform: List[List[int]]):
        """get all columns availables in the platform 
        :param platform : platform of the game 
        :type platform : List[List[int]] 
        :return : all columns availables
        :rtype : List[int] 
        :examples: 
        
        >>> get_all_colums([[2,0,0,0,2,0,1],[2,1,2,1,2,1,2],[2,1,2,1,1,1,2],[1,2,1,1,2,1,1],[2,1,1,2,1,2,2],[1,2,2,1,2,1,2]])
        [1, 2, 3, 5] 
        
        """
        return [i for i in range(7) if self.detect_position(platform, i) != -1]

    def detect_position(self, platform: List[List[int]], column: int):
        """ detect the column's position 
        :param platform : platform of the game 
        :param column : index of the column
        :type platform : List[List[int]] 
        :type column : int
        :return : index of the row
        :rtype : int 
        :examples:
        
        >>> detect_position([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,1,1,2,1,2,1],[2,1,2,2,1,2,1],[1,2,2,1,2,1,1]], 1)
        2

        >>> detect_position([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,1,1,2,1,2,0],[2,1,2,2,1,2,1],[1,2,2,1,2,1,1]], 6)
        3

        >>> detect_position([[2,0,0,0,2,0,1],[2,1,2,1,2,1,2],[2,1,2,1,1,1,2],[1,2,1,1,2,1,1],[2,1,1,2,1,2,2],[1,2,2,1,2,1,2]], 0)
        -1
        
        """
        i = 0
        if platform[i][column] != 0: return -1
        while (platform[i][column] == 0 and i in range(len(platform)-1)): 
            i += 1
        return i

    def remove_columns(self, platform: List[List[int]], places: List[int]):
        """ remove the columns when it is full 
        :param platform : game's platform 
        :param places : list of the cases availables 
        :type platform : list[List[int]] 
        :type places : List[int] 
        :return : list of index availables 
        :rtype : List[int] 
        :examples:
        
        >>> remove_columns([[2,0,0,0,2,0,1],[2,1,2,1,2,1,2],[2,1,2,1,1,1,2],[1,2,1,1,2,1,1],[2,1,1,2,1,2,2],[1,2,2,1,2,1,2]], [0,1,3])
        [1, 3]
         """
        return [i for i in places if self.detect_position(platform, i//100) != -1]

    def count_coin_dir(self, platform: List[List[int]], direction: tuple, col: int):
        """ get the max coin sequence in a direction
        :param platform : game's platform
        :param direction : horizontal and vertical direction
        :param col : index of the column
        :type platform : List[List[int]]
        :type direction : tuple(int)
        :type col : int
        :return : max coin sequence
        :rtype : int
        :examples:

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

    def count_coin(self, platform: List[List[int]], col: int):
        """ get the max coin sequence
        :param platform : game's platform
        :param direction : horizontal and vertical direction
        :param col : index of the column
        :type platform : List[List[int]]
        :type direction : tuple(int)
        :type col : int
        :return : max coin sequence and direction
        :rtype : tuple(int)
        :examples:

        >>> count_coin([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,2,0,0,0],[0,0,0,2,0,0,0]], 3)
        (2, 0)

        """
        comp, dir_r = 0,0
        for row_dir in range(-1,2):
            for col_dir in range(-1,2):
                if (row_dir, col_dir) != (0,0):
                    count = self.count_coin_dir(platform, (row_dir, col_dir), col)
                    if comp < count: 
                        comp = count
                        dir_r = col_dir if row_dir < 0 else -col_dir
        return (comp, dir_r)

    def get_max_coin(self, platform: List[List[int]], col: int):
        """ get max coin sequence in the count_coin()'s tuple
        :param platform : game's platform
        :param direction : horizontal and vertical direction
        :param col : index of the column
        :type platform : List[List[int]]
        :type direction : tuple(int)
        :type col : int
        :return : max coin sequence and direction
        :rtype : int
        :examples:

        >>> get_max_coin([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,2,0,0,0],[0,0,0,2,0,0,0]], 3)
        2

         """
        coin, dir = self.count_coin(platform, col)
        return coin

    def get_dir_coin(self, platform: List[List[int]], col: int):
        """ get max coin sequence in the count_coin()'s tuple
        :param platform : game's platform
        :param direction : horizontal and vertical direction
        :param col : index of the column
        :type platform : List[List[int]]
        :type direction : tuple(int)
        :type col : int
        :return : max coin sequence and direction
        :rtype : int
        :examples:

        >>> get_max_coin([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,2,0,0,0],[0,0,0,2,0,0,0]], 3)
        0
        
        """
        coin, dir = self.count_coin(platform, col)
        return dir

    def get_best_sequence(self, platform: List[List[int]]):
        """"""
        places, max = [], 0
        for col in range(7):
            copy = self.copy_game(platform)
            self.place_coin(copy, col)
            coins = self.get_max_coin(copy, col)
            if max <= coins:
                if max < coins: 
                    max = coins
                    places = []
                places.append(col)
        return places, max

    def get_best_sequence_index(self, platform: List[List[int]]):
        """"""
        places, max = self.get_best_sequence(platform)
        return self.remove_columns(platform, places) if self.remove_columns(platform, places) != [] else self.get_all_columns(platform)

    def get_best_sequence_max(self, platform: List[List[int]]):
        """"""
        places, max = self.get_best_sequence(platform)
        return max

    def intersection(self, L1: List[int], L2: List[int]):
        """

        >>> intersection([2,3,4,6],[0,3])
        [3]

        >>> intersection([2,3,4,6],[1,2,4])
        [2,4]

        >>> intersection([1,2,4,6],[3,5])
        []

        """
        return [i for i in L2 if i in L1]

    def warning_contender_sequence(self, platform: List[List[int]]):
        """ 
        >>> get_best_sequence_contender([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,1,1,2,1,2,1],[2,1,2,2,1,2,1],[1,2,2,1,2,1,1]])
        [3, 6]
        >>> get_best_sequence_contender([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,1,1,2,1,2,1],[2,1,2,2,1,2,1],[2,2,2,1,2,1,2]])
        []
        """
        places, max = [], 3
        for col in range(7):
            copy = self.copy_game(platform)
            self.place_coin(copy, col, 1)
            coins = self.get_max_coin(copy, col)
            if coins >= max: 
                if coins > max: max, places = coins, []
                places.append(col)
        return places 

    def set_places(self, platform: List[List[int]]):
        """"""
        places = self.get_best_sequence_index(platform)  
        if self.get_best_sequence_max(platform) < 4:
            if self.warning_contender_sequence(platform) != []:
                if self.intersection(self.get_best_sequence_index(platform), self.warning_contender_sequence(platform)) != []:
                    places = self.intersection(self.get_best_sequence_index(platform), self.warning_contender_sequence(platform))
                else: places = self.warning_contender_sequence(platform)
        return places

    def AI_gameplay(self, game, platform: List[List[int]]):
        """"""
        if not game.canPlay and not game.win() and not game.platform_is_full():
            pygame.time.wait(1000)
            places = self.set_places(platform)
            self.x = self.random_place(places)
            self.place_coin(platform, self.x)
            game.canPlay = True
