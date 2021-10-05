"""
Code wrote by Nicolas FACON, Student in University Institute 
of Technology in Lens, France, I'm a beginner in Python and 
algorithmics and I hope you'll like my game and its development.
"""
#module importation
import pygame, game
from pygame.locals import *

__name__ = '__main__'

power = game.game()
power.make_paths()

#game loop
while power.game_running:
    power.clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT: power.game_running = False
        elif event.type == KEYDOWN and event.key not in power.Touches:
            power.Touches.append(event.key)
        elif event.type == KEYUP and event.key in power.Touches:
            power.Touches.remove(event.key)
            power.isDown = False

    if not power.win:
        if power.joueur:
            if K_RIGHT in power.Touches and 0 <= power.x < 600:
                if not power.isDown: 
                    power.isDown = not power.isDown
                    power.gameplay.move_coin(power,100)
                    power.printer.print_player_coin(power)

            elif K_LEFT in power.Touches and 0 < power.x <= 600:
                if not power.isDown: 
                    power.isDown = not power.isDown
                    power.gameplay.move_coin(power,-100)
                    power.printer.print_player_coin(power)

            elif K_SPACE in power.Touches and not power.isDown:
                power.isDown = not power.isDown
                power.gameplay.place_coin(power)
                if power.gameplay.gagne_dir(power) != 0: power.win = True
        
        else: 
            pygame.time.wait(1000)
            power.x = power.gameplay.place_coin_in_random_place() * 100
            power.printer.print_player_coin(power)
            power.gameplay.place_coin(power)
            if power.gameplay.gagne_dir(power) != 0: power.win = True
    else: 
        if K_SPACE in power.Touches and not power.isDown:
            power.isDown = True
            power.gameplay.reset_game(power)

    power.printer.print_game(power)
    power.printer.print_player_coin(power)
    if power.win : power.printer.print_win(power)
    pygame.display.flip()
pygame.quit() 
