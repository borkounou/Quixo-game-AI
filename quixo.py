import sys
import pygame
from constants import SQSIZE
from game import Game

def main():
    game = Game()
    board = game.board
    ai = game.ai


    #Main loop
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #g-gamemode
                if event.key == pygame.K_g:
                    game.change_gamemode()

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                
                if event.key ==pygame.K_0:
                    ai.level = 0
                if event.key ==pygame.K_1:
                    ai.level = 1
            
            if event.type ==pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1]//SQSIZE
                col = pos[0]//SQSIZE
                
                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)
                    # print(board.squares)
                    if game.isover():
                        game.running = False


        if game.gamemode =='ai' and game.player == ai.player and game.running:
            pygame.display.update()

            # ai methods
            row, col = ai.eval(board)
            game.make_move(row, col)
            if game.isover():
                game.running = False


    
        pygame.display.update()


main()