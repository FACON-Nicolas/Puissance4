import pygame 

class Joueur:
    def __init__(self, image, value):
        self.image = image
        self.value = value
        
    # methods
    def move_coin(self, addMove, surface):
        self.x += addMove
        self.i += (addMove/100)
        self.i = int(self.i)
        surface.blit(self.image,(self.x, self.y))
    
    # variables initialization
    x = 9
    y = 9
    i = 0
