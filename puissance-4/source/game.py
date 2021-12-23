import pygame
from player import player
from pygame.locals import *
from display import display
from IA import AI

class game:
    """"""
    def __init__(self):
        """ initialization of the game """
        #constants
        self.WIDTH = 7
        self.HEIGHT = 6
        self.CONNECT = 4
        #game variables
        self.grille = [[0 for _ in range(self.WIDTH)]for _ in range(self.HEIGHT)]
        self.isInGame = True
        self.keyIsDown = False
        self.game_running = True
        self.canPlay = True
        self.clock = pygame.time.Clock()
        self.Touches = []
        self.player  = player(1)
        self.AI = AI(2)
        self.display = display()

    def run(self):
        """ run loop """
        while self.game_running:
            self.event()
            self.AI.AI_gameplay(self, self.grille)
            self.controls()
            self.controls_game_over()
            self.display.show_game(self.grille)
            self.display.show_player_coin(self.canPlay, self.get_player())
            pygame.display.flip()

    def event(self):
        """ event method """
        self.clock.tick(60)
        self.keyIsDown = len(self.Touches) > 0
        for event in pygame.event.get():
            if event.type == QUIT: self.game_running = False
            elif event.type == KEYDOWN and event.key not in self.Touches:
                self.Touches.append(event.key)
            elif event.type == KEYUP and event.key in self.Touches:
                self.Touches.remove(event.key)
    
    def controls(self):
        """ controls 'classics' method """
        self.isInGame = not(self.win()) and not(self.platform_is_full())
        if (self.isInGame) and (self.canPlay) and (not self.keyIsDown):
            if self.Touches == [K_RIGHT] and self.player.x in range(600):
                self.player.move_coin(self.player.move)
            elif self.Touches == [K_LEFT] and self.player.x in range(1, 601):
                self.player.move_coin(-self.player.move)
            elif self.Touches == [K_SPACE]:
                row, column = 0, self.player.x // 100
                if self.grille[row][column] == 0:
                    self.player.place_coin(self.grille, self.player.x // 100)
                    self.canPlay = False

    def controls_game_over(self):
        """ controls game over method """
        if not self.isInGame and not self.keyIsDown:
            if self.Touches == [K_SPACE]:
                self.__init__()

    def platform_is_full(self):
        """ the platform is full 
        :return : if the platform is full
        :rtype : bool """
        return 0 not in self.grille[0]

    def get_player(self):
        """ get actual player 
        :return : actual player
        :rtype : player | AI (player) """
        return self.player if self.canPlay else self.AI

    def win_dir(self, direction: tuple, case: tuple):
        """ cans know if a player win with certain direction
        :param direction : direction of the 'victory'
        :param case : start position
        :type direction : tuple(int)
        :type case : tuple(int)
        :return : if a player wins
        :rtype : bool """
        row, column = case
        value = self.grille [row][column]
        direction_row, direction_column = direction
        if value == 0: return False
        for _ in range(1, self.CONNECT):
            row, column = row + direction_row, column + direction_column
            if self.grille[row][column] != value: return False
        return True

    def win(self):
        """ cans know if a player win 
        :return : if a player win
        :rtype : bool """
        for row in range(self.HEIGHT):
            for column in range(self.WIDTH):
                for col_dir in range(-1,2):
                    for row_dir in range(-1,2):
                        if (row_dir,col_dir) != (0,0):
                            row_fin, col_fin = row + ((self.CONNECT-1)*row_dir), column + ((self.CONNECT-1)*col_dir)
                            if row_fin in range(self.HEIGHT) and col_fin in range(self.WIDTH):
                                if self.win_dir((row_dir, col_dir), (row, column)):
                                    return True
        return False

jeu = game()
jeu.run()
