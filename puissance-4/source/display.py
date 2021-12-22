import pygame
from pygame.constants import SHOWN

class display:
    """ creation of the display classe"""
    def __init__(self):
        """ initialization of the display classe """
        pygame.init()
        pygame.display.init()
        self.WIDTH = 700
        self.HEIGHT = 700
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.surface_name = pygame.display.set_caption('Puissance4')
        self.carre = pygame.image.load('../images/carre.png').convert_alpha()
        self.yellow = pygame.image.load('../images/jaune.png').convert_alpha()
        self.red = pygame.image.load('../images/rouge.png').convert_alpha()

    def show_game(self, platform):
        """ show the game 
        :param platform : connect 4's board
        :type platform : List[List[int]] """
        black = (0,0,0)
        self.surface.fill(black)
        for rows in range(len(platform)):
            for columns in range(len(platform[0])):
                coin = self.show_coin(platform, (rows, columns))
                self.surface.blit(self.carre, (columns*100, (rows*100)+100))
                if coin is not None : self.surface.blit(coin, ((columns*100), 100 + rows*100))

    def show_coin(self, platform, case):
        """ show all coins on the screen
        :param platform : connect 4's board 
        :param case : coin's position 
        :type platform : List[List[int]]
        :type case : tuple(int) 
        :return : player's coin 
        :rtype : pygame.image 
        TODO : add unit test """
        row, column = case
        if platform[row][column] == 1: return self.yellow.copy()
        elif platform[row][column] == 2: return self.red.copy()

    def show_player_coin(self, canPlay, player):
        """ show the player's coin 
        :param canPlay : if the human player cans play
        :param player : actual player
        :type canPlay : bool
        :type player: player """
        coin = self.yellow.copy() if canPlay else self.red.copy()
        self.surface.blit(coin, (player.x, 0)) 
