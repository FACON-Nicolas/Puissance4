from typing import List
import os

class player:
    """ creation of the player classe """
    def __init__(self, value: int):
        """ inintialization of the player """
        self.x = 0
        self.move = 100
        self.value = value

    def move_coin(self, distance: int):
        """ move the player coin 
        :param distance : ditance to move
        :type distance : int"""
        self.x = self.x + distance
    

    def place_coin(self, platform: List[List[int]], col: int, value=0):
        if value == 0: value = self.value
        """ place coin in the game's platform 
        :param platform : connect 4's platform
        :type platform : List[List[int]] """
        row = 0
        while (row < len(platform) and platform[row][col] == 0):
            row += 1
        if (row == -1): return
        row -= 1
        platform[row][col] = value
