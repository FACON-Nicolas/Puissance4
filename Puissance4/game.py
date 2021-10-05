import pygame, os, random
from math import sqrt

class game():
        #make the path's game with its files if it doesn't exist
    def make_paths(self):
        if not os.path.exists(self.path):
            self.create_path(self.surface, self.path)
        
    #make the path's game with it's files
    def create_path(self):
            os.mkdir(self.path)
            self.surface = pygame.display.set_mode((100,100))
            self.draw_coin((255,255,0), 'jaune',self.surface, self.path)
            self.draw_coin((255,255,0), 'jaune_fond',self.surface, self.path, (0,0,255))
            self.draw_coin((255,0,0), 'rouge',self.surface, self.path)
            self.draw_coin((255,0,0), 'rouge_fond',self.surface, self.path, (0,0,255))
            self.draw_coin((0,0,0), 'noir',self.surface, self.path, (0,0,255))

    #classe used to print object 
    class printer():
        def print_game(self):
            self.surface.fill((0,0,0))
            for c in range(len(self.Grille[0])):
                for l in range(len(self.Grille)):
                    if self.Grille[l][c] == 0 : self.surface.blit(self.noir, (c*100, (l*100)+100))
                    elif self.Grille[l][c] == 1: self.surface.blit(self.jaune_fond, (c*100, (l*100)+100))
                    elif self.Grille[l][c] == 2: self.surface.blit(self.rouge_fond, (c*100, (l*100)+100))

        #draw coin (use this if the coin doesn't exist)
        def draw_coin(self,color, colorstr, wallpapercolor=(0,0,0)):
            self.surface.fill((wallpapercolor))
            for y in range(82):
                for x in range(82):
                    r = sqrt((x - 41)**2 + (y - 41)**2)
                    if r < 41:
                        self.surface.set_at((x+9,y+9), color)
            pygame.image.save(self.surface, self.path + '/' + colorstr +'.png')

        def print_player_coin(self):
            if self.joueur == True: coin = self.jaune.copy()
            else: coin = self.rouge.copy() 
            self.surface.blit(coin,(self.x,self.y))

        def print_win(self):
            font=pygame.font.Font(pygame.font.match_font('arialblack'), 100, bold=True)
            text = font.render('VICTOIRE !',True,(255,255,255))
            self.surface.blit(text,(175,350))
    
    class gameplay():
        def move_coin(self, distance):
            self.x += distance

        def place_coin(self):
            i = 0
            if self.Grille[0][int((self.x/100))] == 0:
                while self.Grille[i+1][int(self.x/100)] == 0 and  i+1 < len(self.Grille)-1: i+=1
                if (self.Grille[i+1][int(self.x/100)] == 0): i+=1
                if self.joueur : self.Grille[i][int(self.x/100)] = 1
                else : self.Grille[i][int(self.x/100)] = 2
                self.joueur = not self.joueur

        def direction(self, case, direction):
            l,c = case
            dl, dc = direction
            j = self.Grille[l][c] 
            for i in range(1,4):
                l,c = l+dl, c+dc
                if l < 0 or l >= 6 or c < 0 or c >= 7: return 0
                elif not self.Grille[l][c] == j or j == 0: return 0
            return j

        def gagne_dir(self):
            for l in range(6):
                for c in range(7):
                    for dl in range(-1,2):
                        for dc in range(-1,2):
                            if(dl,dc) != (0,0):
                                p = self.gameplay.direction(self, (l,c), (dl,dc))
                                if p != 0: return p
            return 0

        def place_coin_in_random_place():
            return random.randint(0,6)

        def reset_game(self):
            self.Grille=[[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]]
            self.win = False
            self.joueur = True

        def platform_is_full(self):
            for i in range(len(self.Grille[0])): 
                if self.Grille[0][i] == 0: return False
            font=pygame.font.Font(pygame.font.match_font('arialblack'), 100, bold=True)
            text = font.render('Fin de partie !',True,(255,255,255))
            self.surface.blit(text,(10,350))
            return True

    #variables initialization
    pygame.init()
    name = pygame.display.set_caption("PUISSANCE 4")
    path = '/home/' + os.environ['USERNAME'] + '/Documents/Puissance4/'
    surface = pygame.display.set_mode((700,700))

    Touches = []

    x = 0
    y = 0

    game_running = True
    joueur = True
    isDown = False
    win = False
    clock = pygame.time.Clock()

    noir = pygame.image.load(path + 'noir.png').convert_alpha()
    jaune = pygame.image.load(path + 'jaune.png').convert_alpha()
    rouge = pygame.image.load(path + 'rouge.png').convert_alpha()
    jaune_fond = pygame.image.load(path + 'jaune_fond.png').convert_alpha()
    rouge_fond = pygame.image.load(path + 'rouge_fond.png').convert_alpha()

    Grille=[[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]
