class player:
    """ creation of the player classe """
    def __init__(self, value):
        """ inintialization of the player """
        self.x = 0
        self.move = 100
        self.value = value

    def move_coin(self, distance):
        """ move the player coin 
        :param distance : ditance to move
        :type distance : int"""
        self.x = self.x + distance
    

    def place_coin(self, platform):
        """ place coin in the game's platform 
        :param platform : connect 4's platform
        :type platform : List[List[int]] """
        column = self.x // self.move
        for i in range(len(platform)):
            row = (len(platform) - (1+i))
            if platform[row][column] == 0: 
                platform[row][column] = self.value
                break
