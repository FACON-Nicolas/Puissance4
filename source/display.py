from typing import List
import pygame

from player import player

class display:
    """ creation of the display classe"""
    def __init__(self):
        """ initialization of the display classe """
        pygame.init()
        pygame.display.init()
        self.WIDTH = 700
        self.HEIGHT = 700
        self.COLUMN_SIZE = 100
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Puissance4')

    def show_game(self, platform: List[List[int]]):
        """ show the game 
        :param platform : connect 4's board
        :type platform : List[List[int]] """
        black = (0,0,0)
        self.surface.fill(black)
        for rows in range(len(platform)):
            for columns in range(len(platform[0])):
                pygame.draw.rect(self.surface, (0, 0, 255), pygame.Rect(columns*self.COLUMN_SIZE, self.COLUMN_SIZE+ (rows*self.COLUMN_SIZE), self.COLUMN_SIZE, self.COLUMN_SIZE))
                pygame.draw.circle(self.surface, self.show_color(platform, (rows, columns)), ((columns*self.COLUMN_SIZE)+self.COLUMN_SIZE//2, self.COLUMN_SIZE+(rows*self.COLUMN_SIZE)+self.COLUMN_SIZE//2), (self.COLUMN_SIZE//2)-5, 0)


    def show_color(self, platform: List[List[int]], case: tuple):
        """ show all coins on the screen
        :param platform : connect 4's board 
        :param case : coin's position 
        :type platform : List[List[int]]
        :type case : tuple(int) 
        :return : player's coin 
        :rtype : pygame.Image """
        row, column = case
        return (255, 255, 0) if platform[row][column] == 1 else (255, 0, 0) if platform[row][column] == 2 else (0, 0, 0)

    def show_player_coin(self, canPlay: bool, player: player):
        """ show the player's coin 
        :param canPlay : if the human player cans play
        :param player : actual player
        :type canPlay : bool
        :type player: player """
        pygame.draw.circle(self.surface, (255, 255, 0) if canPlay else (255, 0, 0), (player.x+self.COLUMN_SIZE//2, 0+self.COLUMN_SIZE//2), (self.COLUMN_SIZE//2)-5)
